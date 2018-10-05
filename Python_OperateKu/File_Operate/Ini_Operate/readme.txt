Python操作ini配置文件--使用ConfigParser模块对ini文件进行管理：实现查询、添加、删除、保存

ini配置文件格式：
节： [session]
参数(键=值) name=value

例子：
[port]
	port1=8000
	port2=8001

基础用法
#############################################################################
import configparser

cfg = configparser.ConfigParser()
cfg.read('one.ini')
"""
one.ini内容为：

[userinfo]
name=zhangsan
pwd=abc

[study]
python_base=15
python_junior=20
linux_base=15

"""
#打印所有section的值
# print(cfg.sections()) #['userinfo', 'study']

#遍历sections,取出sections中的name与值
# for se in cfg.sections():
#     print(se)  #userinfo
#     print(cfg.items(se)) #[('name', 'zhangsan'), ('pwd', 'abc')]

#增加到已有session下的name与值,这种方式只是放在内存中，没有保存到文件中
# cfg.set('userinfo','email','zhangsan@qq.com')

#增加到已有session下的name与值,并将修改保存到ini文件中
# fp=open('one.ini','w')
# cfg.set('userinfo','email','zhangsan@qq.com')
# cfg.write(fp)
# fp.close()

#删除已有session下的name与值
# cfg.remove_option('userinfo','email')
