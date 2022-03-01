const Koa = require('koa')
const app = new Koa()
const fs = require('fs')

const serve = require('koa-static')
app.use(
  serve(__dirname + '/', {
    extensions: ['html'],
  })
)

app.use(async (ctx, next) => {
  if (ctx.request.path === '/data') {
    ctx.response.type = 'json'
    ctx.response.body = fs.readFileSync('./spider/JD_spider.json')
  } else {
    await next()
  }
})

// 在端口3000监听:
app.listen(3000)
console.log('app started at port 3000...')
