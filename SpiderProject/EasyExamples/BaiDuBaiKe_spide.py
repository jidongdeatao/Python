#目的：从 “网页爬虫” 的词条开始爬, 然后在页面中任意寻找下一个词条, 爬过去, 再寻找词条, 继续爬. 看看最后我们爬到的词条和 “网页爬虫” 差别有多大.

#观察规律：
‘’‘
这个爬虫说实在的, 并不难, 只有20+行代码. 但是却能让它游走在百度百科的知识的海洋中. 首先我们需要定义一个起始网页, 我选择了 “网页爬虫”. 我们发现, 页面中有一些链接, 指向百度百科中的另外一些词条, 比如说下面这样.
<a target="_blank" href="/item/%E8%9C%98%E8%9B%9B/8135707" data-lemmaid="8135707">蜘蛛</a>
<a target="_blank" href="/item/%E8%A0%95%E8%99%AB">蠕虫</a>
<a target="_blank" href="/item/%E9%80%9A%E7%94%A8%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E">通用搜索引擎</a>
通过观察, 我们发现, 链接有些共通之处. 它们都是 /item/ 开头, 夹杂着一些 %E9 这样的东西. 但是仔细搜索一下, 发现还有一些以 /item/ 开头的, 却不是词条. 比如
<a href="/item/史记·2016?fr=navbar" target="_blank">史记·2016</a>
’‘’

#制作爬虫

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com"

his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()
        
        
