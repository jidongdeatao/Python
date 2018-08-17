# -*-coding:utf8-*-

import requests
import json
import random
import pymysql
import sys
import datetime
import time
from imp import reload

zhuanlan_urls = []

# Please change the range data by yourself.
for i in range(100):
    zhuanlan_url = 'http://zhuanlan.freebuf.com/index/columRec/?tag=0'
    zhuanlan_urls.append(zhuanlan_url)

qucongid =(str(0),)
def getsource(zhuanlanurl):
    global qucongid
    try:
        zhuanlan_content = requests.get(zhuanlanurl).text
        jsDict = json.loads(zhuanlan_content)
        statusJson = jsDict['status'] if 'status' in jsDict.keys() else False
        if statusJson == 200:
            if 'data' in jsDict.keys():
                for i in  range(len(jsDict['data'])):

                    jsData_i = jsDict['data'][i]
                    mid = jsData_i['id']
                    columName = jsData_i['columName']
                    imgUrl = jsData_i['imgUrl']
                    url = jsData_i['url']
                    intro = jsData_i['intro']
                    attenMount = jsData_i['attenMount']
                    artiMount = jsData_i['artiMount']
                    if mid in qucongid:
                        continue
                    else:
                        try:
                            qucongid = qucongid + (mid,)
                            print("Now is fangwen column %s" % columName)

                            # Please write your MySQL's information.
                            conn = pymysql.connect(
                                host='localhost', user='root', passwd='123212', db='FreeBuf', charset='utf8')
                            cur = conn.cursor()
                            cur.execute('INSERT INTO zhuanlan(mid,columName,imgUrl,url,intro,attenMount,artiMount) \
                                            VALUES ("%s","%s","%s","%s","%s","%s","%s")'
                                        %
                                        (mid,columName,imgUrl,url,intro,attenMount,artiMount))
                            conn.commit()
                        except Exception as e:
                            print(e)
            else:
                print("no data now")
        else:
            print("Error: " + zhuanlanurl)
    except Exception as e:
        print(e)
                
if __name__ =='__main__':
    for url in zhuanlan_urls:
        getsource(url)
