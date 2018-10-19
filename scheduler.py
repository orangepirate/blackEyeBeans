import threading
from multiprocessing import Process
import os
from IPy import IP
from scanner import scan_single

def parseIps(s):
    ip_list = []
    for ip in IP(s):
        ip_list.append(ip)
    return ip_list

if __name__=="__main__":
    iplist = parseIps('202.12.132.0/30')
    print('parent process {}.'.format(os.getpid()))
    for i in range(len(iplist)):
        p = Process(target=scan_single,args=(iplist[i]))
        p.start()

print('process end')
