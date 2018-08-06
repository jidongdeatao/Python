xadmin
是一款开源的Django后台管理系统，比Django自带的后台管理系统功能更加完善

后台管理系统要求特点：
  具有权限管理功能、少前端样式、可以快速搭建
  
  
Django自带的admin后台管理系统会自动在
  settings.py:
      INSTALLED_APPS = [
      'django.contrib.admin',
      ..
      ]
  urls.py:
      urlpatterns = [
        url(r'^admin/', admin.site.urls),
      ]
    有默认配置
    
创建超级用户：python manage.py createsuperuser
            这里我创建的账号：admin 密码：adminpassword
            
使Django后台系统支持中文显示与修改时区设置（不然在处理时间会出现问题）：
    在settings.py:
      LANGUAGE_CODE = 'en-us'
      TIME_ZONE = 'UTC'
      USE_I18N = True
      USE_L10N = True
      USE_TZ = True
      修改为：
      LANGUAGE_CODE = 'zh-hans' #注意1.8版本后是这个包名，之前是zh-CN
      TIME_ZONE = 'Asia/Shanghai'
      USE_I18N = True
      USE_L10N = True
      USE_TZ = False
      
 在users/admin.py文件中把用户信息这个模块注册到后台管理系统，代码如下：
    from django.contrib import admin

    # Register your models here.

    from .models import UserProfile

    class UserProfileAdmin(admin.ModelAdmin):
        pass

    admin.site.register(UserProfile,UserProfileAdmin)
    
 刷新后台管理系统会发现用户信息出现在了后台，这个表与Models是对应的
 
 Django 默认admin管理系统介绍到这
 
 重点介绍xadmin 
 
Xadmin有两种安装方式：
  1.使用pip安装
    安装完之后，
    在settings.py将xadmin的两个名称
    'xadmin',
    'crispy_forms',
    添加进来
    在urls.py中
    import xadmin
    urlpatterns = [
        url(r'^xadmin/', xadmin.site.urls),
      ]
   同时需要删除掉之前使用users/admin.py注册到后台的模块
   然后将xadmin的表同步到数据库
   python manage.py makemigrations xadmin
   python manage.py migrate xadmin
   
   启动，在浏览器中输入127.0.0.1:8000/xadmin就进入了后台
  2.使用源码进行安装
      github上下载 然后对源码配置到项目中
      github地址：https://github.com/sshwsfc/xadmin
      下载后解压缩，新建与apps平级目录extra_apps,将文件夹中的xadmin目录拖到这个目录下
      这个extra_apps需要Mark为根目录，同时在settings.py中设置下
      BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
      sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
      sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))#新加入的位置
      不过也需要xadmin的依赖包django-crispy-forms
      与pip 安装xadmin一样配置一下
    图文教程参考：http://www.cnblogs.com/vincenshen/articles/6477069.html
    
 在Xadmin中配置APP功能模块：需要在APP中新建个adminx.py文件，xadmin会自动搜索该文件
  users/adminx.py 中的功能：
# -*- coding:utf-8 -*-
import xadmin
from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    list_display = ("code", "email", "send_type", "send_time")
    search_fields = ("code", "email", "send_type")
    list_filter = ("code", "email", "send_type", "send_time")

class BannerAdmin(object):
    list_display = ("title", "image", "url", "index", "add_time")
    search_fields = ("title", "image", "url", "index")
    list_filter = ("title", "image", "url", "index", "add_time")

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
      
 
      
