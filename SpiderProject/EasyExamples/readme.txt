简单的爬虫小示例

#京东图片爬虫
爬取的起始URL：https://list.jd.com/list.html?cat=9987,653,655
这个URL是京东手机列表的第一页
爬取多个网页，变动的值仅是page=后的数字，表示的是页数
https://list.jd.com/list.html?cat=9987,653,655&page=9&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main


#链接爬虫
import re
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def getlink(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0')
    file = urllib.request.urlopen(req)
    data = str(file.read())
    print(data)
    pat = '(https?://[^s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link
url = "http://blog.csdn.net/"
linklist = getlink(url)
for link in linklist:
    print(link)
