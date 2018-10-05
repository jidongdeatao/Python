# -*- coding:utf-8 -*-

from configparser import ConfigParser
import os


class INIParser:
    def __init__(self, path):
        self.path = path
        self.ini = ConfigParser()
        self.ini.read(self.path)

        # 获取sections列表
    def get_sections(self):
        if self.ini:
            return self.ini.sections()

            # 获取指定的section的options列表
    def get_options_by_section(self, section):
        if self.ini:
            return self.ini.options(section)

            # 获取指定section的配置信息列表
    def get_section_items(self, section):
        if self.ini:
            return self.ini.items(section)

            # 按类型读取配置信息

    # 返回字符串类型
    def get_string(self, section, option):
        if self.ini:
            return self.ini.get(section, option)

            # 返回int类型

    def get_int(self, section, option):
        if self.ini:
            return self.ini.getint(section, option)

            # 返回float类型

    def get_float(self, section, option):
        if self.ini:
            return self.ini.getfloat(section, option)

            # 返回bool类型

    def get_boolean(self, section, option):
        if self.ini:
            return self.ini.getboolean(section, option)

            # 新增section
    def add_section(self, section):
        if self.ini:
            self.ini.add_section(section)
            self.ini.write(open(self.path, "w"))

            # 设置指定option值

    def set_option(self, section, option, value):
        if self.ini:
            self.ini.set(section, option, value)
            self.ini.write(open(self.path, "w"))

            # 删除指定section
    def remove_section(self, section):
        if self.ini:
            self.ini.remove_section(section)
            self.ini.write(open(self.path, "w"))

            # 删除指定option

    def remove_option(self, section, option):
        if self.ini:
            self.ini.remove_option(section, option)
            self.ini.write(open(self.path, "w"))


if __name__ == "__main__":
    print("python ini标准库解析实例")

    # 如果存在mysql.ini先删除，方便下列代码的运行
    if os.path.exists("mysql.ini"):
        os.remove("mysql.ini")

        # 我们先写一些数据到mysql.ini中
    ini = INIParser("mysql.ini")

    # 先加一个mysql section
    mysql_section = "mysql"
    ini.add_section(mysql_section)

    # 在mysql section下写入一些配置信息
    ini.set_option(mysql_section, "host", "127.0.0.1")
    ini.set_option(mysql_section, "port", "3306")
    ini.set_option(mysql_section, "db", "autotesting")
    ini.set_option(mysql_section, "user", "root")
    ini.set_option(mysql_section, "password", "123456")

    # 再添加一个oracle section
    oracle_section = "oracle"
    ini.add_section(oracle_section)

    # oracle section下写入一些配置信息
    ini.set_option(oracle_section, "host", "127.0.0.1")
    ini.set_option(oracle_section, "port", "1520")
    ini.set_option(oracle_section, "db", "auto_ui")
    ini.set_option(oracle_section, "user", "sa")
    ini.set_option(oracle_section, "password", "123456")

    # 获取下所有的section，并在console输出
    sections = ini.get_sections()
    print(sections)

    # 遍历各个section下的options，并在console中输出
    print("---" * 20)
    for sec in sections:
        print(sec, " 中的options为： ")
        options = ini.get_options_by_section(sec)
        print(options)
        print("---" * 20)

        # 获取各个section下的配置信息
    for sec in sections:
        print(sec, " 中的配置信息为： ")
        items = ini.get_section_items(sec)
        print(items)
        print("---" * 20)

        # 获取指定的option值这里演示读取host和port
    host = ini.get_string("mysql", "host")
    port = ini.get_int("mysql", "port")
    print("类型： ", type(host), " ", type(port))
    print(host, " ", port)

    # 删除mysql中的host配置
    ini.remove_option("mysql", "host")

    # 删除oracle section
    ini.remove_section("oracle")

    # 修改mysql port的值为4000
    ini.set_option("mysql", "port", "4000")

    # 最终mysql.ini中的文件内容如下
    # [mysql]
    # port = 4000
    # db = autotesting
    # user = root
    # password = 123456

