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
    
