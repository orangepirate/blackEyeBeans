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
    #iplist = parseIps('1.1.8.68/30')
    string = '{}.{}.{}.{}'
    for k in range(1,255):
        for l in range(1,255):
            for m in range(1,255):
                iplist = parseIps('{}.{}.{}.0/24'.format(k,l,m))
                #for i in range(len(iplist)):
                #    print(iplist[i])
                #iplist = parseIps('90.127.170.227')
                #iplist = parseIps('192.168.1.105')
                #print('parent process {}.'.format(os.getpid()))
                for i in range(len(iplist)):
                    #print(iplist[i])
                    scan_single(iplist[i])
    '''
        p = Process(target=scan_single,args=(iplist[i]))
        p.start()
    '''
print('process end')
