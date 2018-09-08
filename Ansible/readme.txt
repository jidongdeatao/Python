Ansible
GitHub地址；
https://github.com/ansible/ansible

ansible的官方文档：
https://docs.ansible.com/

Ansible原理：
Ansible 默认通过 SSH 协议进行管理。同时 Ansible 是基于 python 的一个模块（paramiko）开发的，遵循 SSH 协议，
支持加密和认证的方式来进行远程服务器连接，因此 Ansible 不需要客户端和服务端。
Ansible 可以通过命令来简单执行一些任务，也可以通过 palybook的配置脚本来执行复杂任务，同时 playbook不用分发到远程，在本地就可以执行。
Ansible 中的 playbook 使用的是 Jinja2 （基于 python 的模板引擎），简单易学
Ansible 基于模块工作，易于扩展，而模块可以用任何语言编写，并以标准输出的 JSON协议进行通信

请先从安装和配置文件.txt开始看起：
   如何添加一台机器？
   1、添加主机到/etc/ansible/hosts
   2、添加本机的公钥到目标机器
   3、添加本机的私钥到ansible
   4、运行ansible all -m ping测试是否添加成功
ansible的基本使用

      ad-hoc ：临时命令，是在输入内容后，快速执行某些操作，但不希望保存下来的命令。
        一般来说，Ansible 主要在于我们后面会学到的 playbook 的脚本编写，但是，ad-hoc 相较来说，它的优势在于当你收到一个临时任务时，
        你只用快速简单的执行一个 ad-hoc 临时命令，而不用去编写一个完整的 playbook 脚本就可以了。
        类似于这种命令$ ansible all -m ping被称为ad-hoc 命令。

      Playbook 
      是一种非常简单的配置管理系统以及是多机器部署系统的基础，十分适合复杂的应用部署。
      同时，Playbook 还可以用于声明配置，以及编排有序的执行过程，使得在多组机器之间有序的执行指定步骤，或者同步或异步的发起任务。
      Playbook 也是一个任务列表，这个列表中的可以包含一个或者多个 plays，所有的操作放在这么一个文件中，然后一次性的执行。
      而它与 AD-HOC 最大的不同之处就在于它是把这些任务放在源码中进行控制。
      执行命名方式：
      $ ansible-playbook **.yaml
      






Python运维开发场景：
   基础（python基础-Django基础-DevOps构建）
    ||
    \/
自动化资产扫描发现（资产扫描作用、nmap存活扫描、telnetlib端口扫描、perspect登陆探测、paramiko登陆探测、docker容器扫描、KVM虚拟机扫描、snmp网络设备、SDK调用扫描ESXI）
    ||
    \/
ansible自动化任务（ansible安装、python ansible、ansible adhoc、ansible playbook、核心类调用、api接口封装、方法改写、Redis消息存储、Mongo事件日志)



ansible是python中的一套模块，系统中的一套自动化工具，可以用来做系统管理、自动化命令等任务。

ansible的play_book模式，采用yaml配置，对于自动化任务执行一目了然。

GitHub地址：
https://github.com/ansible/ansible

自动化任务执行
举例：
在n台服务器安装某服务，自动化任务执行只需要将步骤


自动化任务执行的应用：





图文教程：
http://blog.51cto.com/191226139/2066936

慕课网免费课程：
https://www.imooc.com/video/15229
