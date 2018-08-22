拉钩网爬虫

$ scrapy genspider --list
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed
默认使用basic模版，这次选取crawl 这个模版

1.使用命令
  scrapy genspider -t crawl lagou www.lagou.com
  创建lagou模版
  对于crawl这个模版，通过源码阅读剖析
  https://doc.scrapy.org/en/1.3/topics/spiders.html#crawlspider
      提供了一些可以让我们进行简单的follow的规则，link，迭代爬取
2.观察页面，选取要爬取哪些元素，设计数据库

3.在items.py文件中定义LagouJobItem对象

4.从要爬取的详细页面中提取共同元素到parse_detail函数中，并且使用itemLoad方法
    这里可以使用scrapy shell url
    response.css进行调试
    需要注意 网站做了限制爬虫，所以需要加上user-agent
    scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36" url
