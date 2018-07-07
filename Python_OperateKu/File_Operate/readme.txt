基本文件的操作

对文件进行操作的流程：
     第一，建立文件对象。
     第二，调用文件方法进行操作。
     第三，不要忘了关闭文件。
     （为什么要关闭python文件：1）将写缓存同步到磁盘；2）Linux系统中每个进程打开的个数是有限的，如果打开个数到了系统限制，再打开文件就会失败）




Python文件属性（常见）：
     file.fileno():文件描述符       file.mode : 文件打开权限
     file.encoding :文件编码        file.closed : 文件是否关闭
     使用f=open('file名'),f.fileno 等方式查看f属性
     f.buffer         f.fileno(        f.newlines       f.seekable(
     f.close(         f.flush(         f.read(          f.tell(
     f.closed         f.isatty(        f.readable(      f.truncate(
     f.detach(        f.line_buffering f.readline(      f.writable(
     f.encoding       f.mode           f.readlines(     f.write(
     f.errors         f.name           f.seek(          f.writelines(
Python标准文件：
     文件标准输入

     
1.能调用方法的一定是对象,比如数值、字符串、列表、元组、字典，甚至文件也是对象，Python中一切皆为对象。
 str1 = 'hello'
 str2 = 'world'
 str3 = ' '.join([str1,str2])
 print(str3)
 
2.三种基本的文件操作模式：r(only-read)、w(only-write)、a(append)

文件file1
一张褪色的照片，
好像带给我一点点怀念。
巷尾老爷爷卖的热汤面，
味道弥漫过旧旧的后院；
流浪猫睡熟在摇晃秋千，
夕阳照了一遍他咪着眼；
那张同桌寄的明信片，
安静的躺在课桌的里面。
(1)r模式
在只读模式下写入内容会报错。
 f = open('file1','r')
 f_read = f.read()   #read是逐字符地读取,read可以指定参数，设定需要读取多少字符，无论一个英文字母还是一个汉字都是一个字符。
 print(f_read)
 f.close()
 f = open('file1','r')
 f_read = f.readline() #readline只能读取第一行代码，原理是读取到第一个换行符就停止。
 print(f_read)
 f.close()
 f = open('file1','r')
 f_read = f.readlines() #readlines会把内容以列表的形式输出。
 print(f_read)
 f.close()
 f = open('file1','r')
 for line in f.readlines() #使用for循环可以把内容按字符串输出。
   print(line) #输出一行内容输出一个空行，一行内容一行空格... 因为文件中每行内容后面都有一个换行符，而且print()语句本身就可以换行，如果不想输出空行，就需要使用下面的语句：print(line.strip())
 f.close()
(2)w模式
在进行操作前，文件中所有内容会被清空。比如在file1中写入'hello world'，程序执行后file1中就只剩下一句'hello world'
 f = open('file1','w',encoding='utf8')  #由于Python3的默认编码方式是Unicode，所以在写入文件的时候需要调用utf8，以utf8的方式保存，这时pycharm（默认编码方式是utf8）才能正确读取，当读取文件时，文件是utf8格式，pycharm也是utf8，就不需要调用了。
 f_w = f.write('hello world')
 print(f_w)  #有意思的是，这里并不打印'hello world'，只打印写入多少字符
 f.close()
(3)a模式
与w模式不同的是，a模式不会把原来内容清空，而是光标移到内容最后位置，继续写入新内容。比如在最后追加'hello world'
 f = open('file1','a')
 f_a = f.write('hello world')
 print(f_a) #还是会打印写入的字符数
 f.close()
打印文件，在'流浪猫睡熟在摇晃秋千'后面加上'helloworld'输出
在r模式时，我们说过用for循环和readlines()输出文件内容，这种输出内容的原理是：打开文件，把全部内容读入内存，然后再打印输入，当文件很大时，这种读取方式就不靠谱了，甚至会使机器崩溃。我们需要及时关闭文件，如下：
f = open('file','r')
data=f.readlines()  #注意及时关闭文件
f.close()

num = 0
for i in data:
  num += 1
  if num == 5:
    i = ''.join([i.strip(),'hello world']) #不要使用“+”进行拼接
  print(i.strip())
f.close()
对于大数据文件，要使用下面的方法：
num = 0
f.close()  #不要过早关闭文件，否则程序不能识别操作句柄f.
f = open('file','r')
for i in f:  #for内部把f变为一个迭代器，用一行取一行。
  num += 1
  if num == 5:
    i = ''.join([i.strip(),'hello world'])
  print(i.strip())
f.close()
3.tell和seek
     tell：查询文件中光标位置
     seek：光标定位
f = open('file','r')
print(f.tell())  #光标默认在起始位置
f.seek(10)    #把光标定位到第10个字符之后
print(f.tell())  #输出10
f.close()
----------------------
f = open('file','w')
print(f.tell())  #先清空内容，光标回到0位置
f.seek(10)    
print(f.tell())
f.close()
----------------------
f = open('file','a')
print(f.tell())  #光标默认在最后位置
f.write（'你好 世界'）
print(f.tell())  #光标向后9个字符，仍在最后位置
f.close()
4.flush 同步将数据从缓存转移到磁盘
示例，实现进度条功能
import sys,time  #导入sys和time模块
for i in range(40):
  sys.stdout.write('*')
  sys.stdout.flush()  #flush的作用相当于照相，拍一张冲洗一张
  time.sleep(0.2)
下面代码也能够实现相同的功能
import time 
for i in range(40):
  print('*',end='',flush=True) #print中的flush参数
  time.sleep(0.2)
5.truncate 截断
不能是r模式下执行，
w模式下，已经清空所有数据，使用truncate没有任何意义，
a模式下，截断指定位置后的内容。
 f = open('file','a')
 f.truncate(6) #只显示6个字节的内容（6个英文字符或三个汉字），后面的内容被清空。
6.光标位置总结
一个汉字两个字节，涉及光标位置的方法有4个：read、tell、seek、truncate。
#--------------------------光标总结head-----------------------------------
f = open('file','r')
print(f.read(6)) #6个字符
print(f.tell())  #位置12字节，一个汉字两个字节
f.close()

f = open('file','r')
f.seek(6)      #6个字节
print(f.tell())
f.close()

f = open('file','a')
print(f.tell())  #光标默认在最后位置
f.write('你好 世界')
print(f.tell())  #光标向后9个字节，一个汉字两个字节，仍在最后位置 182-->191
f.close()

f = open('file','a',encoding='utf-8')
print(f.truncate(6)) #由于需要光标定位位置，所以也是字节。只显示6个字节的内容（6个英文字母或三个汉字,一个汉字两个字节），后面的内容被清空。
f.close()
#-----------------------------光标总结end---------------------------------
7.另外3种模式：r+、w+、a+
      r+：读写模式，光标默认在起始位置，当需要写入的时候，光标自动移到最后
     w+：写读模式，先清空原内容，再写入，也能够读取
     a+：追加读模式，光标默认在最后位置，直接写入，也能够读取。
f = open('file','a')
print(f.tell())  #末尾207位置
f.close()

f = open('file','r+')
print(f.tell())  #0位置
print(f.readline()) #读取第一行
f.write('羊小羚')   #光标移到末尾207位置并写入
print(f.tell())  #213位置
f.seek(0)     #光标移到0位置
print(f.readline())  #读取第一行
f.close()
8.修改文件内容
思路：由于数据存储机制的关系，我们只能把文件1中的内容读取出来，经过修改后，放到文件2中。
f2 = open('file2','w',encoding='utf8')  #写入的时候必须加utf8
f1 = open('file','r')
num = 0
for line in f1: #迭代器
  num += 1
  if num == 5:
    line = ''.join([line.strip(),'羊小羚\n'])  #里面就是对字符串进行操作了
  f2.write(line)
f1.close()
f2.close()
9.with语句
可以同时对多个文件同时操作，当with代码块执行完毕时，会自动关闭文件释放内存资源，不用特意加f.close() ，我们通过下面的示例体会with的用法和好处。
用with语句重写8中的代码
num = 0
with open('file','r') as f1,open('file2','w',encoding='utf8') as f2:
  for line in f1:
    num += 1
    if num == 5:
      line = ''.join([line.strip(),'羊小羚'])
    f2.write(line)


慕课网相关入门视频：
《python文件处理》 https://www.imooc.com/learn/416
     
