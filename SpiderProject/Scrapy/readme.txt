爬虫Scrapy框架


Scapy的组件包括：
1. Scrapy Engine：处理系统数据流和事务的引擎。
2. Scheduler 和 Scheduler Middlewares：调度引擎发过来的请求。
3. Downloader 和 Downloader Middlewares：下载网页内容的下载器。
4. Spider ：爬虫系统，处理域名解析规则及网页解析。

Scrapy的基本用法包括下面几个步骤：
1. 新建 Scrapy 项目
2. 实现 Item，用来存储提取信息的容器类
3. 实现 Spider，用来爬取数据的爬虫类
4. 从 HTML 页面中提取数据到 Item
5. 实现 Item Pipeline 来保存 Item 数据
当一个新的 Scrapy 项目创建后将会自动生成代码结构，只需要按照上述步骤把指定的文件进行自定义就可以实现爬虫功能。

Scrapy项目的目录结构：
  创建一个爬虫项目名称叫onespider
  使用命令：scrapy startproject onespider 创建Scrapy项目：
  目录结构为：
  onespider
  |-scrapy.cfg
  |-onespider
    |-__init__.py
    |-items.py
    |-pipelines.py
    |-setting.py
    |-spiders
      |-__init__.py
  
  这些文件分别是:
* scrapy.cfg: 项目的配置文件。
* onepider/: 该项目的python模块。之后将在此加入代码。
* onespider/items.py: 为爬虫项目的数据容器文件，主要用来定义我们要获取的数据。
* onespider/pipelines.py: 爬虫项目的管道文件，主要用来对items里面定义的数据进行进一步的加工和处理。
* onespider/settings.py: 项目的设置文件。
* onespider/spiders/: 放置spider代码的目录。
