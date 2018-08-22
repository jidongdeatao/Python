首先创建：
scrapy genspider zhihu www.zhihu.com

login_zhihu.py这个在新版本知乎上已经不可用，现在登录是通过selenium来完成
  使用requests库来完成登录，详情见login_zhihu.py
  使用登录的原因，是有些数据的获取必须通过登录后才能够获取到
  这个登录属于单独的模块，可以移植到其他网站
    验证码识别还是需要手工（可以想象到为啥打码平台那么火爆），这里只是单纯的把验证码下载下来

