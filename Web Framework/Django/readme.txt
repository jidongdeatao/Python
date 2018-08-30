Django

默认pip安装方式：
    安装：pip install django
         指定版本号安装：pip install django==1.10.3
    查看：pip show django
    卸载：pip uninstall django

Django目录结构：
        创建一个新的Django项目（工程）与应用
        $django-admin.py startproject djangoproject
        $cd djangoproject
        $python manage.py startapp webapp
        $tree .
        .
        ├── webapp
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   └── models.py
        │   ├── tests.py
        │   └── views.py
        ├── djangoproject
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py
        1个目录，5个文件
    在根目录djangoproject下，可以得到：
        项目目录：djangoproject
        应用目录：webapp
        manage.py脚本：用于管理Django站点
            在项目目录djangoproje里包含：
                settings.py: 包含项目的所有配置参数
                urls.py: URL根配置
                wsgi.py: 内置runserver命令的WSGI应用配置
                __init__.py: 用来告诉python，当前目录是python模块
            在应用目录webapp里包含：
                admin.py  :  django 自带admin后面管理，将models.py 中表映射到后台
                apps.py :  blog 应用的相关配置
                models.py  : Django 自带的ORM，用于设计数据库表
                tests.py  :  用于编写Django单元测试
                veiws.py ：视图文件，用于编写功能的主要处理逻辑
    新建templates与static目录后，要在settings.py文件中加入路径：
        TEMPLATES = [
            {
                ...
                'DIRS': [os.path.join(BASE_DIR, 'templates')],
                ...
            }]
        #文件最后加入static路径：
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static")
        ]

