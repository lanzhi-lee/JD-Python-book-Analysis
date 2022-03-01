function getSpiderData(callback) {
  $.ajax({
    // url: 'http://localhost:3000/data',
    url: './spider/JD_spider.json',
    async: false,
    success: (res) => typeof callback === 'function' && callback(res),
  })
}

function countTimes(souceArr) {
  return souceArr.reduce(function (allNames, name) {
    if (name in allNames) allNames[name]++
    else allNames[name] = 1
    return allNames
  }, {})
}

getSpiderData((res) => {
  // 初步取出json中的数据
  let authorTemp = []
  let commentTemp = []
  let priceTemp = []
  let publisherTemp = []

  let price_commentTemp = []

  for (let item of res) {
    // 出版社显示出版社名及出现次数
    publisherTemp.push(item.publisher)
    // 作者显示作者名及次数
    authorTemp.push(item.author.trim())
    // 价格显示价格及次数
    priceTemp.push(Math.ceil(+item.price))
    // 热度显示书名及评论数
    commentTemp.push({
      name: item.name,
      commentNum: item.commentNum,
    })

    if (item.price > 5 && item.price < 180) {
      price_commentTemp.push([Math.ceil(+item.price), item.commentNum, item.commentNum, item.name])
    }
  }
  window.authorData = countTimes(authorTemp)
  window.commentData = commentTemp
  window.priceData = countTimes(priceTemp.sort((a, b) => a - b))
  window.publisherData = countTimes(publisherTemp)

  window.price_commentData = price_commentTemp
})
