这部分为数据表设计

需要设计4个APP，分别对应着4张数据表：
  分别是
  1)users
  2)courses
  3)organization
  4)operation
  
  
实际操作：
  环境：Python2.7
       Django ==1.9
       MySQL
       Navicat
       
一、环境搭建
  1.使用virtualenv虚拟环境：
      $ mkvirtualenv -p /usr/bin/python2.7 mxonlinevenv
      $ source mxonlinevenv/bin/activate
      $ pip install django==1.9
      $ django-admin.py startproject MxOnline
      $ cd MxOnline/
      $ pip install mysql-python
  2.使用Pycharm打开项目MxOnline，并配置运行环境为上面设置的虚拟环境mxonlinevenv
  3.修改 MxOnline/settings.py中
          DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': "mxonline",
              'USER':'root',
              'PASSWORD':'123212',
              'HOST':'127.0.0.1'
              }
            }
  4.使用Navicat新建数据库mxonline，字符集“utf-8”，编码顺序“utf8-general-ci”
  5.由于我的pycharm是社区版，没有办法在pycharm中执行manage.py命令
    只好通过Bash来操作：
    $ python manage.py makemigrations
    $ python manage.py migrate
    打开浏览器:http://127.0.0.1:8000 看下是否运行成功
    
 二、APP users设计
    新建APP users：
    $ python manage.py startapp users
    编辑users/models.py
    
 三、APP courses设计
 
 四、APP organization 设计
 
 五、APP operation 设计
 
    
