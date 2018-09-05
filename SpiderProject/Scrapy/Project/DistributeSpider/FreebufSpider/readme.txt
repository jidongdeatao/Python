爬取FreeBuf.com文章
不能直接取到网页数据
选择使用Selenium+Phantomjs进行爬取


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
