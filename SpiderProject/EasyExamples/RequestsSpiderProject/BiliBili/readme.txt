
bilibili-users-info.py
  爬取Bilibili用户信息的程序
  主要是使用了三个接口
  一个是POST接口：
    https://space.bilibili.com/ajax/member/GetInfo
    这个接口请求payload是mid=521403
                      csrf
    这个接口可以返回json数据，以下为举例
        status	true
        data	{…}
        mid	521403
        name	长萌丶
        sex	男
        rank	10000
        face	http://i0.hdslb.com/bfs/face/948a165781961992330d12752e6a82258281098c.jpg
        regtime	1348972688
        spacesta	0
        birthday	06-10
        sign	玄不救非
        level_info	{…}
        current_level	3
        official_verify	{…}
        type	-1
        desc	
        suffix	
        vip	{…}
        vipType	0
        vipStatus	0
        toutu	bfs/space/768cc4fd97618cf589d23c2711a1d1a729f42235.png
        toutuId	1
        theme	default
        theme_preview	
        coins	0
        im9_sign	0c0470979bdad40769ffae4cfea7fa7f
        fans_badge	false

  另外两个GET请求接口；
    https://api.bilibili.com/x/relation/stat?vmid=
    https://api.bilibili.com/x/space/upstat?mid=
    
  还有很多特殊的用户信息可以爬取到，只要认真的分析任意一个获取用户信息的URL：https://space.bilibili.com/521403/#/
  然后建立与数据库的连接，把抓取到的这些数据可以存储到数据库中：
  在本地建立个bilibili的数据库，在其中创建个表bilibili_user_info
  bilibili_user_info.sql
  其中的字段为：
DROP TABLE IF EXISTS `bilibili_user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bilibili_user_info` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mid` int(20) unsigned NOT NULL,
  `name` varchar(45) NOT NULL,
  `sex` varchar(45) NOT NULL,
  `rank` varchar(45) NOT NULL,
  `face` varchar(200) NOT NULL,
  `regtime` varchar(45) NOT NULL,
  `spacesta` varchar(45) NOT NULL,
  `birthday` varchar(45) NOT NULL,
  `sign` varchar(300) NOT NULL,
  `level` varchar(45) NOT NULL,
  `OfficialVerifyType` varchar(45) NOT NULL,
  `OfficialVerifyDesc` varchar(100) NOT NULL,
  `vipType` varchar(45) NOT NULL,
  `vipStatus` varchar(45) NOT NULL,
  `toutu` varchar(200) NOT NULL,
  `toutuId` int(20) unsigned NOT NULL,
  `coins` int(20) unsigned NOT NULL,
  `following` int(20) unsigned NOT NULL,
  `fans` int(20) unsigned NOT NULL,
  `archiveview` int(20) unsigned NOT NULL,
  `article` int(20) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
LOCK TABLES `bilibili_user_info` WRITE;
/*!40000 ALTER TABLE `bilibili_user_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `bilibili_user_info` ENABLE KEYS */;
UNLOCK TABLES;
  
  
 这个主要是分析了这个爬虫，没有多大难度， 
https://github.com/airingursb/bilibili-user  
 bilibili-users-info.py 需要使用到USE-AGENT头文件（避免被反爬虫到），已放到项目中。
  
