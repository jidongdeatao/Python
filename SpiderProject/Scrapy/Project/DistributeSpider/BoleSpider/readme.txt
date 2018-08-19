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

        #Xpath的用法
        front_image_url = response.meta.get("front_image_url", "")
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first("")
        create_date = response.xpath('//div[@class="entry-meta"]/p/text()').extract()[0].strip().replace("·","").strip()
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        content = response.xpath('//div[@class="entry"]').extract()[0]
        praise_nums = response.xpath('//div[@class="post-adds"]/span/h10/text()').extract()[0]
        fav_nums = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0].strip()
        match_re = re.match(".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0
        comment_nums = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0].strip()
        match_re = re.match(".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = int(match_re.group(1))
        else:
            comment_nums = 0

        # 为实例化后的对象填充值
        article_item['front_image_url'] = [front_image_url]
        article_item["url"] = response.url
        article_item["url_object_id"] = get_md5(response.url)
        article_item['title'] = title
        try:
            create_date = datetime.datetime.strptime(create_date, "%Y/%m/%d").date()
        except Exception as e:
            create_date = datetime.datetime.now().date()
        article_item['tags'] = tags
        article_item['content'] = content
        article_item['praise_nums'] = praise_nums
        article_item['fav_nums'] = fav_nums
        article_item['comment_nums'] = comment_nums

        yield article_item
    
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
     
     
