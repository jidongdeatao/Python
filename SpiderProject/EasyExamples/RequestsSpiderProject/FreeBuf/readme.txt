FreeBuf
喜欢的一个网络安全的科普类网站

选取它作为爬虫对象

首先选取的是专栏作家
这里涉及几个接口
    3.
        http://zhuanlan.freebuf.com/index/columRec/?tag=0&first=1&search=
        这个接口为get请求，请求多次后会返回数据库不同的专栏信息
        请求后返回的json格式为：
        status	200
        data    【	
            0	
            id	"106"
            columName	"潜心学习的小白帽"
            imgUrl	"http://image.3001.net/images/20170920/15058369361454.jpg!video"
            url	"/column/index/?name=潜心学习的小白帽"
            intro	"漏洞复现，代码审计，工具介绍，CTF总结。"
            attenMount	"9646"
            artiMount	"76"
            attenflag	"关注"
            】
    2.
    http://zhuanlan.freebuf.com/column/articleSelectHome/?name=%E5%88%A9%E5%99%A8%E7%99%BE%E5%AE%9D%E7%AE%B1
    http://zhuanlan.freebuf.com/column/articleSelectHome/?page=3&name=%E5%88%A9%E5%99%A8%E7%99%BE%E5%AE%9D%E7%AE%B1
    这两个URL为同一个接口，对于分页的话在page处发生变更
        请求后返回的json字段有以下部分
        status	200
        data	「
          totalPage	9
          list {
            0	{
              id	163208
              title	StaCoAn：一款能够在移动应用上执行静态代码分析的跨平台工具
              url	www.freebuf.com/column/163208.html
              imgUrl	http://image.3001.net/images/20180223/15193774453923.png!240.160
              content	StaCoAn是一款跨平台工具，它可以帮助开发人员、漏洞猎人以及白帽黑客对移动端应用程序进行静态代码分析。
              author	Alpha_h4ck
              authorImg	http://image.3001.net/2016/08/11.png
              authorUrl	www.freebuf.com/author/Alpha_h4ck
              time	174天前
              comMount	0
              readCount	690044
              money	0
              }
             }
             」
        从这个返回值就可以提取出想要的信息
        
        现在还差一个可以遍历所有专栏作家的URL接口
        
           
SQL语句：
zhuanlan表需要使用的语句：

DROP TABLE IF EXISTS `zhuanlan`;
CREATE TABLE `zhuanlan` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mid` int(20) unsigned NOT NULL,
  `columName` varchar(45) NOT NULL,
  `imgUrl` varchar(100) NOT NULL,
  `url` varchar(45) NOT NULL,
  `intro` varchar(200) NOT NULL,
  `attenMount` int(10) NOT NULL,
  `artiMount` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

content表需要使用到的语句：

DROP TABLE IF EXISTS `content`;
CREATE TABLE `content` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `page_id` varchar(10)  NOT NULL,
  `title` varchar(100) NOT NULL,
	`page_url` varchar(100) NOT NULL,
  `imgUrl` varchar(200) NOT NULL,
	`contents` varchar(200) NOT NULL,
	`author` varchar(50) NOT NULL,
  `authorImg` varchar(200) NOT NULL,
	`authorUrl` varchar(200) NOT NULL,
  `deploytime` varchar(50) NOT NULL,
	`comMount` varchar(10) NOT NULL,
  `readCount` varchar(10) NOT NULL,
	`money` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
