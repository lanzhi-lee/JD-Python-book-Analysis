const fs = require('fs')

function getCommentNum(str) {
    str = str.replace('+', '')
    if (str[str.length - 1] === "万") return (+str.replace('万', '')) * 10000
    else return +str
}

let str = fs.readFileSync('./JD_spider.txt').toString()
let arr = str.split('………………………………………………………………………………………………………………………………………………………………')
arr.pop()

// let count = 0
let targetArr = []
let tempObj = {}
for (let item of arr) {
    // console.log(count++)
    temp = item.trim().split('\r\n')

    temp.splice(1, 3)
    temp.splice(2, 4)
    temp.splice(6, 1)
    // console.log(temp)

    // 索引
    tempObj.index = temp[0].split('： ')[1]
    // 书名
    tempObj.name = temp[1]
    // 价格
    tempObj.price = +temp[2].replace('￥', '')
    // 作者
    tempObj.author = temp[3].split('： ')[1]
    // 出版社
    tempObj.publisher = temp[4].split('： ')[1]
    // 出版时间
    tempObj.publishTime = temp[5].split('： ')[1]
    // 评论数
    tempObj.commentNum = getCommentNum(temp[6].split('： ')[1])

    console.log(tempObj)
    targetArr.push(tempObj)
    tempObj = {}
}

fs.writeFileSync('./JD_spider.json',JSON.stringify(targetArr))