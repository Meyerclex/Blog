---
title: 💎站点更新日志 Changelog
description:
date: 2021-06-28
slug: changelog
toc: true
---

## TODO

- [x] 适配移动端（只能说微微适配啦…）
- [x] 修改夜晚主题配色
- [ ] 增加图片点击放大
- [ ] 修改鼠标指针
- [ ] 修改表格之类的基础样式问题
- [ ] 增加一个喜报通知条幅（这什么东西？）

## 2024/12/03

新增了Cafe页面，用的是[Status Cafe]()挂件。

参考了这个教程：[Creating a Feed Reader from StatusCafe
](https://bechnokid.neocities.org/resources/tut_statuscafefeed)

## 2024/11/23

博客大装修了一番。

> **Resource Credit**
> 
> - 图标来源[Pixel Safari](https://pixelsafari.neocities.org/favicon/)
> 
> - 页面设计来源[aeon flexx](https://codepen.io/aeon-flexx-dead-girl/pen/RwXmbdQ)

## 装修笔记索引

> [1. 鱼鱼小家的装修笔记](/posts/archiveandlink/)
>
> [2. Stack 主题及 Waline 评论区装修笔记](/posts/decoration/)
>
> [3. Luna 主题装修笔记](/posts/hugo-luna/)


## 2022-12-17

主题更换为[Gruvbox](https://github.com/schnerring/hugo-theme-gruvbox)，因为懒所以没有配置右下角的提问箱也没有写装修笔记（喂），主要改动有：

1. 将目录修改为默认显示
2. 配置了 Waline 评论区并修改了配色
3. 为文章配置了中文字数显示，增加页脚统计
4. 成功把评论区的表情给改大了。不知为何在 CSS 文件里写样式，本地预览生效但推上去却不显示，所以最终是在`layouts\partials\comments.html`里加了`<style>`标签写样式来解决的这个问题

因为不太理解 Git 分支到底怎么更新，我现在驯服这个主题的方式把主题仓库拉下来，更新文章后敲`hugo`生成新的`public`文件夹，建一个 Public 仓库，把`public`文件夹的内容复制过来，更新仓库，把这个仓库作为站点仓库，而非像过去那样把主题仓库作为站点仓库。

## 2022-09-14

文章页面打开时实在过分卡顿，排查原因，查到[一篇文章](https://segmentfault.com/a/1190000002970056)谈到是背景图片显示方式`background-attachment: fixed;`导致的，一口气注释掉。

原文提供的优化方法试了几次都会导致字重显示有误（怀疑是`::before`的原因），最终也没有找到能够让图片不滚动的方法，图片滚动好像又会导致渲染不及时所以下滑时有短暂的大闪白光效果（）？，所以加了一行`will-change: auto;`应付一下就算完事了，谁知道起不起效果，不管你了！

不知道为什么表情变得奇大无比，于是修改了评论区表情的大小和显示方式，现在悬停在它们身上可以获得放大效果，超可爱。感谢[咖啡冰河的文章](https://blog.mysto.cyou/posts/211028-blognewtheme/)：

```
    img.wl-emoji,
    img.vemoji {
        width: 38px;
        vertical-align: sub;
        transition: ease-out .6s;
    }

    img.wl-emoji:hover,
    img.vemoji:hover {
        transform: scale(1.75);
    }
```

## 2022-09-10

由于 Luna 实在难以驾驭，所以换回了又快又好用的 Stack 主题噗哈哈哈 XD！对主题一番装修，人家的 CSS 知识还没法照顾到移动端的适配，希望不要出太大差错。

### 关于版权

1. 感谢又快又好用的[Stack](https://github.com/CaiJimmy/hugo-theme-stack)主题
2. 感谢 Home 页的九十年代小猫咪：[It's Neko!](https://webneko.net/?white)
3. 如果你也想要一个站点标题图片：[textanim](https://textanim.com/)
4. 背景与页脚图片（一个美丽的站点）：[cinni.net](https://cinni.net/web.html#blinkies)

## 2022-08-30

取消了 Channel.io 聊天气泡.

## 2022-07-24

根据芋阿圆的笔记增加了文章段首空两格的 Feature.

## 2022-05-24

终于把消失很久的聊天小气泡加上，虽然没有人找我聊天啦 💬

## 2022-05-22

终于把页脚的心头大患 Run Time 给改了实现了所有想要的 Feature 了，小鸟立誓再也不会打开装修页面了 😤VS code 也卸载了（假的），再见！

## 2022-05-19

经过爆破艰难地更新了船新版本的 Luna，获取了浮动 Toc 并立誓再也不更新主题了

## 2022-05-05

站点主题从 Stack 更换为 Luna

## 2021-11-14

小鸟拥有了自己的第一个私人博客
