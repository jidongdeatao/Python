#coding:utf-8
import redis
# 基础操作:验证redis是否可操作

# redis.Redis()兼容老版本，redis.StrictRedis()不考虑兼容性
r = redis.Redis(host='localhost', port=6379, db=0)
# r = redis.StrictRedis(host = 'localhost', port=6379, db=0)
r.set('user1','choupi')
user1 = r.get('user1')
print(user1)


