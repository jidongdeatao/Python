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
 
