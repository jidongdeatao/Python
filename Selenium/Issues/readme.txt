Issues1-解决不安全连接的方法.txt
一、selenium+python+firefox解决不安全连接的方法

  1.firefox创建用户profile
        firefox.exe -p创建用户profile
  2.在1创建的用户profile中将需要访问的站点设置为信任
  3.selenium启动浏览器时设置启动1创建的用户profile
        代码如下：
        #coding=utf_8
        from selenium import webdriver
        from time import time,sleep
        #指定配置文件地址
        profile_directory = r"C:\Users\zhouj\AppData\Roaming\Mozilla\Firefox\Profiles\oj9vd1gi.zj_selenium_test"
        #加载配置
        profile = webdriver.FirefoxProfile(profile_directory)
        #启动浏览器配置
        br=webdriver.Firefox(profile)
        br.get("https://192.168.211.218")

        br.find_element_by_id("username").send_keys("superadmin")
        br.find_element_by_id("password").send_keys("p@ssw0rd")

        sleep(2)
        br.find_element_by_class_name("s-button").click()
        url=br.current_url
        print (url)
