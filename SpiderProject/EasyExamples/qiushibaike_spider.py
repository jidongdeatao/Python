
#(2)
import urllib.request
import re
def getcontent(url,page):
    #模拟成浏览器
    headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    #构建对应用户提取的正则表达式
    userpat='target="_blank" title="(.*?)">'
    #构建段子内容提取的正则表达式
    contentpat='<div class="content">(.*?)</div>'
    #寻找出所有的用户
    userlist=re.compile(userpat,re.S).findall(data)
    #寻找出所有的内容
    contentlist=re.compile(contentpat,re.S).findall(data)
    x=1
    #通过for循环遍历段子内容并将内容分别赋给对应的变量
    for content in contentlist:
        content=content.replace("\n","")
        #用字符串作为变量名，先将对应字符串赋给一个变量
        name="content"+str(x)
         #通过exec()函数实现用字符串作为变量名并赋值
        exec(name+'=content')
        x+=1
    y=1
    #通过for循环遍历用户，并输出该用户对应的内容
    for user in userlist:
        name="content"+str(y)
        print("用户"+str(page)+str(y)+"是:"+user)
        print("内容是:")
        exec("print("+name+")")
        print("\n")
        y+=1
#分别获取各页的段子，通过for循环可以获取多页
for i in range(1,30):
    url="http://www.qiushibaike.com/8hr/page/"+str(i)
    getcontent(url,i)
