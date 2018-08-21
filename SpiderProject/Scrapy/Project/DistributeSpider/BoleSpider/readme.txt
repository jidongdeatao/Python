Scrapy爬取伯乐在线

标准开始命令：
    scrapy startproject ArticleSpider
    cd ArticleSpider
    scrapy genspider jobbole blog.jobbole.com

在主目录ArticleSpider下创建个main.py文件，里面内容：（作用用于debug)
  # _*_ coding: utf-8 _*_

  from scrapy.cmdline import execute
  import sys
  import os
  sys.path.append(os.path.dirname(os.path.abspath(__file__)))
  execute(["scrapy","crawl","jobbole"])
  

在spiders下的jobbole.py文件中，针对parse、parse_detail两个函数进行处理：
    其中：
     parse函数是用于获得要爬取的多个页面的url，以及建立不间断的循环
     parse_detail函数是用于针对要爬取的单个页面中的元素进行解析，定义要获取页面中的哪些元素。另外要在这个函数下要把定义的元素传递给Item进行实例化，
          方便每爬取一个页面就把页面元素通过Item传递到pipeline中进行存储或数据处理
     这两个函数有多种获取页面元素的方式，Xpath、Css Selector、item loader，其中item loader是Scrapy自带的一种方法更加灵活，
          使用Scrapy最好首先选择这种方式，前两种是比较通用的方式
     这两个函数详情如下：
     def parse(self, response):
        #Xpath的用法
        post_nodes = response.xpath('//div[@class="post floated-thumb"]/div[@class="post-thumb"]/a')
        for post_node in post_nodes:
            post_url = post_node.xpath('@href').extract()[0]
            img_url = post_node.xpath('img/@src').extract()[0]
            yield Request(url=parse.urljoin(response.url,post_url),meta={"front_image_url":img_url},callback=self.parse_details)
        next_url = response.xpath('//div[@class="navigation margin-20"]/a[@class="next page-numbers"]/@href').extract()[0]
        if next_url:
            yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse)
     
     def parse_details(self, response):
        #实例化
        article_item = JobBoleArticleItem()

        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图

        # 通过item loader加载item
        item_loader = ArticleItemLoader(item=JobBoleArticleItem(), response=response)

        # 通过css选择器将后面的指定规则进行解析。
        item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("front_image_url", [front_image_url])
        item_loader.add_css("praise_nums", ".vote-post-up h10::text")
        item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
        item_loader.add_css("fav_nums", ".bookmark-btn::text")
        item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("content", "div.entry")

        # 调用这个方法来对规则进行解析生成item对象
        article_item = item_loader.load_item()

        # 已经填充好了值调用yield传输至pipeline
        yield article_item
        
        #这里使用了scrapy提供的最简便的itemLoader用法，其他如Xpath用法、CSS选择器用法，见Xpath与CSS选择器用法
    
在items.py文件中元素要与jobbole.py文件中parse_details函数中定义的元素一致
class JobBoleArticleItem(scrapy.Item):
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    title = scrapy.Field()
    create_data = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    praise_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
    这种方法有了改进，增加了更多的形式，详见item.py文件中处理item process.py
    
 
 在pipeline.py文件中定义数据存储到数据库、或保存到本地的方法：
 
 
 别忘了在settings.py文件中加入相关配置。
 
     
     
