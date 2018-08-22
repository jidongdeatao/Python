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
