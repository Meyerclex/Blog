---
title: "Docsify | 花哨文具码在案前，用不用另说"
description: "目前为止，我都喜爱它。"
date: "2022-07-07"
slug: "Doclog"
image: ""
categories:
    - 为沙滩插上太阳伞
tags:
    - Docsify
toc: true
hidden: true 
---

总而言之，某日逛到一个Docsify笔记库，简洁干净又漂亮，看了一下教程似乎并不难，我对自己的[前笔记库](https://teetotaler.vercel.app/)不满很久（因为没有办法检索），于是摸鱼事件着手折腾Docsify，竟然成了（竟然成了）。

## 参考资料

1. [Docsify的配置+全插件列表](https://xhhdd.cc/archives/80/comment-page-1)
2. [Docsify的配置中文文档](https://docsify.js.org/#/zh-cn/)
3. [Docsify | 搭建个人静态笔记库](https://mantyke.icu/posts/2021/docsify-build/)

## 主题修改

配置是网上搜了一个随便复制下来用了（竟然成了），主要使用到的插件：字数统计、全文搜索、翻页、页面右侧TOC。

参考了塔塔的教程中[CSS的修改办法](https://mantyke.icu/posts/2021/docsify-build/#%E6%9C%AC%E5%9C%B0%E5%BC%95%E7%94%A8css)。

参照了教程修改了字体，还将默认的引用样式修改成了我喜欢的样子：

```
.markdown-section blockquote {
 background: rgba(235, 236, 237, 0.3);
 border-left: 5px solid currentcolor;
 border-radius: 5px;
 margin: 0.5rem 0;
 padding: 0.1em 1em;
 font-size: 1em;
 display: block;
 margin-block-start: 1em;
 margin-block-end: 2em;
 margin-inline-end: 40px;
}
```

## 注意事项

Docsify的侧边栏功能是由插件实现的，并且并不是自动生成的，你需要添加了一个Markdown文件后，在`_sidebar.md`文件中列出这个文档的名字和路径，例如`[受戒](Books\受戒.md)`，之后这个文件才会被读到侧边栏中。

在文档很多的情况下，手动录入变得非常麻烦。最终我用[Auto Sidebar For Docsify](https://gitee.com/vaguelycloud/auto-sidebar-for-docsify)解决了这个问题！

## 铛啷！

[Welcome to 鱼’s Repository！](https://note.gregueria.icu/)

最近到了晚上约莫十点前后，眼皮就开始打架，今天振作起来打开文档，以超快速度并超不详细地写一篇超短的更新（我意识到这几个月我每次写博客都大动干戈企图翻出最内在的情绪宣泄，然后导致一些长篇累牍连篇废话，这不是一个正常的状态，对我这等超强表演欲的精神暴露狂来讲凡是超过3000字都是危险的，所以我决定最近的计划是缩短更新间隔，删减更新篇幅，所以我这次写了这个没有感情色彩的折腾笔记。靠，可我甚至都不是一个正常人，我哪来的正常的状态？像个大疯狗一样站在网页中央刨水坑就是我的一个天然自然正常的形态）。这个笔记库是上周建的，其实只是个一成放读书笔记、九成放小说摘抄的整理库，整理起来倒也很快：一键导出电子书划线部分，SNS的俏皮话复制粘贴一下，调整格式，放进Markdown文档里，丢进Docsify，上传，即成。Docsify的好处在于它没有Front-matter之类的东西，完美实现所见即所得。目前为止，我都喜爱它。