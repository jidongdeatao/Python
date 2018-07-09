Flask

第一个demo：
    操作环境：
        pyhon3.6
    使用virtualenv创建项目环境，以及安装flask
        mkdir myproject
        cd myproject
        virtualenv --no-site-packages flaskvenv
        source flaskvenv/bin/activate
        pip install flask
        安装完成后查看：pip freeze
    新建app.py,在其中输入以下代码并运行:
        # coding;utf8
        from flask import Flask
        app =Flask(__name__)
        @app.route("/")
        def index():
            return "<h1 style='color:red'>Hello World</h1>"
        if __name__ =="__main__":
            app.run()
    显示：* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    在浏览器打开http://127.0.0.1:5000/可以看到输出结果了
    
