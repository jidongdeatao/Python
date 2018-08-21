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
