# JD-Python-book-Analysis

项目是大三下学期企业工程实践课的答辩项目，采集了京东python类图书的大约1500条数据

项目基于koa进行搭建，使用echarts进行数据可视化，使用pm2进行线上部署

### 目录结构

data --- 对数据进行预处理的函数

spider --- 爬虫抓取的静态数据

static --- 静态资源文件

test --- 尝试使用词云，最终因为时间放弃了

app.js --- 服务程序主入口文件

index.html --- 主页面文件

### 最终效果

![1565711779052](https://baibai-mine.oss-cn-shanghai.aliyuncs.com/1565711779052.png)

![1565711825572](https://baibai-mine.oss-cn-shanghai.aliyuncs.com/1565711825572.png)

![1565711847695](https://baibai-mine.oss-cn-shanghai.aliyuncs.com/1565711847695.png)

### 线上地址

如果比较幸运，服务器没有挂掉，线上地址为：http://122.152.236.186:3000/

### 过后总结

这个小项目并不难，工作量也不大，从确定目标到最终实现不过两天时间，其中也有不少不完善的地方。不过还好，麻雀虽小，五脏俱全——前端jQuery+echarts，后端koa，该有的都有了

最大的收获是，经过这些东西，让自己的知识结构更完善了，发现了一些以往觉得JavaScript不能做的但实际上能做的东西