# JD-Python-book-Analysis

> 2022.03.01 注
> 
> 陆陆续续发现有十多个同学给我点了 star，这让我很惊喜，因为以现在的技术眼光来看，这个小 Demo 属实是很简单了
> 
> 为了方便查看我把可访问的地址更新了 -> [戳我](https://lanzhi-lee.github.io/JD-Python-book-Analysis/index.html)
> 
> 如果有其他的疑问我能帮到你，欢迎邮件联系我

项目是大三下学期企业工程实践课的答辩项目，采集了京东 python 类图书的大约 1500 条数据

~~项目基于 koa 进行搭建，使用 echarts 进行数据可视化，使用 pm2 进行线上部署~~

现在改为直接使用 GitHub=Pages 进行静态部署

### 目录结构

```
├── README.md                       // 本文档
├── app.js                          // 【已废弃】服务程序主入口文件
├── data                            // 对数据进行预处理的函数
│   └── data.js
├── index.html                      // 主页面文件
├── package.json
├── spider                          // 爬虫抓取的静态数据
│   ├── JD_spider.json
│   ├── JD_spider.txt
│   ├── app.py
│   └── index.js
├── static                          // 静态资源文件
│   ├── css
│   │   ├── normalize.css
│   │   └── zzsc-demo.css
│   └── js
│       ├── jquery-2.1.1.min.js
│       ├── main.js
│       ├── naiveScroll.js
│       └── naiveScroll.min.js
└── test                            // 尝试使用词云，最终因为时间放弃了
    └── testJieba.js
```

### 最终效果

![1565711779052](https://baibai-mine.oss-cn-shanghai.aliyuncs.com/1565711779052.png)

![1565711825572](https://baibai-mine.oss-cn-shanghai.aliyuncs.com/1565711825572.png)

![1565711847695](https://baibai-mine.oss-cn-shanghai.aliyuncs.com/1565711847695.png)

### 线上地址

如果比较幸运，服务器没有挂掉，~~线上地址为：http://122.152.236.186:3000/~~

可访问地址更新为 https://lanzhi-lee.github.io/JD-Python-book-Analysis/index.html

### 过后总结

这个小项目并不难，工作量也不大，从确定目标到最终实现不过两天时间，其中也有不少不完善的地方。不过还好，麻雀虽小，五脏俱全——前端 jQuery+echarts，后端 koa，该有的都有了

最大的收获是，经过这些东西，让自己的知识结构更完善了，发现了一些以往觉得 JavaScript 不能做的但实际上能做的东西
