《精通python网络爬虫》--韦玮编著
运行python环境：python3.6

1.Urllib是什么
2.使用Uillib快速爬取网页
  步骤：
  方法一：
    1）从网页获取数据
      import urllib.request
      file = urllib.request.urlopen("http://www.baidu.com")

      ##################以下为三种读取页面的方式#####################

      #读取文件的全部内容 使用file.read(),会把读取到的内容赋值给一个字符串变量
      data = file.read()
      #print(data)

      ##读取文件的全部内容 与read()不同的是,readlines会把读取到的内容赋值给一个列表变量，若要读取全部内容，推荐使用这种方式
      datalines = file.readlines()
      #print(datalines)

      #读取页面一行内容 使用file.readline()
      dataline = file.readline()
      #print(dataline) #结果为b'',是由于只爬取了页面的第一行

     2)保存数据到本地
      fhandle = open("data.html","wb")
      fhandle.write(data)
      fhandle.close() 
   方法二：
      import urllib.request
      filename = urllib.request.urlretrieve("http://www.baidu.com",filename="data.html")
      
      #urlretrieve()函数执行的时候会产生缓存，需要使用urlcleanup()函数进行清除
      urllib.request.urlcleanup()
    
3.Urllib的常见用法
    import urllib.request
    file = urllib.request.urlopen("http://www.baidu.com")
      命令：
        1）
        #获取爬取网页的环境信息，以下为爬取百度首页返回的info
        info = file.info()
        #print(info)
          # Bdpagetype: 1
          # Bdqid: 0xcbc019b5000082d2
          # Cache-Control: private
          # Content-Type: text/html
          # Cxy_all: baidu+22ba0c02535743a893b966956094582a
          # Date: Sun, 01 Jul 2018 02:54:38 GMT
          # Expires: Sun, 01 Jul 2018 02:53:46 GMT
          # P3p: CP=" OTI DSP COR IVA OUR IND COM "
          # Server: BWS/1.1
          # Set-Cookie: BAIDUID=734CBA39D1D2FA96FB972FB811D40AA7:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
          # Set-Cookie: BIDUPSID=734CBA39D1D2FA96FB972FB811D40AA7; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
          # Set-Cookie: PSTM=1530413678; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
          # Set-Cookie: BDSVRTM=0; path=/
          # Set-Cookie: BD_HOME=0; path=/
          # Set-Cookie: H_PS_PSSID=1438_21100_20928; path=/; domain=.baidu.com
          # Vary: Accept-Encoding
          # X-Ua-Compatible: IE=Edge,chrome=1
          # Connection: close
          # Transfer-Encoding: chunked
        2）
        #获取返回码
        getcode = file.getcode()
        #print(getcode)

        #获取爬取的网页URL
        geturl = file.geturl()
        #print(geturl)
    
   
