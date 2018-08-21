保存数据到数据库（关系型数据库），这里有两种方式：
  一、同步
  二、异步
  
  使用异步保存的好处：
  在爬虫爬取的Item速度大于item保存到数据库中速度时，同步方式会造成堵塞，而异步就是为了解决堵塞
  
同步方式，代码：

class MysqlPipeline(object):
    # 采用同步的机制写入mysql
    def __init__(self):
        self.conn = MySQLdb.connect(
            '127.0.0.1',
            'root',
            'tp158917',
            'articlespider',
            charset="utf8",
            use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole_article(title, url, create_date, fav_nums)
            VALUES (%s, %s, %s, %s)
        """
        # 使用VALUES实现传值
        self.cursor.execute(insert_sql,(item["title"],item["url"],item["create_date"],item["fav_nums"]))
        self.conn.commit()
