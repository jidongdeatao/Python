Django

默认pip安装方式：
    安装：pip install django
         指定版本号安装：pip install django==1.10.3
    查看：pip show django
    卸载：pip uninstall django

Django目录结构：
        创建一个新的Django项目（工程）
        $django-admin.py startproject djangoproject
        $cd djangoproject
        $tree .
        .
        ├── djangoproject
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py
        1个目录，5个文件
    在根目录djangoproject下，可以得到：
        项目目录：djangoproject
        manage.py脚本：用于管理Django站点
            在项目目录djangoproje里包含：
            settings.py: 包含项目的所有配置参数
            urls.py: URL根配置
            wsgi.py: 内置runserver命令的WSGI应用配置
            __init__.py: 用来告诉python，当前目录是python模块
