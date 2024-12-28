---
title: "Hugo Luna | 换上了新主题，一边装修一边相声"
date: "2022-05-06"
draft: false
description: "装修To do List一件也没干，贫嘴扯淡已经写满800字。"
# author: Author
# featured_image: cover.jpg
slug: hugo-luna
toc: true
categories:
  - 为沙滩插上太阳伞
tags:
  - Hugo
  - Blog
hidden: true 
---

> 这篇文章的内容已不再适用。

---

Luna 主题经常更新，文章内容可能已经过时。Luna 主题作者的非常热心，主题 Issue 板块是最好的求助渠道。

---

昨天跟 Missing 聊天，说有动换主题的念头，但我们都非常喜欢 Stack 主题的搜索功能，而大多数主题都需要额外配置这一部分。于是随手 Google 一下 Hugo theme，筛选了近一个月的结果——忽然找到了 Luna 主题，作者上周刚发了自荐的帖子，点进去摸摸看看，搜索和字数统计一应俱全，而且配色春意盎然非常漂亮，尽管已经入夏，仍然与友友敲手决定换上。但刚摸上没多久就报错连连，所以决定写篇新博客记录这个主题的安装及装修过程。

> 有一些修改直接参考了上一篇博客装修：[Hugo Stack | 删删改改大胆行事](https://gregueria.icu/posts/decoration/)。
>
> 说给小鸟：不要把博客当成备忘录来写。
>
> 再次说给小鸟：多写博客少装修啦 XD

## To do List

<details>

- [x] Waline 评论区配置 | 在主题作者的帮助下完成了！
- [x] 没有评论区那就加个首页公告（？）好了，评论区可以没有，喜剧效果要先拉起来。
- [x] 全站字数统计
- [x] 解决掉站点的 Icon 问题——为什么是大葱啦！ | 同样在主题作者帮助下完成了！
- [x] Front-matter 里的 Summary 变量改为 Description（这该怎么办？我之前都是用 Description，不会要我全部改一遍吧，不可能啦！）
- [x] About 页里点上一页会出来什么东西，人家想删掉（但是兔狲也蛮可爱的……但是这是什么啊！也是为了喜剧效果吗！）|front-matter 写错带来的问题改好了！
- [x] 修改首页卡片，显示字数而非阅读时间
- [x] 删掉 Summary 后面的“...”，这个真的很紧急人家受不了这个
- [x] Run-time 仅保留天数，拜托！跳秒针看得我好焦虑诶！
- [x] 评论区夜间模式配置
- [x] 一键到顶按钮和聊天小气泡我全都要！
- [ ] 修改代码块颜色

</details>

诶？怎么装修 To do List 一件没干，贫嘴扯淡已经写满 800 字。

## 主题安装

Luna 主题需要 0.97.0 extended 版本的 Hugo。相关准备[塔塔的教程](https://mantyke.icu/2021/hugo-build-blog/)已经写的很清楚了。我原本的 Hugo 版本太低所以需要重新下载，直接覆盖掉原本的`Hugo.exe`。

同时根据这个文档的指示，安装 NodeJs 和 postcss-cli，关于后者的安装，按住`Win+R`，输入`cmd`，输入`npm install postcss-cli -g`。

总而言之，换好以后，去 Github 上新建一个仓库，在 E 盘随便哪个盘右键`git bash here`，然后输入`hugo new site luna`（Luna 是站点文件夹的名字）。接着进去这个文件夹，同样右键选择`git bash here`，依次敲下：

```
git init
git add .
git commit -m ‘first commit’
git remote add origin https://github.com/yourgithubID/gitRepo.git #链接为你新建的仓库的链接
git push -u origin master #将本地仓库push到远程仓库
```

这样就算是把你的一个空白站点 push 到远方仓库上了。

PS：我琢磨来去感觉还是不习惯敲命令行 push and pull……所以后面思索一番，干脆在 Github Desktop 把这个仓库又 Clone 下来了，后续直接在这个 Clone 下来的文件夹里操作，Github Desktop 可以监控到文件改动，轻声询问我要要不要 commit 呀 push 呀……真好（？）

这个主题直接把安装包解压在 theme 文件夹里似乎不可行，连连报错，所以还是建议直接按照文档提示，在站点文件夹根目录执行：

```
git submodule add https://github.com/Ice-Hazymoon/hugo-theme-luna themes/hugo-theme-luna
cd themes/hugo-theme-luna
npm install
```

如果报错告诉你没找到这个仓库之类的，敲一下`git init`应该可以解决。

接着把它的主题文件夹里的`exampleSite`目录中的东西全部复制出来，包括`Content`文件夹。由于它是多语言的主题而我完全不需要，所以直接把`Config.yaml`的多语言部分全部注释掉了，`Content`文件夹里的英语文件夹也删了（冷酷）。那么现在把自己的文章都迁移进去，包括装有图片等文件的`Static`文件夹也复制到站点根目录里，修改`Config.yaml`，接着在 Github Desktop 里 Push 上去，嗯嗯……在这里我经历了人生最久的一次 Push，洗完澡回来它才结束，好像是因为这个主题太花哨沉重了……可是真的很漂亮诶！

接着去 Vercel 把这个仓库 import 进去，接着在这几个地方需要注意一下：

<img src="https://raw.githubusercontent.com/Meyerclex/image/main/20220506164743.png"/>

1. `BUILD COMMAND`中写入：`npm install hugo-extended --save-dev`。关于这一步是因为我发现直接部署会出现`command “Hugo -D --gc”exited with 255`的报错，并且应该不是只有我一个人遇到了这个麻烦。这里我参考了[这个帮助里的指示](https://discourse.gohugo.io/t/netlify-build-error-255-tocss-troubleshooting/25887)，并不是很清楚这个原理，不过总之报错解决顺利 Deploy 了（？
2. 添加环境变量`HUGO_VERSION`，这个主题至少需要 0.97.0，我填了最新的 0.98.0。

如果你在这一步遇到了这个报错：

<img src="https://raw.githubusercontent.com/Meyerclex/image/main/Inked%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220506170623_LI.jpg"/>

那么就在站点根目录下敲命令`Hugo`，它会直接生成一个`Public`文件，之后继续 Deploy 就好了。

### 关于 Luna 主题

这个主题在第一次安装时用`hugo server`命令会话比较长的时间，在它第一次生成了 Public 文件夹之后会好很多。建议在每一次更改主题内容或者写新文章之后用`hugo`命令生成一次站点再 Push，不然会因为本地预览可以看见更改、Push 上去却毫无动静而稍稍有些抓狂。我猜测时因为它真的有太多神秘而复杂的 Feature 了。

`i18n\zh-cn.yaml`里可以修改绝大部分文字花活。如果你希望在导航栏上增加一个新页面，除了在`config.yaml`中增加类似以下的内容之外：

```
    - name: Album
      weight: 39
      identifier: album
      params:
        icon: eva eva-film-outline
      url: /posts/album/
```

还需要再`i18n\zh-cn.yaml`文件夹里加一行这个（与上面的`identifier`变量保持一致），移动端的图标文字部分才能正常显示：

```
navbar:
    album: "Album"
```

## 修改文章链接显示

我一开始没有意识到这个问题，直到我发现我过去贴出的自己的文章链接都 404 啦！原因是两个主题生成的文章链接不同。

我过去的链接形式都是`gregueria.icu/posts/slug`，而这个主题的默认显示形式是`gregueria.icu/2019/01/01/slug.html`，直接修改`Config.toml`中的`permalinks`部分：

```
permalinks:
  # 文章链接的格式
  # Format of posts links
  posts: /posts/:slug # 连同.html一起删掉
```

## 全站字数统计

这一部分感谢[塔塔的站点总字数显示教程](https://mantyke.icu/2022/stack-theme-furnish03/#%E5%8D%87%E7%BA%A7%E8%BF%9B%E5%8C%96%E6%9C%AC%E7%AB%99%E6%80%BB%E5%AD%97%E6%95%B0%E6%98%BE%E7%A4%BA)！完全是复制粘贴 😭

在`layouts\partials\html\footer.html`文件中增添下面中间部分的内容：

```
        <span>Sitemap</span>
    </a>

    {{$scratch := newScratch}}
    {{ range (where .Site.Pages "Kind" "page" )}}
        {{$scratch.Add "total" .WordCount}}
    {{ end }}
    {{$var :=  $scratch.Get "total"}}{{$var = div $var 100.0}}{{$var = math.Ceil $var}}{{$var = div $var 10.0}}&nbsp;&nbsp;共书写了<font color="#dd6065">&nbsp;{{$var}}k&nbsp;</font>字

    {{- if .Site.Params.googleTranslate -}}<div id="google_translate_element" class=" rounded border dark:border-darkBorder overflow-hidden"></div>{{- end -}}
```

## 把文末的 Licences 全部删掉

这个声明似乎是关于不可转载或者原创性的，看着很吵，我不在乎。没找到能取消的地方，所以我做得相当决绝，把语言文件`\i18n\zh-cn.yaml`（记得要复制到根目录中）里的相关信息全给删了，但还是留下一对角框，在`\layouts\partials\post\license.html`把它毁尸灭迹。

这个语言文件夹给本话唠提供很多聊天机会，做了很多修改。

## 首页公告（？）

> 2022-05-22 Update

主题作者直接在新的版本里面加了这个样式，现在可以在`assets/README.md`里更改了……噗 XD

<details>
<summary>
内容过时
</summary>

没有评论区那就加个首页公告（？）好了，评论区可以没有，喜剧效果要先拉起来。（为什么要记录这个，因为感觉就算评论区弄好了这个公告也很好玩，使得大家一点进来先不得不听我聊 50 字屁话，记下来方便屁话修改）。

在`\layouts\index.html`加入：

```
   <span>{{ T "post.archiveCounter" (len (where site.RegularPages "Type" "in" (slice "posts" "status"))) | safeHTML }} </span>
   </div>
    👋嗨！发现了吧！本小鸟换了一个新主题！那么呢，由于种种人家无法解决的评论区加载问题<br>所以现在的评论区——
     <br>是假的！！😱😱<br>
     噗哈哈哈哈哈！所以！我们现在只能这么沟通啦——
     当当当！！请点击：<font color="#dd6065"><a class="link" href="https://gregueria.channel.io/lounge" target="_blank" rel="noopener">💘聊天小气泡</a></font>！！！
     <br>找人家聊天吧！！等等，万一气泡也打不开呢？<br>
     你有人家的电话号码的，对吧？<br><br>
     <div>
```

</details>

## Waline 评论区配置

这一部分的改动是跑去给作者留了个 Issue 后作者提供的，主题更新了之后我发现跑更新的命令行也没法直接更新好主题，干脆重新把主题拉取了下来……嗯这个主题真的让我爆破了很多次施工现场 XD，更新之后发现之前加载迟缓的问题也突然解决了。很奇怪，感觉是我自己之前干了什么不对的事。

总之关于评论区配置，先在`layouts/partials/comment.html`中写入：

```
<div class="border-t py-6 px-6 md:px-8 dark:border-darkBorder">
    <div id="waline"></div>

    <script data-swup-reload-script>
        setTimeout(() => {
            console.log(document.getElementById('waline'))
            window.waline = Waline.init({
                el: '#waline',
                serverURL: '',
                emoji: [],
                requiredMeta: ['name', 'email', 'url'],
            });
        }, 1000);
    </script>
</div>
```

填好 serverURL 和表情链接，之后去这里`layouts/partials/custom/head.html`写入：

```
<script src="https://unpkg.com/@waline/client@v2/dist/waline.js"></script>
<link rel="stylesheet" href="https://unpkg.com/@waline/client@v2/dist/waline.css"/>
```

### Dark Mode

其实改得不好，我只是把背景设成了透明，文字颜色并没有改好。留个坑啦。

### 表情包大小

> TOT 本地预览成功修改，但 Push 上去并没有改到。一个难以捉摸的主题！

Blob 表情当然要大一点！`assets\sass\custom.scss`里写：

```
body {
    .wl-content .vemoji, .wl-content .wl-emoji {
        display: inline-block;
        vertical-align: baseline;
        height: 2.35em; //表情包大小
        margin: -0.125em 0.25em;
    }
}

```

## 首页卡片

### 卡片中的 Summary 变量改为 Description

这个改动说起来很奇怪。Luna 主题的首页卡片上显示的是 Summary 作为摘要，如果没有 Summary 则显示你文章的前 70 个字，而我所有的文章都是用 Description 来作为文章的摘要，于是迁移到这个主题之后之前写过的摘要都不作数了，全都显示前 70 个字，把文章 Summary 全部改成 Description 也不是不行，但是很麻烦很笨啦！所以直接去改这一部分`layouts\partials\post-card.html`的第 93 行和 98 行，将`{{- with $Summary -}}`改成`{{ with .Params.description }}`：

```
<div class="sm:hidden block px-5 border-t dark:border-darkBorder pt-5">
<a href="{{- .RelPermalink -}}" class="font-bold line-clamp-2 md:line-clamp-3 text-2xl">{{- .Title -}}</a>
      {{ with .Params.description }}<div class="line-clamp-2 mt-4 mb-1" title="{{- . -}} ">{{ . }} <span class=" text-gray-400"></span></div>{{- end -}}
</div>
{{- else -}}
   <a href="{{- .RelPermalink -}}" class="block px-5 dark:border-darkBorder pt-5">
      <div class="font-bold line-clamp-2 md:line-clamp-3 text-2xl group-hover:text-theme">{{- .Title -}}</div>
      {{ with .Params.description }}<div class="line-clamp-2 mt-4 mb-1" title="{{- . -}} ">{{ . }} <span class=" text-gray-400"></span></div>{{- end -}}
   </a>
```

还有，我把“...”全删了。我的世界不能有这样的点点点。

### 阅读时间改为字数统计

作者更新后的主题支持在 Config.toml 中开关字数统计和阅读时间，但不知道为什么我关掉之后还是会在首页卡片中显示出来，只好一关再关（？）

在`\layouts\partials\post-card.html`修改：

```
<div class="hidden items-center mr-4 sm:flex">
    <i class="eva eva-book-open-outline mr-1"></i>
    <span class="mr-1">{{- T "post.wordCount" .WordCount}}</span> <!--readingTime改为wordCount-->
</div>
```

### 文章题图

有题图的文章文件名似乎只能是`index.md`，然后要在 Front-matter 上写`featured_image: 图片.jpg`，然后把文章和`图片.jpg`放在同一个文件夹里才能生效。其他时候都会优雅地……报错。

## 遇事不决，版本回退！

换了这个 Theme 之后我差不多把博客爆破了四五次吧。有几次是没有必要的，手忙脚乱之中干脆删除了仓库。其实版本回退就好了：

```
git reset --hard 目标版本号(在仓库Commit里查询)
git push -f
```

> 参考：[Git 恢复之前版本的两种方法](https://blog.csdn.net/yxlshk/article/details/79944535)

## 页尾运行时间

`layouts\partials\components\run-time.html`中删掉：

```
    <b id="run-time-h">0</b>
    <span class="text-xs"> {{ T "runTime.hours" }} </span>
    <b id="run-time-m">0</b>
    <span class="text-xs"> {{ T "runTime.minutes" }} </span>
    <b id="run-time-s">0</b>
    <span class="text-xs"> {{ T "runTime.seconds" }}</span>
```

秒针跳动焦虑去除，成功！

然后去`i18n\zh-cn.yaml`加上一个可爱的 Emoji：

```
runTime:
    text: "🕓 Run Time: "
    days: "Days"
```

平静并且加倍可爱，成功！
