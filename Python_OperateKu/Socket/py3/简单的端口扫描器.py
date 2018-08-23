#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from socket import *

# port_scan.py <host> <start_port>-<end_port>
host = sys.argv[1]
portstrs = sys.argv[2].split('-')

start_port = int(portstrs[0])
end_port = int(portstrs[1])

target_ip = gethostbyname(host)
opened_ports = []

for port in range(start_port, end_port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        opened_ports.append(port)


print("Opened ports:")

for i in opened_ports:
    print(i)

    
#上面的程序要考虑加入多线程，不然太慢
#加入多线程thread
#这种多线程还是需要改进的，如使用threading 或multithreading
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import thread
from socket import *

def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        lock.acquire()
        print "Opened Port:",port
        lock.release()


if __name__=='__main__':
    # portscan.py <host> <start_port>-<end_port>
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')

    start_port = int(portstrs[0])
    end_port = int(portstrs[1])

    target_ip = gethostbyname(host)

    lock = thread.allocate_lock()

    for port in range(start_port, end_port):
        thread.start_new_thread(tcp_test, (port,))
