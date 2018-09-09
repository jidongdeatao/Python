基于python的开源性能测试工具-Locust
使用 Python 代码来定义用户行为。用它可以模拟百万计的并发用户访问你的系统。

官网：
https://locust.io/
GitHub：https://github.com/locustio/locust
官方文档：
https://docs.locust.io/en/stable/

介绍
    Locust 完全基本 Python 编程语言，采用 Pure Python 描述测试脚本，并且 HTTP 请求完全基于 Requests 库。
    除了 HTTP/HTTPS 协议，Locust 也可以测试其它协议的系统，只需要采用Python调用对应的库进行请求描述即可。
    LoadRunner 和 Jmeter 这类采用进程和线程的测试工具，都很难在单机上模拟出较高的并发压力
    Locust 的并发机制摒弃了进程和线程，采用协程（gevent）的机制。协程避免了系统级资源调度，由此可以大幅提高单机的并发能力。
    正是基于这样的特点，使我选择使用Locust工具来做性能测试，另外一个原因是它可以让我们换一种方式认识性能测试，可能更容易看清性能测试的本质。

安装：
参考安装指南
  
开始入门实战：
    编写简单的性能测试脚本
创建 load_test.py 文件，通过 Python 编写性能测试脚本。
from locust import HttpLocust, TaskSet, task
class UserBehavior(TaskSet):
    @task
    def baidu_index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

上述代码解释：
    UserBehavior类继承TaskSet类，用于描述用户行为。
    baidu_index() 方法表示一个用户为行，访问百度首页。使用@task装饰该方法为一个事务。client.get()用于指请求的路径“/”，
    因为是百度首页，所以指定为根路径。
    WebsiteUser类用于设置性能测试。
        task_set ：指向一个定义的用户行为类。
        min_wait ：执行事务之间用户等待时间的下界（单位：毫秒）。
        max_wait ：执行事务之间用户等待时间的上界（单位：毫秒）。

启动性能测试
> locust -f .\load_test.py --host=https://www.baidu.com

    -f 指定性能测试脚本文件。
    –host 指定被测试应用的URL的地址，注意访问百度使用的HTTPS协议。

通过浏览器访问：http://localhost:8089（Locust启动网络监控器，默认为端口号为: 8089）设置测试：
    在Number of users to simulate输入框中输入10
    在Hatch rate输入框中输入2
    Number of users to simulate 设置模拟用户数。
    Hatch rate（users spawned/second） 每秒产生（启动）的虚拟用户数。
    点击 “Start swarming” 按钮，开始运行性能测试。
运行测试主页面的性能测试参数：
    Type： 请求的类型，例如GET/POST。
    Name：请求的路径。这里为百度首页，即：https://www.baidu.com/
    request：当前请求的数量。
    fails：当前请求失败的数量。
    Median：中间值，单位毫秒，一半的服务器响应时间低于该值，而另一半高于该值。
    Average：平均值，单位毫秒，所有请求的平均响应时间。
    Min：请求的最小服务器响应时间，单位毫秒。
    Max：请求的最大服务器响应时间，单位毫秒。
    Content Size：单个请求的大小，单位字节。
    reqs/sec：是每秒钟请求的个数。

Locust no-web模式：
    对刚才那个脚本，使用no-web模式运行
    > locust -f load_test.py --host=https://www.baidu.com --no-web -c 10 -r 2 -t 1m
    启动参数含义：
    –no-web 表示不使用Web界面运行测试。
    -c 设置虚拟用户数。
    -r 设置每秒启动虚拟用户数。
    -t 设置设置运行时间。



