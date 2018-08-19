打造分布式Scapy爬虫

一、
选取目标网站：伯乐在线
标准开始命令：
    scrapy startproject ArticleSpider
    cd ArticleSpider
    scrapy genspider jobbole blog.jobbole.com
详情见：BoleSpider
在主目录
  # _*_ coding: utf-8 _*_

  from scrapy.cmdline import execute
  import sys
  import os
  sys.path.append(os.path.dirname(os.path.abspath(__file__)))
  execute(["scrapy","crawl","jobbole"])
