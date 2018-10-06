# python操作MongoDB数据库
## MongoDB介绍- [详情](https://github.com/jidongdeatao/Database/tree/master/MongoDB)
### pymongo
- 安装
pip install pymongo
- 文档
  * https://github.com/mongodb/mongo-python-driver
- 示例
  * 连接本地数据库方式
    ```python
      方式1：简写
      > from pymongo import MongoClient
      > client = MongoClient()
     方式2：指定端口和地址
      > client2 = MongoClient('localhost', 27017)
      方式3：使用URI
      > client3 = MongoClient('mongodb://localhost:27017/')
      ```
  * 详见：[ mongodb_operate.py](https://github.com/jidongdeatao/Python/blob/master/Python_OperateKu/MongoDB_Operate/mongodb_operate.py)
## MongoDB ODM

### mongoengine
- 安装
pip install mongoengine
- 文档
  * http://mongoengine-odm.readthedocs.io/guide/ 
- 示例
  * 连接本地数据库方式
  ```python
  方式1：简写
  connect('students')
  >>> from mongoengine import connect
  >>> connect('students')
  MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
  方式2：指定端口和地址
  connect('students',host='192.168.3.96',port=27017)
  方式3：使用URI
  connect('students',host='mongodb://localhost/students')
  ```
  * 详见： [mongodb_engine_operate.py](https://github.com/jidongdeatao/Python/blob/master/Python_OperateKu/MongoDB_Operate/mongodb_engine_operate.py)
