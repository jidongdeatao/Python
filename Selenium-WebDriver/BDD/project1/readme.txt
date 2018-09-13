执行前准备：
  测试环境为python2.7
  pip install lettuce
  pip install selenium

项目说明：
  lettuce可以调用selenium来执行保存在scenario情景中的表格数据，并将执行过程记录在日志中

项目结构：
    project1/features/|- sogou.feature
                      |- sogou.py
                      |- terrain.py
                      |- report.log（项目执行完才会生成）

执行方式：
  cd到features文件到上级目录，输入命令:lettuce
  就可以看到项目的执行
  
代码详情见features下的文件
