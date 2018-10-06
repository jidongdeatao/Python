#coding:utf-8
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId


class MongoTest(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['blog']

    def add_one(self):
        '''添加单条数据'''
        
        # 造数据
        # for i in range(3):
        #     post = {
        #         'title':"人民代表大会提出将提高个税起征点"+str(i),
        #         'content':"非常好的建议，有利于民生"+str(i),
        #         'x':i,
        #         'create_at': datetime.now()
        #     }
        #     self.db.blog.posts.insert_one(post)

        # 添加单条数据
        post = {
            'title':"人民代表大会提出将提高个税起征点",
            'content':"非常好的建议，有利于民生",
            'x':18,
            'create_at': datetime.now()
        }
        return self.db.blog.posts.insert_one(post)

    def get_one(self):
        '''获取单条数据'''
        return self.db.blog.posts.find_one()

    def get_more(self):
        '''获取多条数据'''
        return self.db.blog.posts.find()

    def get_one_from_oid(self,oid):
        '''查询指定ID的数据'''
        obj = ObjectId(oid)
        return self.db.blog.posts.find_one({'_id':obj})

    def update(self):
        ''' 修改数据 '''

        # 将x为1的文档改为x+3
        # res = self.db.blog.posts.update_one({'x':1},{'$inc':{'x':3}})
        # print(res.matched_count)

        # 将所有的值都增加20
        return self.db.blog.posts.update_many({}, {'$inc':{'x':20}})

    def delete(self):
        '''删除数据'''

        # 删除x为1的1条数据
        # res = self.db.blog.posts.delete_one({'x':0})
        # print(res.deleted_count)

        # 删除x为1的多条数据
        res = self.db.blog.posts.delete_many({'x':1})
        print(res.deleted_count)

def main():
    mon = MongoTest()
    res = mon.add_one()
    # print(res.inserted_id)

    # res = mon.get_one()
    # print(res['title'])

    # res = mon.get_more()
    # for i in res:
    #     print(i['title'])

    # res =obj.get_one_from_oid('59522222dfd')
    # print(res)

    # res = mon.update()
    # print(res.matched_count)

    mon.delete()
    

if __name__ == "__main__":
    main()
