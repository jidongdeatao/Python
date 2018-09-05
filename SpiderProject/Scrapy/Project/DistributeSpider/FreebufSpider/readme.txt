爬取FreeBuf.com文章
不能直接取到网页数据
选择使用Selenium+webdriver进行爬取,selenium不再支持PhantomJS 这里注意


1.使用命令
  scrapy genspider -t crawl freebuf www.freebuf.com
    
2.观察页面，选取要爬取哪些元素，设计数据库,由于网站使用了JavaScript限制了访问请求（即使用scrapy -shell 抓取url 抓取到的只是JavaScript），
  所以这里

  spider/freebuf.py 文件如下：
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from ArticleSpider.items import FreebufItem
from ArticleSpider.items import FreebufItemLoader
from ArticleSpider.utils.common import get_md5

from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from selenium.webdriver.firefox.options import Options
import re
class FreebufSpider(CrawlSpider):
    name = 'freebuf'
    allowed_domains = ['www.freebuf.com']
    start_urls = ['http://www.freebuf.com/']

    def __init__(self):
        options = Options()
        options.add_argument('-headless')  # 无头参数
        options.add_argument('--disable-gpu')
        self.browser = webdriver.Firefox(firefox_options=options)

        super(FreebufSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        #当爬虫退出的时候关闭chrome
        print ("spider closed")
        self.browser.quit()

    rules = (
        Rule(LinkExtractor(allow=("author/.*",)), follow=True),
        Rule(LinkExtractor(allow=("zhuanlan/.*",)), follow=True),
        Rule(LinkExtractor(allow=r'articles/web/\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'articles/system/\d+.html'), callback='parse_item', follow=True),

    )
    def parse_item(self, response):
        # 实例化
        freebuf_item = FreebufItem()

        # 通过item loader加载自定义的itemLoader
        item_loader = FreebufItemLoader(item=FreebufItem(), response=response)
        # 通过css选择器将后面的指定规则进行解析。
        item_loader.add_css("title", ".articlecontent .title h2::text")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("author", ".property .name a::text")
        item_loader.add_css("create_date", ".property .time::text")
        item_loader.add_css("watch_nums", ".property .look strong::text")
        item_loader.add_css("tags", ".property .tags a::text")
        item_loader.add_xpath("content", "//div[@id='contenttxt']")
        item_loader.add_value("crawl_time", datetime.now())

        # 调用这个方法来对规则进行解析生成item对象
        freebuf_item = item_loader.load_item()
        # 已经填充好了值调用yield传输至pipeline
        yield freebuf_item

3.在items.py文件中定义Item对象
  class FreebufItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    。。。
4.pipelines依然适用和爬取其他网站的一样都使用MysqlTwistedPipeline

5.middlewares.py加入使用selenium的命令
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from scrapy.http import HtmlResponse
class JSPageMiddleware(object):

    #通过Firfox请求动态网页
    def process_request(self, request, spider):
        if spider.name == "freebuf":
            # browser = webdriver.Firefox()
            spider.browser.get(request.url)
            import time
            time.sleep(3)
            print ("访问:{0}".format(request.url))

            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8", request=request)

 6.settings.py文件中设置上面的引用
 DOWNLOADER_MIDDLEWARES = {
   'ArticleSpider.middlewares.JSPageMiddleware': 1,
   'ArticleSpider.middlewares.RandomUserAgentMiddlware': 2,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}
 

        
        

