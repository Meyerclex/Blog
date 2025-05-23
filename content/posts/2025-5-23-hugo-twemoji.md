---
title: "如何在Hugo博客中使用Twemoji🍻"
date: 2025-05-23
slug: "2025-05-23-Twemoji" 
draft: false
tags:
  - monthly
description: 这么折腾一番完全是出于好奇。
comment: true
toc: true
layout: ""
---

<style>
#post-content .temoji img.emoji {
    height: 3em;
    width: 3em;
    margin: 0 .15em;
    vertical-align: -0.8em;
}
</style>

## 不负责任的Emoji小记

这周上网乱逛，看到网友的动态博客站点的默认Emoji样式很好看，于是产生了一个疑问，那就是我的博客中，Emoji到底是如何呈现的。

首先，以下是几个比较常见的Emoji样式：

| **Google** | **iOS** | **Twemoji** | **Microsoft**                              |
| :------------------------- | :--------------------- | :------------------------------------- |:-------------------------------------------|
| ![](/blog/Google.png)      | ![](/blog/iOS.png)     | ![](/blog/loudly-crying-face_1f62d.webp) | ![](/blog/anxious-face-with-sweat-730.png) |

在我的Windows设备上打开博客，我的Emoji通常呈现第四种。存在比较粗的黑色描边。在Mac和iPhone上打开则是第二种，立体感强。第一种在我印象里应该某个APP上非常常见，因为我记得我很喜欢这个黄豆伤心脸。但一时想不起来了。

<div class="temoji">

在长毛象中，我们输出Emoji发出后，经常看到的是第三种，它的黄豆哭脸“😭”表现力很强，成排使用效果更佳：😭😭😭😭……但也可能是我用多了习惯了。

</div>

我已经记不清在来长毛象之前我对这种样式的Emoji是什么感受了。用多了只觉得血萌（？）它似乎是Twitter设计的Emoji，特点是扁平，没有描边。

---

那么，<mark>为什么我们在自己的打出Emoji符号后，不同的设备能够接收到它，并自动呈现出特定风格的图标呢？</mark>

这是因为所有的Emoji它们共享着一套Unicode，感兴趣的朋友可以搜索一下Emoji的历史。简单来说就是1999年日本的一位设计师创建了一个Emoji字符集，是为了日本的手机设计的，最初只是在日本运营商内部存在标准，无法跨平台显示，随着智能手机兴起，2010年Unicode Consortium（统一码联盟）把Emoji纳入到了Unicode标准。

Unicode给Emoji们赋予了唯一的代码与具体的含义。每一个Emoji的代码与含义，都可以在[Unicode官方文档](https://unicode.org/emoji/charts/full-emoji-list.html)中找到。

当我们发送一个“😢”表情时，它在Unicode的标准里的代码是“U+1F622”，表示Crying face。而“😭”表情的意思是**Loudly** crying face……哭得会更大声。

回到博客本身，Hugo博客是不自带任何特定Emoji的。一般情况下我们在Markdown文档里打出一个哭脸，实际上只是指定了这个Emoji的代码，如“U+1F622”。于是，你在iPhone上会看到带有立体感风格的表情，在Windows上则会看到有黑色描边的表情风格。默认情况下，这取决于你打开一个Hugo博客时所使用的设备。

那么小记到此为止，不保证上述内容没有表述方面错误，但大体应该不差。

---

## 😉那么，如何在Hugo博客中使用Twemoji呢？

### 一些前言废话

由于觉得我常用设备上带黑边的表情和博客主题风格不符，网上搜索的时候发现了[hugo-mod-twemoji](https://github.com/jakejarvis/hugo-mod-twemoji)这个库，它可以把博客中的Emoji都指定为Twemoji的风格。Twemoji没有描边而且很亲切，于是开始折腾。

这个库的原理（在我理解中）是将Twemoji官方库的表情下载到本地，然后每当你在Markdown在使用Emoji时，它会识别出其表情代码，然后在你部署为静态网页的时候自动将它们替换为一个svg/png图片。

因此这种方法也将统一不同设备的显示效果，不管在哪种设备上使用，都将显示为统一的Twemoji。

如仓库中说明所述，我们可以用`hugo-mod`来引入，方法非常简单。按照Usage一步步操作即可，但这将导致的一个问题是，它会下载七千多个表情文件放在`public/twemoji`里，导致每次部署都会很久（我日常本地部署大概200ms左右，这个方法会把速度拖到9000-16000ms），吓得我忙不迭复原了。

事实上这七千多个表情文件，有一半都是重复的，因为这种Mod方式会默认下载png和svg两种格式，我们只使用一种就可以了。其次是我们日常使用的基础Emoji数量不多，例如有两百多个国家旗帜，我从未使用过，例如每一个人物Emoji，都会有由深至浅的五种肤色变体和两种性别变体（我们上面使用的示例，都是没有任何肤色和性别的默认Emoji），我觉得只保留基本的Emoji也是可以的。

在后文中，我会解释我筛选出自己大致要用的Emoji范围的过程，但即便如此，我也保留了1700+的表情svg文件。而第一次本地预览时完整建构的速度是1900ms，而后续文件修改时再次建构还是能回到正常的200ms左右。这个速度我还是可以接受的。

### 开始吧！

放弃仓库作者推荐的使用Hugo Mod以后，我们要做的是手动把表情拉取下来，并进行整理筛选。

1. 打开[twemoji.min.js](https://cdn.jsdelivr.net/npm/twemoji@14.0.2/dist/twemoji.min.js)链接后`ctrl+s`，将脚本保存到`assets/js`目录下。

2. 在`static`目录里创建一个新的子文件夹，例如：`static/my-emojis/`，此处将放置表情文件。

3. 访问[twemoji](https://github.com/twitter/twemoji/releases)，从Release里下载最近更新的压缩包（在`Assets`下，你会看到两个`Source code`，下载其中一个即可）。
   
    下载后得到`twemoji-14.0.2.zip`，解压缩后在`\twemoji-14.0.2\assets\svg`，将这一整个`svg`，拖入到你的`static\my-emojis\`文件夹中。

4. 将如下代码放入你`layouts/baseof.html`文件中的`</body>`标签前

```
    {{ $twemojiJS := resources.Get "js/twemoji.min.js" }}
    <script src="{{ $twemojiJS.RelPermalink }}"></script>
    <script>
       document.addEventListener('DOMContentLoaded', function() {
            twemoji.parse(document.body, {
            base: '{{ "/my-emojis/" | relURL }}', 
            folder: 'svg', 
            ext: '.svg' 
            });
            });
    </script>
    
    <!--这段代码的意思是，在你的博客中引入步骤1的JS代码，它会扫描你网页内的内容，将所有Emoji字符都替换为步骤3中的你放入在/my-emojis/文件夹内的svg图片。-->
    <!--下方还有一个</body>标签，表示放在这个标签前，如果重复请删除。-->
</body>
```

5. 在你的CSS文件（如`assets/css/main.scss`）中，加入以下代码：

```
    img.emoji {
    height: 1.2em; /* 如果需要像毛象一样大，则height和width都设置为1.8em */
    width: 1.2em;
    margin: 0 .15em; 
    vertical-align: -0.2em; /* 表情在文字间对齐可以微调 */
    border-radius: 0px;
    }
```

此时构建部署，文字内所使用的Emoji应该可以显示为Twemoji风格了。倘若不行，也许是步骤4中的代码放错了位置，或者博客内有多个`baseof.html`需要放置不止一个位置，这需要根据不同主题模板情况来判断。

### 选做：Emoji筛选

完成上述步骤后，`static\my-emojis\svg`文件夹下应该有3600+个图标，大概在8M左右。如前言所述，如果不需要那么多图标，我们可以到文件夹内手动删掉一些。

1. 国旗Emoji我完全不需要，它们通常以`1f1xx-1f1xx`形式出现，必然存在一个`-`，因此直接搜索`1f1`，将有`-`的表情图标直接全选删掉。
   
    而`1f1f3.svg`这类没有横杠的，都是字母数字🔠1️⃣之类。考虑保留。

2. 肤色变体我几乎不用。将包含肤色代码的表情搜索并删除：

   `1f3fb (浅肤色)`
   `1f3fc (中浅肤色)`
   `1f3fd (中等肤色)`
   `1f3fe (中深肤色)`
   `1f3ff (深肤色)`

肤色变体数量非常多，删掉以后基本已经只剩下1.7k表情了，文件夹在5M左右，也差不多啦，也可以根据个人进一步精简。其实我还删掉了一些人物职业之类的表情，反正我只用黄豆小脸嘛🥺手球运动员Emoji对我有什么意义……！

这么折腾一番完全是出于好奇。其实我Emoji也用得不多（……）毕竟人家，也不是中学生了啊。

## 彩蛋时间

<details>
<summary>「来自豆瓣的抽象文案效果一览」</summary>
<div class="temoji">
我实话和你说了吧😩😩我人生最后悔的事情😫😫就是和你结婚✋💔💔太痛苦了🤮🤮🤮我受不了啦😩😩😩我放着自己大好人生不过😖我🤧🤧我和你结婚😢😢太——痛——苦——了——😭😭太——痛苦了——
</div>
</details>

总之，Happy twemoji！
