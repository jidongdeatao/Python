
import re
import urllib.request

def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 ='<div id = "plist".+? <div class="gl-i-wrap j-sku-item">'
    result1 = re.compile(pat1).findall(html1)
    print(result1)
    result1 = result1[0]
    pat2 = '<img width ="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    x =1
    for imageurl in imagelist:
        imagename = "/Users/wangxitao/Desktop/img"+str(page)+str(x)+".jpg"
        imageurl = "http://" +imageurl
        try :
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
            x+=1
for i in range(1,79):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)
