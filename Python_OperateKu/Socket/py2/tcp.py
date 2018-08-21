# -*- coding: utf-8 -*-
# TCP 服务器
import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip, bind_port)

# 这是客户处理线程
def handle_client(client_socket):
    # 打印出客户端发送得到内容
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request
    # 返还一个数据包
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = server.accept()
    print "[*] Accept connection from: %s:%d" % (addr[0], addr[1])
    # 挂起客户端线程并处理传入的数据
    client_handler = threading.Thread(target=handle_client, args=(client,))
client_handler.start()






# -*- coding: utf-8 -*-
# TCP 客户端
import socket

target_host = 'www.baidu.com'
target_port = 80

# 建立一个 socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接客户端
client.connect((target_host, target_port))
# 发送一些数据
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")
# 接收一些数据
response = client.recv(4096)
print response






#下面是另外一个版本的服务端与客户端端交互

#-*- coding: utf-8 -*-
#服务端
from socket import *
from time import ctime
from time import localtime
import time

HOST=''
PORT=8888 #设置侦听端口
BUFSIZ=1024
ADDR=(HOST, PORT)
sock=socket(AF_INET, SOCK_STREAM)

sock.bind(ADDR)

sock.listen(5)
#设置退出条件
STOP_CHAT=False
while not STOP_CHAT:
  print('等待接入，侦听端口:%d' % (PORT))
  tcpClientSock, addr=sock.accept()
  print('接受连接，客户端地址：',addr)
  while True:
    try:
      data=tcpClientSock.recv(BUFSIZ)
    except:
      #print(e)
      tcpClientSock.close()
      break
    if not data:
      break
    #python3使用bytes，所以要进行编码
    #s='%s发送给我的信息是:[%s] %s' %(addr[0],ctime(), data.decode('utf8'))
    #对日期进行一下格式化
    ISOTIMEFORMAT='%Y-%m-%d %X'
    stime=time.strftime(ISOTIMEFORMAT, localtime())
    s='%s发送给我的信息是:%s' %(addr[0],data.decode('utf8'))
    tcpClientSock.send(s.encode('utf8'))
    print([stime], ':', data.decode('utf8'))
    #如果输入quit(忽略大小写),则程序退出
    STOP_CHAT=(data.decode('utf8').upper()=="QUIT")
    if STOP_CHAT:
      break
    tcpClientSock.close()
sock.close()


# -*- coding: utf-8 -*-
#客户端
from socket import *
class TcpClient:
    HOST = '127.0.0.1'
    PORT = 8888
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)

        while True:
            data = input('>')
            if not data:
                break
            self.client.send(data.encode('utf8'))
            data = self.client.recv(self.BUFSIZ)
            if not data:
                break
            print(data.decode('utf8'))


if __name__ == '__main__':
    client = TcpClient()
