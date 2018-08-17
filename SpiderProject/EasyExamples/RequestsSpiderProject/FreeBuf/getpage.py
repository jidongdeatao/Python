

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
