使用Requests库进行爬虫的项目

比urllib库更好使用的库


Mac下安装：
    # python 2+
    pip install requests
    # python 3+
    pip3 install requests

requests get请求演示：
    import requests
    import webbrowser
    param = {"wd": "XXX"}  # 搜索的信息
    r = requests.get('http://www.baidu.com/s', params=param)
    print(r.url)
    webbrowser.open(r.url)

requests post请求演示：
    data = {'firstname': 'XX', 'lastname': 'Y'}
    r = requests.post('http://zzz.php', data=data)
    print(r.text)

requests 上传图片：
    file = {'uploadFile': open('./image.png', 'rb')}
    r = requests.post('http://xxx.php', files=file)
    print(r.text)
    
requests 登录：
    #需要使用到cookie的传递
    payload = {'username': 'Morvan', 'password': 'password'}
    r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())
    # {'username': 'XXX', 'loggedin': '1'}
    
    r = requests.get('XXXX.php', cookies=r.cookies)
    print(r.text)

requests 使用Session进行登录：
  #每次都要传递 cookies 是很麻烦的, 好在 requests 有个很 handy 的功能, 那就是 Session. 
  #在一次会话中, 我们的 cookies 信息都是相连通的, 它自动帮我们传递这些 cookies 信息
    session = requests.Session()
    payload = {'username': 'Morvan', 'password': 'password'}
    r = session.post('http://welcome.php', data=payload)
    print(r.cookies.get_dict())
    # {'username': 'xxx', 'loggedin': '1'}

    r = session.get("http://xxxx.php")
    print(r.text)
    
    
    
requests 下载：
#为了下载到一个特定的文件夹, 我们先建立一个文件夹吧. 并且规定这个图片下载地址.
    import os
    os.makedirs('./img/', exist_ok=True)
    IMAGE_URL = "https://xxx.png"

    import requests
    r = requests.get(IMAGE_URL)
    with open('./img/image2.png', 'wb') as f:
        f.write(r.content)

#如果你要下载的是大文件, 比如视频等. requests 能让你下一点, 保存一点, 而不是要全部下载完才能保存去另外的地方. 
这就是一个 chunk 一个 chunk 的下载. 使用 r.iter_content(chunk_size) 来控制每个 chunk 的大小, 然后在文件中写入这个 chunk 大小的数据.

    r = requests.get(IMAGE_URL, stream=True)    # stream loading
    with open('./img/image3.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
            
对比urllib模块中的urlretrieve下载
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './img/image1.png')

