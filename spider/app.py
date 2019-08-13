import requests  # urllib urllib3
from bs4 import BeautifulSoup # re  lxml(xpath)
import json
import time
import random


spider_lzl=open("JD_spider.txt",'w+')

#建立一个user-Agent池防屏蔽
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ']
#随机生成一个headers
user_agent = random.choice(user_agents)
headers = {"User-Agent": user_agent,  "Referer": "https://item.jd.com/12353915.html"}
#书籍计数器
count_book=0
#设置搜索链接页面url\n",
for book_page in range(1,100,2):
    url_json="https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=Python&page={0}&s=54&click=0".format(book_page)
    html=requests.get(url_json,headers=headers).content
    soup = BeautifulSoup(html,'html.parser')
    soup_allli = soup.find_all('li',class_="gl-item")
    for soup_li in soup_allli:
        #评论计数
        count_comment=1
        #获取书名
        soup_name=soup_li.find('div',class_="p-name")
        #获取书的价格
        soup_price=soup_li.find('div',class_="p-price")
        #获取书的作者姓名
        soup_author=soup_li.find('span',class_="p-bi-name")
        #获取书店名称
        soup_store=soup_li.find('span',class_="p-bi-store")
        #获取出版日期
        soup_date=soup_li.find('span',class_="p-bi-date")
        #获取书的产品号
        ProductID=soup_li.find('div',class_="p-commit").strong.a['href'].lstrip('https://item.jd.com/').rstrip('.html#comment')
        ProductID=int(ProductID.strip())
        #获取书的详细页网址\n",
        comment_url='https://item.jd.com/'+str(ProductID)+'.html'
        ######################
        #获取评论
        # commemt_detail='评论详情:\n'
        # #生成0-9页的随机数，防止被京东屏蔽
        ran_num=random.sample(range(10), 10)
        for page in ran_num:
            # time.sleep(10)
            url_json = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv486&productId='+str(ProductID)+'&score=0&sortType=5&page='+str(page)+'&pageSize=10&isShadowSku=0&fold=1'
            user_agent = random.choice(user_agents)
            headers = {"User-Agent": user_agent,  "Referer": "https://item.jd.com/12353915.html"}
            html = requests.get(url_json,headers= headers).text
            try:
                data=json.loads(html[25:-2])
            except:
                break
            commitsum=data['productCommentSummary']['commentCountStr']
            # print(data)
        #     for i in range(0,10):
        #         commemt_detail=commemt_detail+"评论"+str(count_comment)+':'+data['comments'][i]['content']+'\n'
        #         count_comment=count_comment+1
        count_book=count_book+1
        ######################输出到控制台
        print("书籍：",count_book)
        print("产品号：",ProductID)
        print("书名：",soup_name.get_text())
        print("价格：",soup_price.get_text())
        try:
            print("作者：",soup_author.get_text().rstrip('著'))
        except:
            print("作者：","作者未知")
        try:
            print("书店：",soup_store.get_text())
        except:
            print("书店：","书店未知")
        try:
            print("出版日期：",soup_date.get_text())
        except:
            print("出版日期：","出版日期未知")
        # print("书籍详细页网址：",comment_url)
        print("评论总数：",commitsum)
        # print(commemt_detail)
        print("……"*30)
        #######################重新同时输出到文件
        print("书籍：",count_book,file=spider_lzl)
        print("产品号：",ProductID,file=spider_lzl)
        print("书名：",soup_name.get_text(),file=spider_lzl)
        print("价格：",soup_price.get_text(),file=spider_lzl)
        try:
            print("作者：",soup_author.get_text().rstrip('著'),file=spider_lzl)
        except:
            print("作者：","作者未知",file=spider_lzl)
        try:
            print("书店：",soup_store.get_text(),file=spider_lzl)
        except:
            print("书店：","书店未知",file=spider_lzl)
        try:
            print("出版日期：",soup_date.get_text(),file=spider_lzl)
        except:
            print("出版日期：","出版日期未知",file=spider_lzl)
        print("书籍详细页网址：",comment_url,file=spider_lzl)
        print("评论总数：",commitsum,file=spider_lzl)
        # print(commemt_detail,file=spider_lzl)
        print("……"*30,file=spider_lzl)
        ################################\n",
        #够500本书就跳出循环\n",
        if count_book >=5000:
            break
    #够500本书就跳出循环
    if count_book >=5000:
        break
spider_lzl.close()
