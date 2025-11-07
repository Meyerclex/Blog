import os
import frontmatter
from datetime import date
from dateutil import parser # 导入日期解析库
from collections import Counter # 新增导入：用于高效统计标签频率

# 1. 配置参数
# ----------------------------------------------------
# 假设您的文章都在这个目录下
# 修复了路径问题，使用正斜杠或原始字符串
CONTENT_DIR = "D:/Github Repo/Blog/content/posts"
# 年度报告年份
TARGET_YEAR = 2025
# 输出的 Markdown 文件名
OUTPUT_FILE = f"Annual_Report_{TARGET_YEAR}_Blog_Stats.md"
# ----------------------------------------------------

def count_words(filepath):
    """
    一个简单的字数统计函数（忽略 Front Matter）
    FIXED: 针对中文内容，改为统计非空白字符数
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # 找到 Front Matter 的结束位置 (第二个 '---')
            parts = content.split('---', 2)
            if len(parts) < 3:
                 # 如果没有 Front Matter，统计全部内容
                 body = content
            else:
                 # 提取文章主体 (忽略 Front Matter)
                 body = parts[2]
            
            # --- 修复点：针对中文统计字数 ---
            # body.split() 会按所有空白符（空格、换行等）分割，得到非空白内容的列表
            # "".join() 将这些内容重新连接起来，形成不含任何空白符的纯文本
            # len() 计算的就是纯文本的字符数，这对于中文统计是准确的。
            character_count = len("".join(body.split()))
            return character_count
            
    except Exception as e:
        # 统一处理文件读取和字数统计中的错误
        print(f"Error counting words in {filepath}: {e}")
        return 0

def generate_stats_table():
    """
    遍历文章目录，提取数据、聚合统计并生成 Markdown 表格
    """
    all_posts_data = []
    # 新增：用于聚合统计的变量
    tag_frequency = Counter() # 标签频率计数器
    total_word_count = 0     # 总字数计数器
    
    # 遍历目录
    for root, _, files in os.walk(CONTENT_DIR):
        for filename in files:
            if filename.endswith((".md", ".markdown")):
                filepath = os.path.join(root, filename)
                
                try:
                    # 使用 frontmatter 库解析文件
                    with open(filepath, 'r', encoding='utf-8') as f:
                        post = frontmatter.load(f)
                        metadata = post.metadata
                        
                        post_date_raw = metadata.get('date')
                        post_date = None
                        
                        # === 健壮的日期解析（为后续年份检查做准备） ===
                        if post_date_raw:
                            try:
                                if isinstance(post_date_raw, str):
                                    post_date = parser.parse(post_date_raw)
                                else:
                                    post_date = post_date_raw
                                    
                            except Exception:
                                print(f"Warning: Cannot parse date for file {filename} (Raw: {post_date_raw}). Skipping year check.")
                        
                        # === 核心过滤规则：排除草稿、隐藏文章、日期缺失/不符合要求的文章 ===
                        
                        # 1. 排除草稿 (draft: true)
                        if metadata.get('draft') is True:
                            print(f"Skipping file {filename}: Draft is set to True.")
                            continue
                            
                        # 2. 排除隐藏文章 (hidden: true)
                        if metadata.get('hidden') is True:
                            print(f"Skipping file {filename}: Hidden is set to True.")
                            continue

                        # 3. 排除日期缺失的文章
                        if not post_date_raw:
                             print(f"Skipping file {filename}: Date is missing.")
                             continue
                             
                        # 4. 排除日期不在目标年份的文章
                        if not (post_date and hasattr(post_date, 'year') and post_date.year == TARGET_YEAR):
                             print(f"Skipping file {filename}: Date ({post_date}) is not in {TARGET_YEAR}")
                             continue
                            
                        # === 提取所需数据（已通过所有检查） ===
                        title = metadata.get('title', 'N/A')
                        description = str(metadata.get('description', 'N/A')) 
                        
                        # 标签安全处理：确保是列表并过滤 None
                        tags_list = metadata.get('tags', [])
                        if not isinstance(tags_list, list):
                            tags_list = [] 
                        
                        clean_tags_list = [str(t) for t in tags_list if t is not None]
                            
                        tags = ", ".join(clean_tags_list) if clean_tags_list else 'N/A'
                        word_count = count_words(filepath)
                        
                        # === 聚合统计：更新总字数和标签频率 ===
                        total_word_count += word_count
                        tag_frequency.update(clean_tags_list)
                        
                        # 将数据添加到列表中
                        all_posts_data.append({
                            'Title': title,
                            'Description': description,
                            'Tags': tags,
                            'Date': post_date.strftime('%Y-%m-%d'), # 格式化日期
                            'Word_Count': word_count
                        })
                            
                except Exception as e:
                    # 捕获 Front Matter 解析过程中可能出现的其他错误
                    print(f"Skipping file {filepath} due to critical parsing error: {e}")

    # 2. 排序 (可选: 按日期排序)
    all_posts_data.sort(key=lambda x: x['Date'])

    # 3. 生成 Markdown 输出内容
    
    final_markdown_output = []
    num_articles = len(all_posts_data)
    
    # ===============================================
    # 3.1 生成数据概览部分（标签频率和总字数）
    # ===============================================
    
    avg_word_count = int(total_word_count / num_articles) if num_articles > 0 else 0

    final_markdown_output.extend([
        f"## 📊 {TARGET_YEAR} 年度博客数据概览",
        "",
        "| 指标 | 统计结果 |",
        "| :--- | :---: |",
        f"| **文章总数** | {num_articles} 篇 |",
        f"| **总字数** | {total_word_count:,} 字 |", # 格式化数字，带千位分隔符
        f"| **平均字数** | {avg_word_count:,} 字 |",
        "",
        "### 🏷️ 标签频率统计 (按使用次数降序)",
    ])
    
    # 格式化标签频率列表
    tag_list_markdown = []
    if tag_frequency:
        for tag, count in tag_frequency.most_common():
            tag_list_markdown.append(f"- **{tag}**: {count} 篇")
    else:
        tag_list_markdown.append("- 本年度文章中未找到有效标签。")

    final_markdown_output.extend(tag_list_markdown)
    final_markdown_output.append("\n") # 确保概览和列表之间有空行
    
    # ===============================================
    # 3.2 生成文章列表部分
    # ===============================================

    final_markdown_output.extend([
        f"## 📅 {TARGET_YEAR} 年度博客文章列表 ({num_articles} 篇)",
        "",
        "| 序号 | 发布日期 | 文章标题 | 标签 | 摘要/描述 | 字数 |",
        "| :---: | :---: | :--- | :--- | :--- | :---: |"
    ])
    
    # 表格行
    for i, data in enumerate(all_posts_data, 1):
        # 限制 Description 长度，避免表格过宽
        short_desc = (data['Description'][:50].replace('\n', ' ') + '...') if len(data['Description']) > 50 else data['Description'].replace('\n', ' ')
        
        row = (
            f"| {i} "
            f"| {data['Date']} "
            f"| **{data['Title']}** "
            f"| {data['Tags']} "
            f"| {short_desc} "
            f"| {data['Word_Count']} |"
        )
        final_markdown_output.append(row)

    # 4. 写入文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_markdown_output))
        
    print(f"\n✅ 统计完成！Markdown 表格已保存到: {OUTPUT_FILE}")
    print(f"共统计到 {num_articles} 篇 {TARGET_YEAR} 年的文章。")


if __name__ == "__main__":
    if not os.path.isdir(CONTENT_DIR):
        print(f"❌ 错误: 目录 {CONTENT_DIR} 不存在。请检查 CONTENT_DIR 变量设置。")
    else:
        generate_stats_table()