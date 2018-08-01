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
    
    在MxOnline settings.py中加入users与替换用户表：
          INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'users',
      ]
      AUTH_USER_MODEL = "users.UserProfile"
    然后更新：
    $ python manage.py makemigrations users
    $ python manage.py migrate users
    
 三、APP courses设计
    新建APP courses：
    $ python manage.py startapp courses
    编辑courses/models.py
    
 四、APP organization 设计
    新建APP organization：
    $ python manage.py startapp organization
    编辑organization/models.py
 
 五、APP operation 设计
    新建APP operation：
    $ python manage.py startapp operation
    编辑operation/models.py
    
 六、在MxOnline settings.py中加入所有APP：
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'organization',
    'operation',
]
 更新：
    $ python manage.py makemigrations
    $ python manage.py migrate
 Pycharm中在project目录下新建个python package，名字为apps，然后把上面新建的4个APP拖入到其中，
    点击apps右键，Mark Directory as source root
 在MxOnlie settings.py中把apps加入到python搜索目录之下，
    import os
    import sys #新加入
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0,os.path.join(BASE_DIR,'apps')) #新加入
    
    运行，看下有无报错
    本部分结束
    
    
    
    
