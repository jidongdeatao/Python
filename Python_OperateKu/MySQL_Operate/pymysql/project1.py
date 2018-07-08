#银行转账实例
#来自于慕课网免费课程 《python操作MySQL》 https://www.imooc.com/learn/475

import pymysql
#import sys 这个模块不知道怎么用的就不用敲了
class TransferMoney(object):
    def __init__(self,conn):
        self.conn = conn

    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = """select * from account where acctid=%s"""%acctid
            cursor.execute(sql)
            print("check_acct_availabale:"+sql)
            rs=cursor.fetchall()
            if len(rs) !=1:
                raise Exception("账号%s不存在"%acctid)
        finally:
            cursor.close()

    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = """select * from account where acctid=%s and money>%s"""%(acctid,money)
            cursor.execute(sql)
            print("has_enough_money:"+sql)
            rs=cursor.fetchall()
            if len(rs) !=1:
                raise Exception("账号%s没有足够的钱"%acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = """update account set money=money-%s where acctid=%s """%(money,acctid)
            cursor.execute(sql)
            print("reduce_money:"+sql)
            if cursor.rowcount !=1:
                raise Exception("账号%s减款失败"%acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = """update account set money=money+%s where acctid=%s """%(money,acctid)
            cursor.execute(sql)
            print("add_money:"+sql)
            if cursor.rowcount !=1:
                raise Exception("账号%s加款失败"%acctid)
        finally:
            cursor.close()

    def transfer(self,source_acctid,target_acctid,money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

if __name__=='__main__':
    source_acctid = 11 #sys.argv[1] 
    target_acctid = 12 #sys.argv[2]
    money = 100 #sys.argv[3]

    conn = pymysql.connect(host='127.0.0.1',port=3306,
                       user='root',password='',
                       db='imooc',charset='utf8')
    tr_money = TransferMoney(conn)
    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print("出现问题："+str(e))
    finally:
        conn.close()
        
        
#解释一下，上图代码作用就是把账号11中的钱向账号12中转移100.而能不能具体实现主要依赖之前我们建立imooc数据库中account表中数据是否符合：
#1.账号能否对得上
#2.账号11中有没有大于100的金额
#如果上面两条如果有不符合的情况，系统就会报错
