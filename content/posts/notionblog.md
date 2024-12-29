+++
categories = ["为沙滩插上太阳伞"]
date = 2022-01-11T16:00:00Z
description = "尝了一口Node.js后我忽然想起了一个未竟的事业。"
slug = "nodejs-notablog"
tags = ["Blog", "Notion"]
title = "Blog | 互联网乱序试吃后，敲起之前中道崩殂的Notablog"
textIndent = true
hidden = true 
+++
> 在我敲完这篇的四天后（_2022年1月16日_）我忽然瞧见了另一个博客，TA也写了如何自己的搭建流程，我想TA的方案显然比我的更简洁也更好，虽然我想不到有谁会认真参考我的博客内容，但还是一并贴来：[Making a Github blog from Notion pages](https://janakymurthy.github.io/making_blog_from_notion_pages.html)
> 
> 2022年4月7日 Update：增加了一个简陋的更新方法。

这段时间有一搭没一搭地学[FreeCodeCamp](chinese.freecodecamp.org)，CSS学到一半的路上被最后的项目困住，苦恼了几秒之后我开始试吃别的课程，在互联网乱序游荡，点开了Node.js的课，一步一步跟着先下载各种安装包，在`Install`按下没多久忽然发现——

咦。我本来就有Node.js环境？

大概是过去哪一回互联网试吃失败遗留下来的东西吧，实在不知道什么时候我试图挑战过这个了。但我完全不知道这个怎么用，这在FCC也是很后面的课程，而我Javascript都还只试吃了小半口，跟着敲了一下查看版本的代码都不是很顺利，于是去找了一个手把手的教程：[Node.js全套入门教程](https://www.bilibili.com/video/BV1a34y167AZ?p=5)，它的分集目录很明确完整，非常有利于精准试吃，于是我这才终于明白：原来你想在哪里敲代码，就应该在目录那里打开终端——这样的表述也不知道对不对，总之就是按一下路径然后敲`cmd`回车。嗯！我会了！这就完成了第一步！

试吃到这里我忽然想起来Node.js这个东西我在哪里见过：[沙滩会是鱼的最后一站吗？](https://gregueria.vercel.app/posts/%E6%B2%99%E6%BB%A9%E4%BC%9A%E6%98%AF%E9%B1%BC%E7%9A%84%E6%9C%80%E5%90%8E%E4%B8%80%E7%AB%99%E5%90%97/)

> 📌**前情回顾**
>
> [Notablog](https://github.com/dragonman225/notablog)：界面美丽。但Getting Start里的“Make sure you have Node.js v12.0.0 or higher”使我未能开始。

……原来在这儿呢。现在我已经有了Node.js v12.0.0 or higher啦😝虽然用Notion搭东西的愿望已经没有那么强烈了，但既然我都学到这里了（刚学完`npm`怎么用的地步）那我就一定要试试！Let's get started！

## Let's get started!

接下来的活动也没有那么激动，就是按照Notablog的文档一步步敲下来就好啦（这一步我直接在磁盘路径下的`cmd`敲的）：`npm i -g notablog`

然后在新建的`notablog-starter`文件夹里的`cmd`中继续敲：`git clone https://github.com/dragonman225/notablog-starter.git`

然后像其他用Notion搭的博客一样，去把[作者提供的模板](https://www.notion.so/b6fcf809ca5047b89f423948dce013a0?v=03ddc4d6130a47f8b68e74c9d0061de2)Duplicate回自己的Notion里，然后把它设为公开，接着把自己那串网址复制下来，把`notablog-starter`文件夹中的`config-json`里的`url`值替换成自己的。

然后在`notablog-starter`目录里敲命令行：`notablog generate .`——很快你的Notion中的内容就被拉下来形成了一个网站，存放在了`notablog-starter/public/`里。而之后每一次在Notion上做了调整更新，都可以用这个命令行读取并划拉下来。

根据我稀薄的Html知识大概明白了网站就在这个public文件夹里了，作者是这么说的：

> open index.html with a browser to preview your site.

嗯，对`index.html`右键用浏览器打开，确实是那个漂亮样子！Congratulations！等一下，可是这样不行呀！😫我不能让它放在硬盘里孤芳自赏对不对？根据作者的建议：

> You can copy files in notablog-starter/public/ directory to a server or upload them to any static hosting service to share your content with the world.
>
> Some options for static hosting services:
>
> **Github Pages**、Netlify、surge.sh

## 把它们上传到Github！

我们可以把这个`Public`文件夹用类似Github Pages之类的托管服务弄到互联网世界里——Netlify好像也挺常见的，但我没有用过，只有第一个是我认识的，因为之前读过很多用Github Pages搭建博客的文章，看了一下文档和视频大概明白了怎么处理它，嗯！动手吧！（胡扯，人家在这里卡了一个多小时唉😫）

> 💨**参考文献**
>
> 1. [如何把本地文件夹上传到github](https://blog.csdn.net/littlely_ll/article/details/80054481)：谢谢你互联网老师，我总算知道怎么弄这个啦！
> 2. [零基础-通过Github Pages搭建个人博客](https://www.bilibili.com/video/BV1Xh411b7wh?p=3&share_source=copy_web)：这个Po有讲关于Github的Master和Main分支，虽然我没有搞懂，但我总算知道了自己建完仓库以后的那些指令是做什么的。
> 3. [Github Pages](https://pages.github.com/)

🧐那就开始吧！

1. 先在Github上建一个新仓库，根据上面第二份和第三份文献，可以知道仓库名需要是`Username.github.io`，这里应该必须是自己的用户名作为前缀，其他就先不管啦。关于SSH之类的知识，我没有专门再设置。鉴于我之前搭博客设置过类似的东西，这里应该不需要……吧？把仓库地址复制下来。
2. 接下来在`notablog-starter\public`中右键用`git bash here`，按照第二份文献（视频）中做的那样敲：`git init`
3. 用`git add .`把文件都添加上去。
4. `git commit -m "注释"`
5. 将仓库关联到github：`git remote add origin https://xxxx，https`为刚才github上创建仓库的地址。
6. 把文件推送到github仓库：`git push -u origin master`，下次推送时，可以把-u去掉。

之后就可以在`Your Username.github.io`中看到自己的网页，这是我的：[鱼’s Notebook](https://teetotaler.vercel.app/)。至于为什么这里的地址后缀是*vercel.app*，因为人家不喜欢自己的Github用户名嘛😫！然后就用Vercel把那个仓库划拉下来，换一下域名，总之两个地址都可以到同一个地方，同一个门有两个门牌号的意思。

弄完这个玩具之后很开心，其实后续的更新很麻烦啦。在Notion上更新完网页之后，要在`notablog-starter`目录里敲命令行：`notablog generate .`，接着又得跑去`public`把上面的Step3、4、6重复一遍才算完毕。

虽然很麻烦……但人家学到了新东西还用上了很开心嘛😝今天的修太阳伞活动到此结束！关于后续我的这个可爱小网页要怎么用？打算用来做成书影游待办List和常用网页书签，因为Notion的这一部分很漂亮嘛。

## 我想要更优美的更新方式！

### 2022-01-16 Update

上面谈到更新很麻烦嘛，于是互联网游历途中我看到了一些别的方案。关于怎么更简单地更新页面，作者其实给出了这个解决方案：[Trigger Webhook from Notion](https://github.com/dragonman225/trigger-webhook-from-notiony)

以及在这个博客，同样给出了TA的办法：[Making a Github blog from Notion pages](https://janakymurthy.github.io/making_blog_from_notion_pages.html)并且TA也详尽地写了怎么样把自己的博客推到Github Pages上，TA的更新流程显然更短也更方便，相比之下我写的真是凌乱不堪，很是惭愧。

不过我的互联网试吃活动一直是有一搭没一搭的，所以目前只是看到了，并没有用上。这里只是存一下档，或许将来某天心血来潮了会开始试试^^

### 2022-04-07 Update

改用了另一种简陋但方便一点点的更新方法。在根目录文件夹`notablog-starter\`新建一个`generate.bat`，里面写一行：`notablog generate .`，之后双击可以直接完成拉去。

在`notablog-starter\public`中新建`git.bat`，里面写入：

```
git add .
git commit -m "commit_msg"
git push origin master

pause
```

虽然上面那个博客也给出了类似的更新方法但是对方写的那个`Workflow.sh`我运行一直失败，就只好自己摸摸看了……很简陋吧！我连在`.bat`文件中如何更改运行目录的命令行都不会写所以只好分成两个文件运行，以后Notion更新完之后按顺序戳两下`generate.bat`和`git.bat`就可以更新好了（很简陋呢但终于不用自己手敲了（没错我手动敲了一个月的命令才开始像笨仓鼠找更优路径一样找新的办法（逃
