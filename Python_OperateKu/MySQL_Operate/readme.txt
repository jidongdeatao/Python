
Python DB API介绍：
  Python访问数据库（包括MySQL、Oracle、SQLserver）接口的统一接口规范
Python DB API包含内容：
  1.connection 数据库连接对象
  2.cursor 数据库交互对象
  3.exceptions 数据库异常类

使用Python DB API访问数据库流程：
  开始 -> 创建connection -> 获取cursor -> 执行查询、执行命令、获取数据、处理数据-> 关闭cursor ->关闭connection ->结束
  
python2中操作MySQL使用的MySQLDB这个库
python3中操作MySQL使用的pymysql这个库

  
访问数据库流程示例（使用pymsql模块)：
一、创建connection连接对象
      首先创建connection连接对象：建立Python客户端与数据库的网络连接
      创建方法：MySQLdb.Connect(参数）
        参数有host,port，user,password，db，charset 其类型除了port是数字，其他都是字符型
        含义分别是MySQL服务器地址，端口，用户，密码，数据库名称，连接编码
      这一部分执行代码：
            import pymysql
            conn = pymysql.connect(host='127.0.0.1',port=3306,
                                   user='root',password='',
                                   db='imooc',charset='utf8')
            cursor=conn.cursor()
            print(cursor)
            print(conn)
            cursor.close()
            conn.close()
      通过Pycharm输出结果：
      <pymysql.cursors.Cursor object at 0x00BF9250>
      <pymysql.connections.Connection object at 0x00BFE0D0>
      可以看到已经与数据库建立连接
      
      connection对象支持的方法有：
      cursor() 使用该连接创建并返回游标
      commit() 提交当前事务
      rollback() 回滚当前事务
      close() 关闭连接
      
 二、获取cursor
    cursor游标对象： 用于执行查询和获取结果
    cursor对象支持的方法：
        execure(op[,args])  执行一个数据库查询和命令
        fetchone()          取的结果集的下一行
        fetchmany(size)     获取结果集的下几行
        fetchall()          获取结果集中剩下的所有行
        rowcount            最近一次excute返回数据的行数或影响行数
        close()             关闭游标对象
     这一部分执行代码需要在刚才基础上添加：
        import pymysql
        conn = pymysql.connect(host='127.0.0.1',port=3306,
                       user='root',password='',
                       db='imooc',charset='utf8')
        cursor=conn.cursor()
        #增加sql语句。 #新建名为user的表
        sql = """CREATE TABLE users(
        userid INT(11) NOT NULL AUTO_INCREMENT,
        username VARCHAR(100) DEFAULT NULL,
        PRIMARY KEY(userid)
        )ENGINE=INNODB CHARSET=utf8 COLLATE=utf8_general_ci"""
        cursor.execute(sql)
        #插入数据(插入9条数据）
        sql = """INSERT INTO users VALUES(1,'name1');
        INSERT INTO users VALUES(2,'name2');
        INSERT INTO users VALUES(3,'name3');
        INSERT INTO users VALUES(4,'name4');
        INSERT INTO users VALUES(5,'name6');
        INSERT INTO users VALUES(6,'name6');
        INSERT INTO users VALUES(7,'name7');
        INSERT INTO users VALUES(8,'name8');
        INSERT INTO users VALUES(9,'name9');
        """
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        """
        这里注意下：
        对数据库的操作基本上都是将数据库的命令写到sql变量中然后放到execute方法中，可以不用每条execute后面都紧接着使#commit方法提交，但直到提交完成，这些操作才会在数据库中生效：也就是说，比如你在前面先创建了一个表并exectute，虽然没有提交到数据库，但只要execute，后面的操作会认为你的动作已经完成，最后一次commit就会全部生效.sql语句要放在try.except语句中，如果sql有错误的话，.rollback()会避免错误的产生

        以上的插入还可以写成另外一种形式：
        sql = """INSERT INTO users(userid,username) VALUES('%d','%s')%(1,'name1')
        ...."""
        """
        #查询已插入的数据
        sql = """select * from user"""
        cursor.execute(sql)
        print(cursor.rowcount)#可以打印获取到的数据行数
        rs=cursor.fetchone()
        print(rs) #获取此时游标后的1行数据
        rs=cursor.fetchmany(3)
        print(rs) #获取此时游标后的3行数据
        rs=cursor.fetchall()
        print(rs) #获取此时游标后的所有数据
        cursor.close()
        conn.close()
        """
        此时的输出结果为：
        9
        (1, 'name1')
        ((2, 'name2'), (3, 'name3'), (4, 'name4'))
        ((5, 'name6'), (6, 'name6'), (7, 'name7'), (8, 'name8'), (9, 'name9'))
        以上结果说明，每次执行fetch都是在上次fetch执行的结果后执行的
        """

        如果想要打印所有的数据，并按我们想要的格式输出，代码如下：
        sql = """select * from user"""
        cursor.execute(sql)
        rs=cursor.fetchall()
        for row in rs:
            print("userid=%d,username=%s"%row)
        输出结果为：
        userid=1,username=name1
        userid=2,username=name2
        userid=3,username=name3
        userid=4,username=name4
        userid=5,username=name6
        userid=6,username=name6
        userid=7,username=name7
        userid=8,username=name8
        userid=9,username=name9

以上操作完整的流程：
开始 -> 创建connection -> 获取cursor -> 使用cursor.execute()执行i/u/d语句 -> 出现异常？ （否）-> 使用conn.commit()提交事务------
                                                                            |（是）                                    |  
                                                                            |-----------> 使用conn.rollback()回滚事务---|  
                                                                                                                      |
                                                                                       结束 <--关闭connection  <--关闭cursor
                                                                                       
 

慕课网相关免费入门视频：
《python操作MySQL数据库》 https://www.imooc.com/learn/475
