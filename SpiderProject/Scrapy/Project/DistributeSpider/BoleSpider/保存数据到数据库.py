# 保存数据到数据库（关系型数据库），这里有两种方式：
#   一、同步
#   二、异步
  
#   使用异步保存的好处：
#   在爬虫爬取的Item速度大于item保存到数据库中速度时，同步方式会造成堵塞，而异步就是为了解决堵塞
  
# 同步方式，代码：
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
        
# 同时需要在settings.py中引入这种方式
ITEM_PIPELINES = {
   'ArticleSpider.pipelines.MysqlPipeline': 1,
}



# 异步方式，代码：

import MySQLdb
import MySQLdb.cursors
# 异步操作mysql插入
class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    # 自定义组件或扩展很有用的方法: 这个方法名字固定, 是会被scrapy调用的。
    # 这里传入的cls是指当前的MysqlTwistedPipline class
    def from_settings(cls, settings):
        # setting值可以当做字典来取值
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        # 连接池ConnectionPool
        # def __init__(self, dbapiName, *connargs, **connkw):
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        # 此处相当于实例化pipeline, 要在init中接收。
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行：参数1：我们自定义一个函数,里面可以写我们的插入逻辑
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 添加自己的处理异常的函数
        query.addErrback(self.handle_error, item, spider)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print (failure)
        
 # 同时需要在settings.py中引入这种方式
ITEM_PIPELINES = {
   'ArticleSpider.pipelines.MysqlTwistedPipeline': 1,
}

# setting值可以当做字典来取值，settings.py文件中需要设置下mysql的基本信息
# mysql基本信息
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "articlespider"
MYSQL_USER = "root"
MYSQL_PASSWORD = "123212"
