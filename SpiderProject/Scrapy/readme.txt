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
