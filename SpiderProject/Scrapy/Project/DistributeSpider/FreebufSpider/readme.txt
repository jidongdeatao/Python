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
 

5.由于元素有部分数据需要进一步处理，这里需要在items.py文件的LagouJobItem对象前加入处理函数：
      def remove_splash(value):
          #去掉工作城市的斜线
          return value.replace("/","")

    然后在对象中引用：
    class LagouJobItem(scrapy.Item):
        job_city = scrapy.Field(
            input_processor = MapCompose(remove_splash)
        )
        
        
6.在pipelines.py中定义了保存数据库的模版，
  class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    ......
    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)
        
        
7.在items.py文件中的LagouJobItem()对象下加入与数据库建立连接并执行的语句：
     def get_insert_sql(self):
        insert_sql = """
            insert into lagou_job(title, url, url_object_id, salary, job_city, work_years, degree_need,
            job_type, publish_time, job_advantage, job_describe, job_addr, company_name, company_url,
            tags, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_describe=VALUES(job_describe)
        """
        params = (
            self["title"], self["url"], self["url_object_id"], self["salary"], self["job_city"],
            self["work_years"], self["degree_need"], self["job_type"],
            self["publish_time"], self["job_advantage"], self["job_describe"],
            self["job_addr"], self["company_name"], self["company_url"],
            self["tags"], self["crawl_time"].strftime(SQL_DATETIME_FORMAT),
        )

        return insert_sql, params
