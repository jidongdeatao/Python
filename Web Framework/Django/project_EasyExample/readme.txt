利用Django快速搭建Blog
  #转自虫师博客
  http://www.cnblogs.com/fnng/p/3737964.html
本文只讲述最直接的命令，图文教程请查看上链接

操作环境：
  python3.6
  Django2.0
  
#第一部分：实现目标：可以访问前台与后台
第一步：使用virtualenv创建项目环境，以及安装Django
        mkdir myproject
        cd myproject
        virtualenv --no-site-packages venv
        source venv/bin/activate
        pip install django
第二步：创建项目与应用
       > django-admin startproject mysite   # 创建mysite项目
       > cd mysite        # 切换到mysite目录
       mysite> python manage.py startapp blog   # 创建blog应用
第三步：打开mysite/mysite/settings.py,把blog应用添加到配置文件中
        # Application definition
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'blog',#添加的位置
        ]
第四步：初始化admin后台数据库与创建超级管理员账号（这里默认使用SQLite3自带的数据库）
        mysite> python manage.py migrate
        mysite> python manage.py createsuperuser
        这里按照操作自己配置
第五步:启动应用&访问后台（第一部分完成）
        mysite> python manage.py runserver
        通过浏览器访问前台：http://127.0.0.1:8000
        通过浏览器访问后台：http://127.0.0.1:8000/admin
        
#第二部分：实现目标：设计数据库表
第一步：设计blog表，通过编辑mysite/blog/models.py
        from django.db import models

        # Create your models here.
        class BlogsPost(models.Model):
            title = models.CharField(max_length = 150)  # 博客标题
            body = models.TextField()                   # 博客正文
            timestamp = models.DateTimeField()          # 创建时间
第二步：执行数据库同步
      mysite> python manage.py makemigrations blog
      mysite> python manage.py migrate
第三步：通过Admin后台来管理blog表数据。打开mysite/blog/admin.py
      from django.contrib import admin
      from blog.models import BlogsPost
      # Register your models here.
      class BlogsPostAdmin(admin.ModelAdmin):
          list_display = ['title', 'body', 'timestamp']
      admin.site.register(BlogsPost, BlogsPostAdmin)
第四部：登录Admin后台添加blog
      再次启动项目，访问后台，编写博客并保存
      
#第三部分：实现目标：更换前台模版
第一步：创建模版：在blog项目下创建templates目录（mysite/blog/templates/）,在目录下创建模板文件index.html，内容如下：
      {% for blog in blog_list %}
          <h2>{{ blog.title }}</h2>
          <p>{{ blog.timestamp }}</p>
          <p>{{ blog.body }}</p>
      {% endfor %}
第二步：创建视图函数：编辑mysite/blog/views.py：
      from django.shortcuts import render
      from blog.models import BlogsPost
      # Create your views here.
      def blog_index(request):
          blog_list = BlogsPost.objects.all()  # 获取数据库里面所拥有BlogPost对象的所有数据
          return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html页面，顺带把数据库中查询出来的所有博客内容blog_list一并返回
第三步：创建blog的URL模式：编辑mysite/mysite/urls.py:
      from django.contrib import admin
      from django.urls import path
      from blog import views

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('blog/', views.blog_index),
      ]
第四步：再次启动服务，访问blog应用：http://127.0.0.1:8000/blog/

至此项目完成。
美化部分另见其他文档


 
