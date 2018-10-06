
## python简单操作mysql
- 数据库的连接和简单获取数据改进之捕获异常
      '''python
      #encoding:utf-8
      import MySQLdb
      #捕获异常
      #获取连接
      try:
          conn = MySQLdb.connect(
              host = '127.0.0.1x',
              user = 'root',
              password = '',
              db = 'news',
              port = 3306,
              charset = 'utf8'
          )

          # 获取数据
          cursor = conn.cursor()
          cursor.execute('select * from news order by created_at desc')
          rest = cursor.fetchone()
          print(rest)

          # 关闭连接
          conn.close()
      except MySQLdb.Error as e:
          print('mysql error:%s' % e)
      '''
