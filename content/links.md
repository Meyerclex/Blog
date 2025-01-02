---
title: 小鱼和她的朋友们
description:
date: 2021-06-28
toc: false
---

<script>
document.addEventListener("DOMContentLoaded", function() {
    // 获取带有 post-content 类的文章内容
    var articleContent = document.querySelector(".post-content");

    // 获取文章内容内部的所有列表项
    var items = articleContent.querySelectorAll("ul li");

    // 将列表项转换为数组
    var itemsArray = Array.from(items);

    // 随机排列数组中的元素
    for (var i = itemsArray.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = itemsArray[i].innerHTML;
        itemsArray[i].innerHTML = itemsArray[j].innerHTML;
        itemsArray[j].innerHTML = temp;
    }

    // 获取每隔6个项后的分割线
    for (var i = 5; i < itemsArray.length; i += 6) {
        var hr = document.createElement("hr");
        itemsArray[i].parentNode.insertBefore(hr, itemsArray[i].nextSibling);
    }
});
</script>

> {{< emoji name="blobcatflower" ext="">}}基于自己的认识对也在写博客的朋友们写了自己简单的了解，如果我冒冒失失搞错了任何地方欢迎联系我修改！
> 
> 每一次刷新，排列顺序都会被打乱。

---

- [Missing](https://www.missingid.online/)：重新点亮域名的年更选手宝宝！！

- [Mengru](https://mengru.space/)：她的空间很棒，爱看周记栏目！

- [Muko](https://oaad.iceco.icu/)：很有活力的Kpop选手，不管学习记录还是旅行记录都很好看。

- [Plaskier](https://blog.plaskier.icu/)：芋阿圆，非常严谨文字书写风格。

- [Shixiaocaia](https://shixiaocaia.fun)：是小蔡，CS相关选手，非常积极地学习与生活。

- [suica](https://suicablog.cobaltkiss.blue)：有许多服务搭建的分享，与读书游玩体验笔记。召唤Suica！

- [Zoeash](https://writee.org/zoeash/)：诗歌与虚构，诚实的自我观察。

- [咖啡冰河](https://blog.mysto.cyou)：Kraka的美丽博客，她也书写着小说。

- [晴空](https://www.summeringway.icu/)：一个是安静的地方，存放夏夏的看过和走过的地方。

- [小球飞鱼](https://mantyke.icu/)：是塔塔，无论是按节气更新的生活日志还是经验教程类文章都非常好看！

- [超新星电台](https://supernovaradio.live/)：远游的云，在名为自己的迷宫里东张西望。

- [蝴蝶曾在此处](https://write.c7.io/tyou/)：小猫的博客，不是在打球就是在打球的路上！非常有活力的书写。

- [A Purrception](https://tortie.me/)：尾巴摆摆，一只美丽玳瑁小猫的姐姐。她在阅读和绘画，很好看的热情的分享！

- [天仙子](https://tianxianzi.me/)：繁茂的文字森林，正在记录与分享着自己生命的旅程。

- [白天](https://luoshui.icu/)：小狗充满激情的脚印！在书籍与现实世界中高速地冲浪。

- [山茶花舍](https://irithys.com/)：是吕楪喔。非常好读可爱的文字风格。关于她的生活与经验。

- [深海鱼拒绝触礁](https://trails-of-isara.vercel.app/)：鲨鲨！我们海底世界朋友（？是坦诚自由的书写。

- [东俄勒冈群山](https://houdini.eu.org/)：小迪独特的书写，字里行间藏满像风一样的思绪。

- [昼河万里](https://tothemoonriver.icu/)：是小河。她在学习，观察自己，去着不同的地方。她的沉思与旅行都值得阅读。

- [山月](https://sanguok.com/)：长期的博客写作者，书写了非常多丰富的主题。沉静的文字风格。

- [呆呆不是槑](http://graugris.icu/)：是呆呆！一位认真地书写着自己的生活与学习经验的Kpop选手。

- [甜鱼/Ayu](https://ayu.land)：多面手甜鱼，她在画画和做音乐与游戏，像万花筒一样的博客！

- [圆面包如何逃离狐口](https://sunnkynews.icu/)：是盐，在骑车，并分享着她生活里不同的风景。

- [冷酷蹦迪](https://www.hezicola.com/)：帅气而冷酷的设计，非常好玩的书写，一个很行的博客。

- [Χαρυβδις](https://kharybdism.xyz/)：是M君！博客存放着她的同人与文章翻译，帅气的同人女友友。

- [天堂错误文件](https://naturaleki.one/)：是小爱，我首页的游戏实况博主（？

- [眠于水月间](https://sleepymoon.cyou)：是鹤辞！像夜空一般的博客，有一个美丽的展柜，正在分享着她的珍藏。

- [Velas电波站](https://www.velasx.com)：一些生活的自我记录与游戏的分享，她也在写小说。

- [夜航南飞](https://banshou-air.netlify.app/)：一条充满未知的航线，与一位跑团的高手。伊在认真的对待自己的人生。

- [让黑夜划满星](https://www.rouroupuppy.top/)：秋田犬酱！！恋哥高手（小声）你好，你的cp很好也借我嗑一口……

- [珊瑚阁 GoldMaple](https://goldmaple.info/)：是世界公民小金，正在写着关于驻西非的生活。她正在用特别而珍贵的视角，坦率地记录着自己的人生。

- [Kawa1Planet](https://kawa1planet.fun/)：今年做了非常多漂亮本本封面的友友！（而我似乎即将拥有其所作封面的两本🤲

- [Shadows of the Sun](https://rovingsun.wordpress.com/)：很好的、优美的写作，与一个火热的真心，来自新朋友Rovingsun。你也会喜欢她的。

- [一支咏叹调](https://turquoise.one/)：是蜉蝣（的小豆泥乐园！）今年是钩针织物艺术家！

- [一片痴心俱成灰](https://akaito.xyz/)：是女祭，一位神秘长情狡兔多窟的参展达人同人女。

---

喜欢大家，爱看大家，通过RSS猛猛地订阅了大家{{< emoji name="meow_blush" ext="">}}

## 要和我交换吗？

> 链接：https://gregueria.icu/
> 
> 名称：谢谢所有的鱼
> 
> 简介（如需）：您首页的奶牛猫图片转发大使

很珍惜博客这样的连结，因而暂时不希望是单向链接。 虽然新主题暂时没办法打开友链评论区，但仍然欢迎和我说过话/有毛毛象联系方式的朋友交换链接，Guest Book和毛象联系都OK！

{{< emoji name="cats" ext="">}}希望您也是对人和小动物都富有同理心的友善之人！
