import threading
from multiprocessing import Process
import os
from scan_single import parseIps

from test import scan_single




if __name__=="__main__":
    iplist = parseIps('192.168.1.0/29')
    print('parent process {}.'.format(os.getpid()))
    for i in range(len(iplist)):
        p = Process(target=scan_single,args=(iplist[i]))
        print('process will starts.')
        p.start()

print('process end')
