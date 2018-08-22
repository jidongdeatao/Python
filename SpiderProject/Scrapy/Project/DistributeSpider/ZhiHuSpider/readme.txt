首先创建：
scrapy genspider zhihu www.zhihu.com


使用requests库来完成登录，详情见login_zhihu.py
使用这个的原因，是有些数据的获取必须通过登录后才能够获取到
这个登录属于单独的模块，可以移植到其他网站

