拉钩网爬虫

$ scrapy genspider --list
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed
默认使用basic模版，这次选取crawl 这个模版

中间有任何需要调试的地方都可以debug main.py
# _*_ coding: utf-8 _*_

from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","lagou"])

1.使用命令
  scrapy genspider -t crawl lagou www.lagou.com
  创建lagou模版
  对于crawl这个模版，通过源码阅读剖析
  https://doc.scrapy.org/en/1.3/topics/spiders.html#crawlspider
      提供了一些可以让我们进行简单的follow的规则，link，迭代爬取
  这里需要设置rules规则，方便在深度爬取哪些url
  rules = (
    Rule(LinkExtractor(allow=("zhaopin/.*",)), follow=True),
    Rule(LinkExtractor(allow=("gongsi/j\d+.html",)), follow=True),
    Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
  )
    
2.观察页面，选取要爬取哪些元素，设计数据库

3.在items.py文件中定义LagouJobItem对象
  class LagouJobItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    。。。

4.从要爬取的详细页面中提取共同元素到parse_detail函数中，并且使用itemLoad方法
    这里可以使用scrapy shell url
    response.css进行调试
    需要注意 网站做了限制爬虫，所以需要加上user-agent
    scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36" url

    items.py文件中自定义itemloader，parse_detail函数中需要加载
    # 自定义itemloader实现默认取第一个值
    class LagouJobItemLoader(ItemLoader):
        default_output_processor = TakeFirst()

    def parse_details(self, response):
        # 实例化
        lagou_item = LagouJobItem()

        # 通过item loader加载自定义的itemLoader
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        # 通过css选择器将后面的指定规则进行解析。
        item_loader.add_css("title",".name::text")
        。。，
        # 调用这个方法来对规则进行解析生成item对象
        lagou_item = item_loader.load_item()
        # 已经填充好了值调用yield传输至pipeline
        yield lagou_item
  

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

    @classmethod
    # 自定义组件或扩展很有用的方法: 这个方法名字固定, 是会被scrapy调用的。
    # 这里传入的cls是指当前的MysqlTwistedPipline class
    def from_settings(cls, settings):
        # setting值可以当做字典来取值
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        # 连接池ConnectionPool
        # def __init__(self, dbapiName, *connargs, **connkw):
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        # 此处相当于实例化pipeline, 要在init中接收。
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行：参数1：我们自定义一个函数,里面可以写我们的插入逻辑
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 添加自己的处理异常的函数
        query.addErrback(self.handle_error, item, spider)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print (failure)
        
        
