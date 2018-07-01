《精通python网络爬虫》--韦玮编著
运行python环境：python3.6

1.Urllib是什么
2.使用Uillib快速爬取网页
  步骤：
  方法一：
    1）从网页获取数据
      import urllib.request
      file = urllib.request.urlopen("http://www.cn.baidu.com")

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
    fil
    
    
   
