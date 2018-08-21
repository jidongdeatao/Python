
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
