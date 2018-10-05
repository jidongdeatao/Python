Python文件基础操作
	包括文件打开及文件不同的打开方式、
	使用read,readlines及迭代器访问文件、
	文件写入方式及写缓存处理、
	文件关闭及由不关闭导致的问题、
	文件指针及文件指针操作
文件属性及OS模块使用
	包括文件属性、标准文件、文件命令行参数、文件编码格式、使用os模块中方法对文件进行操作、使用os模块中的方法对目录进行操作
python文件操作练习--使用ConfigParser模块对ini文件进行管理


对文件进行操作的流程：
     第一，建立文件对象。
     第二，调用文件方法进行操作。
     第三，不要忘了关闭文件。
     （为什么要关闭python文件：1）将写缓存同步到磁盘；2）Linux系统中每个进程打开的个数是有限的，如果打开个数到了系统限制，再打开文件就会失败）

在Linux文件系统中Python对文件操作的过程分析：
          得到文件对象
          打开文件，得到文件描述符
          对应文件驱动
          硬件设备


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
     
     
    使用普通方式打开文件：写入u'中文'，出现的问题：
    f = open('1.txt','r+') f.write(u'中文') 报UnicodeEncodeError
    需要将unicode转码为'utf-8'然后写入
    a=unicode.encode(u'中文','utf-8) 然后f.write(a)就没有问题
    
    使用codecs模块创建一个utf-8或者其他编码格式的文件
    import codecs
    f = codecs.open(fname,mode,encoding,errors,buffering)
    如：f = codecs.open('test.txt','w','utf-8')
          可以直接f.write(u'中文')
          
Python标准文件(sys模块)：
     文件标准输入：sys.stdin
     文件标准输出：sys.stdout
     文件标准错误：sys.stderr
     import sys
     >>> sys.stdin.
          sys.stdin.buffer         sys.stdin.isatty(        sys.stdin.readlines(
          sys.stdin.close(         sys.stdin.line_buffering sys.stdin.seek(
          sys.stdin.closed         sys.stdin.mode           sys.stdin.seekable(
          sys.stdin.detach(        sys.stdin.name           sys.stdin.tell(
          sys.stdin.encoding       sys.stdin.newlines       sys.stdin.truncate(
          sys.stdin.errors         sys.stdin.read(          sys.stdin.writable(
          sys.stdin.fileno(        sys.stdin.readable(      sys.stdin.write(
          sys.stdin.flush(         sys.stdin.readline(      sys.stdin.writelines(
     >>> sys.stdout.
          sys.stdout.buffer         sys.stdout.isatty(        sys.stdout.readlines(
          sys.stdout.close(         sys.stdout.line_buffering sys.stdout.seek(
          sys.stdout.closed         sys.stdout.mode           sys.stdout.seekable(
          sys.stdout.detach(        sys.stdout.name           sys.stdout.tell(
          sys.stdout.encoding       sys.stdout.newlines       sys.stdout.truncate(
          sys.stdout.errors         sys.stdout.read(          sys.stdout.writable(
          sys.stdout.fileno(        sys.stdout.readable(      sys.stdout.write(
          sys.stdout.flush(         sys.stdout.readline(      sys.stdout.writelines(
     ########################
     sys模块提供sys.argv属性，通过该属性得到命令行参数
          sys.argv:字符串组成的列表
     这个方法常用于程序输入不同的参数，
