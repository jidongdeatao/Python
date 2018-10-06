#encoding:utf-8
import MySQLdb

class MysqlConnection(object):

    # 初始化
    def __init__(self, host = '127.0.0.1', port = 3306, user = 'root', password = '', db = 'news',charset='utf8'):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._db = db
        self._charset = charset
        self._conn = None
        self._cursor = None
        self.get_conn()

    # 关闭数据库连接
    def close(self):
        if self._cursor:
            self._cursor.close()
            self._cursor = None

        if self._conn:
            self._conn.close()
            self._conn = None

    def commit(self):
        self._conn.commit()

    # 获取数据库连接
    def get_conn(self):
        try:
            self._conn = MySQLdb.connect(
                host = self._host,
                user = self._user,
                password = self._password,
                db = self._db,
                port = self._port,
                charset = self._charset
            )

            self._cursor = self._conn.cursor()
        except MySQLdb.Error as e:
            print('mysql error:%s' % e)


    # 获取单条新闻
    def get_one(self):

        sql = 'select * from news where types = %s order by created_at desc'
        # 获取数据
        self._cursor.execute(sql,('百家',))
        rest = dict(zip([k[0] for k in self._cursor.description], self._cursor.fetchone()))

        # 关闭连接
        self.close()
        return rest

    # 获取多条新闻
    def get_more(self):

        sql = 'select * from news where types = %s order by created_at desc'
        # 获取数据
        self._cursor.execute(sql,('百家',))
        rest = [dict(zip([k[0] for k in self._cursor.description], row)) 
        for row in self._cursor.fetchall()]

        # 关闭连接
        self.close()
        return rest

    def add_one(self):
        sql = 'insert into news(title,image,content,types,is_valid) values(%s, %s, %s, %s, %s)'
        self._cursor.execute(sql, ('标题1','/static/img/news/01.png', '新闻内容1','推荐',1))
        self.commit()
        self.close()

def main():
    obj = MysqlConnection()
    # rst = obj.get_more()
    # rst = obj.get_one()
    # print(rst)
    obj.add_one()

if __name__ == "__main__":
    main()
