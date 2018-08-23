Python网络编程：Socket库
Python的Socket模块可以用来编写客户端、服务端，以及一个TCP代理，之后可以完善成我们自己的netcat

该库的具体应用：
一、构建类似于netcat的反向连接木马程序
二、构建类似于使用TCP连接进行扫描的nmap


Socket 是进程间通信的一种方式，它与其他进程间通信的一个主要不同是：它能实现不同主机间的进程间通信，我们网络上各种各样的服务大多都是基于 Socket 来完成通信的，例如我们每天浏览网页、QQ 聊天、收发 email 等等。要解决网络上两台主机之间的进程通信问题，首先要唯一标识该进程，在 TCP/IP 网络协议中，就是通过 (IP地址，协议，端口号) 三元组来标识进程的，解决了进程标识问题，就有了通信的基础了。

本文主要介绍使用Python 进行TCP Socket 网络编程，假设你已经具有初步的网络知识及Python 基本语法知识。
TCP 是一种面向连接的传输层协议，TCP Socket 是基于一种 Client-Server 的编程模型，服务端监听客户端的连接请求，一旦建立连接即可以进行传输数据。那么对 TCP Socket 编程的介绍也分为客户端和服务端：

一、客户端编程
      创建socket
      首先要创建 socket，用 Python 中 socket 模块的函数 socket 就可以完成：
      #Socket client example in python

      import socket  #for sockets
      #create an AF_INET, STREAM socket (TCP)
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      print 'Socket Created'

      函数socket.socket 创建一个 socket，返回该 socket 的描述符，将在后面相关函数中使用。该函数带有两个参数：
      Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）
      Type：套接字类型，可以是 SOCKET_STREAM（流式套接字，主要用于 TCP 协议）或者SOCKET_DGRAM（数据报套接字，主要用于 UDP 协议）
      注：由于本文主要概述一下 Python Socket 编程的过程，因此不会对相关函数参数、返回值进行详细介绍，需要了解的可以查看相关手册

      错误处理
      如果创建 socket 函数失败，会抛出一个 socket.error 的异常，需要捕获：
      #handling errors in python socket programs

      import socket  #for sockets
      import sys #for exit
      try:
        #create an AF_INET, STREAM socket (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit();

      print 'Socket Created'

      那么到目前为止已成功创建了 socket，接下来我们将用这个 socket 来连接某个服务器，就连 www.google.com 吧。

      连接服务器
      本文开始也提到了，socket 使用 (IP地址，协议，端口号) 来标识一个进程，那么我们要想和服务器进行通信，就需要知道它的 IP地址以及端口号。
      获得远程主机的 IP 地址

      Python 提供了一个简单的函数 socket.gethostbyname 来获得远程主机的 IP 地址：
      host = 'www.google.com'
      port = 80

      try:
        remote_ip = socket.gethostbyname( host )
      except socket.gaierror:
        #could not resolve
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

      print 'Ip address of ' + host + ' is ' + remote_ip

      现在我们知道了服务器的 IP 地址，就可以使用连接函数 connect 连接到该 IP 的某个特定的端口上了，下面例子连接到 80 端口上（是 HTTP 服务的默认端口）：
      #Connect to remote server
      s.connect((remote_ip , port))
      print 'Socket Connected to ' + host + ' on ip ' + remote_ip

      运行该程序：
      $ python client.py
      Socket created
      Ip of remote host www.google.com is 173.194.38.145
      Socket Connected to www.google.com on ip 173.194.38.145

      发送数据
      上面说明连接到 www.google.com 已经成功了，接下面我们可以向服务器发送一些数据，例如发送字符串GET / HTTP/1.1\r\n\r\n，这是一个 HTTP 请求网页内容的命令。
      #Send some data to remote server
      message = "GET / HTTP/1.1\r\n\r\n"
      try :
        #Set the whole string
        s.sendall(message)
      except socket.error:
        #Send failed
        print 'Send failed'
        sys.exit()
      print 'Message send successfully'

      发送完数据之后，客户端还需要接受服务器的响应。
      接收数据
      函数 recv 可以用来接收 socket 的数据：
      #Now receive data
      reply = s.recv(4096)

      print reply
      一起运行的结果如下：

      Socket created
      Ip of remote host www.google.com is 173.194.38.145
      Socket Connected to www.google.com on ip 173.194.38.145
      Message send successfully
      HTTP/1.1 302 Found
      Cache-Control: private
      Content-Type: text/html; charset=UTF-8
      Location: http://www.google.com.sg/?gfe_rd=cr&ei=PlqJVLCREovW8gfF0oG4CQ
      Content-Length: 262
      Date: Thu, 11 Dec 2014 08:47:58 GMT
      Server: GFE/2.0
      Alternate-Protocol: 80:quic,p=0.02

      <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
      <TITLE>302 Moved</TITLE></HEAD><BODY>
      <H1>302 Moved</H1>
      The document has moved
      <A HREF="http://www.google.com.sg/?gfe_rd=cr&ei=PlqJVLCREovW8gfF0oG4CQ">here</A>.
      </BODY></HTML>

      关闭 socket
      当我们不想再次请求服务器数据时，可以将该 socket 关闭，结束这次通信：
      s.close()

      小结
      上面我们学到了如何：
          创建 socket
          连接到远程服务器
          发送数据
          接收数据
          关闭 socket
      当我们打开www.google.com 时，浏览器所做的就是这些，知道这些是非常有意义的。在 socket 中具有这种行为特征的被称为CLIENT，客户端主要是连接远程系统获取数据。
      socket 中另一种行为称为SERVER，服务器使用 socket 来接收连接以及提供数据，和客户端正好相反。所以 www.google.com 是服务器，你的浏览器是客户端，或者更准确地说，www.google.com 是 HTTP 服务器，你的浏览器是 HTTP 客户端。
      那么上面介绍了客户端的编程，现在轮到服务器端如果使用 socket 了。

二、服务器端编程
服务器端主要做以下工作：
    打开 socket
    绑定到特定的地址以及端口上
    监听连接
    建立连接
    接收/发送数据
上面已经介绍了如何创建 socket 了，下面一步是绑定。

绑定socket
函数 bind 可以用来将 socket 绑定到特定的地址和端口上，它需要一个 sockaddr_in 结构作为参数：

import socket
import sys
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
  s.bind((HOST, PORT))
except socket.error , msg:
  print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
  sys.exit()
   
print 'Socket bind complete'
绑定完成之后，接下来就是监听连接了。

监听连接
函数 listen 可以将 socket 置于监听模式：

s.listen(10)
print 'Socket now listening'

该函数带有一个参数称为 backlog，用来控制连接的个数。如果设为 10，那么有 10 个连接正在等待处理，此时第 11 个请求过来时将会被拒绝。

接收连接

当有客户端向服务器发送连接请求时，服务器会接收连接：

#wait to accept a connection - blocking call
conn, addr = s.accept()
 
#display client information
print 'Connected with ' + addr[0] + ':' + str(addr[1])

运行该程序的，输出结果如下：

$ python server.py
Socket created
Socket bind complete
Socket now listening

此时，该程序在 8888 端口上等待请求的到来。不要关掉这个程序，让它一直运行，现在客户端可以通过该端口连接到 socket。我们用 telnet 客户端来测试，打开一个终端，输入 telnet localhost 8888：

$ telnet localhost 8888
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Connection closed by foreign host.

这时服务端输出会显示：

$ python server.py
Socket created
Socket bind complete
Socket now listening
Connected with 127.0.0.1:59954

我们观察到客户端已经连接上服务器了。在建立连接之后，我们可以用来与客户端进行通信。下面例子演示的是，服务器建立连接之后，接收客户端发送来的数据，并立即将数据发送回去，下面是完整的服务端程序：

import socket
import sys
 
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
  s.bind((HOST, PORT))
except socket.error , msg:
  print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
  sys.exit()
   
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
#wait to accept a connection - blocking call
conn, addr = s.accept()
 
print 'Connected with ' + addr[0] + ':' + str(addr[1])
 
#now keep talking with the client
data = conn.recv(1024)
conn.sendall(data)
 
conn.close()
s.close()

在一个终端中运行这个程序，打开另一个终端，使用 telnet 连接服务器，随便输入字符串，你会看到：

$ telnet localhost 8888
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
happy
happy
Connection closed by foreign host.

客户端（telnet）接收了服务器的响应。

我们在完成一次响应之后服务器立即断开了连接，而像www.google.com 这样的服务器总是一直等待接收连接的。我们需要将上面的服务器程序改造成一直运行，最简单的办法是将accept 放到一个循环中，那么就可以一直接收连接了。

保持服务

我们可以将代码改成这样让服务器一直工作：

import socket
import sys
 
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
  s.bind((HOST, PORT))
except socket.error , msg:
  print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
  sys.exit()
   
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
#now keep talking with the client
while 1:
  #wait to accept a connection - blocking call
  conn, addr = s.accept()
  print 'Connected with ' + addr[0] + ':' + str(addr[1])
   
  data = conn.recv(1024)
  reply = 'OK...' + data
  if not data: 
    break
   
  conn.sendall(reply)
 
conn.close()
s.close()

现在在一个终端下运行上面的服务器程序，再开启三个终端，分别用 telnet 去连接，如果一个终端连接之后不输入数据其他终端是没办法进行连接的，而且每个终端只能服务一次就断开连接。这从代码上也是可以看出来的。

这显然也不是我们想要的，我们希望多个客户端可以随时建立连接，而且每个客户端可以跟服务器进行多次通信，这该怎么修改呢？

处理连接

为了处理每个连接，我们需要将处理的程序与主程序的接收连接分开。一种方法可以使用线程来实现，主服务程序接收连接，创建一个线程来处理该连接的通信，然后服务器回到接收其他连接的逻辑上来。

import socket
import sys
from thread import *
 
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
  s.bind((HOST, PORT))
except socket.error , msg:
  print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
  sys.exit()
   
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
  #Sending message to connected client
  conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
   
  #infinite loop so that function do not terminate and thread do not end.
  while True:
     
    #Receiving from client
    data = conn.recv(1024)
    reply = 'OK...' + data
    if not data: 
      break
   
    conn.sendall(reply)
   
  #came out of loop
  conn.close()
 
#now keep talking with the client
while 1:
  #wait to accept a connection - blocking call
  conn, addr = s.accept()
  print 'Connected with ' + addr[0] + ':' + str(addr[1])
   
  #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
  start_new_thread(clientthread ,(conn,))
 
s.close()

再次运行上面的程序，打开三个终端来与主服务器建立 telnet 连接，这时候三个客户端可以随时接入，而且每个客户端可以与主服务器进行多次通信。

telnet 终端下可能输出如下：

$ telnet localhost 8888
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Welcome to the server. Type something and hit enter
hi
OK...hi
asd
OK...asd
cv
OK...cv

要结束 telnet 的连接，按下 Ctrl-] 键，再输入 close 命令。

服务器终端的输出可能是这样的：

$ python server.py
Socket created
Socket bind complete
Socket now listening
Connected with 127.0.0.1:60730
Connected with 127.0.0.1:60731

