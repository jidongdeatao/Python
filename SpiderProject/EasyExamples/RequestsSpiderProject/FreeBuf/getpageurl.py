# -*-coding:utf8-*-

import requests
import json
import random
import pymysql
import sys
import datetime
import time
from imp import reload

def getZhuanLanName():
    try:
        # Please write your MySQL's information.
        conn = pymysql.connect(
            host='localhost', user='root', passwd='123212', db='FreeBuf', charset='utf8')
        cursor = conn.cursor()
        sql = """SELECT url FROM FreeBuf.zhuanlan"""
        cursor.execute(sql)
        rs_count = cursor.rowcount  # 可以打印获取到的数据行数
        rs = cursor.fetchall()
        rs = list(rs)
        cursor.close()
        conn.close()

    except Exception as e:
        print(e)
    zhuanlan_name =[]
    for i in range(rs_count):
        dange = list(rs[i])
        yuansu = dange[0].split('?name=')[1:]
        zhuanlan_name.append(yuansu)
    #print(zhuanlan_name)
    return zhuanlan_name

def geturl(PageNum,ZhuanLanName):
    base_url = 'http://zhuanlan.freebuf.com/column/articleSelectHome/'+ '?page=' + str(PageNum)+'&name='+str(ZhuanLanName)
    return base_url

base_url = 'http://zhuanlan.freebuf.com/column/articleSelectHome/'+ '?name='

def getpage(url):
    zhuanlan_content = requests.get(url).text
    jsDict = json.loads(zhuanlan_content)
    statusJson = jsDict['status'] if 'status' in jsDict.keys() else False
    if statusJson == 200:
        if 'data' in jsDict.keys():
            data = jsDict['data']
            totalPage = data['totalPage']
            return totalPage

def getcontent(url):
    zhuanlan_content = requests.get(url).text
    jsDict = json.loads(zhuanlan_content)
    statusJson = jsDict['status'] if 'status' in jsDict.keys() else False
    if statusJson == 200:
        if 'data' in jsDict.keys():
            data = jsDict['data']
            totalPage = data['totalPage']
            list = data['list']
            for i in range(len(list)):
                list_i = list[i]
                page_id = list_i['id']
                title = list_i['title']
                page_url = list_i['url']
                imgUrl = list_i['imgUrl']
                contents = list_i['content']
                author = list_i['author']
                authorImg = list_i['authorImg']
                authorUrl = list_i['authorUrl']
                deploytime = list_i['time']
                comMount = list_i['comMount']
                readCount = list_i['readCount']
                money = list_i['money']
                #print((page_id,title,page_url,imgUrl,content,author,authorImg,authorUrl,deploytime,comMount,readCount,money))
                try:
                    print("Now is fangwen content %s" %title)

                    # Please write your MySQL's information.
                    conn = pymysql.connect(
                        host='localhost', user='root', passwd='123212', db='FreeBuf', charset='utf8')
                    cur = conn.cursor()
                    cur.execute('INSERT INTO content(page_id,title,page_url,imgUrl,contents,author,authorImg,authorUrl,deploytime,comMount,readCount,money) \
                                    VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
                                %
                                (page_id,title,page_url,imgUrl,contents,author,authorImg,authorUrl,deploytime,comMount,readCount,money))
                    conn.commit()
                    cur.close()
                    conn.close()
                except Exception as e:
                    print(e)
        else:
            print("no data now")
    else:
        print("Error: " + url)

if __name__ == '__main__':
    G = getZhuanLanName()
    for m in range(len(G)):
        ZhuanLanName = G[m][0]
        url = base_url + ZhuanLanName
        totalPage = getpage(url)
        for i in range(totalPage):
            getcontent(geturl(i,ZhuanLanName))
