import os
import yaml
from collections import Counter

CONTENT_DIR = "content"  # 你的 Hugo 文章目录

def extract_tags_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if lines[0].strip() != "---":
        return []
    try:
        # 提取 front matter 区块
        end = lines[1:].index("---\n") + 1
        front_matter = "".join(lines[1:end])
        metadata = yaml.safe_load(front_matter)
        tags = metadata.get("tags", [])
        if isinstance(tags, list):
            return tags
    except Exception as e:
        print(f"Error in file {filepath}: {e}")
    return []

def analyze_tags():
    tag_counter = Counter()
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                tags = extract_tags_from_file(filepath)
                tag_counter.update(tags)

    # 输出结果
    print("📊 Tag 使用频率统计：")
    for tag, count in tag_counter.most_common():
        print(f"{tag:30} {count} 次")

if __name__ == "__main__":
    analyze_tags()
