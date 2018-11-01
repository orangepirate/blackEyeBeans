import os,sys,threading,time
from multiprocessing import Process,Queue
# my own module
from update_database import MySqlCommand
#from check_modules import checkModules
from parse_scanresult import *
from get_domains import GetDomains
from get_webinfo import GetWebInfo

threadLock = threading.Lock()
scan = 0

#scan_port = 'nmap -oX - -Pn {}'
scan_service = 'nmap -oX - -sV {}'
scan_os = 'sudo nmap -O {}'

class MyThread(threading.Thread):
    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args
    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None

def get_privilege():
    if os.getuid():
        args = [sys.executable]+ sys.argv
        os.execlp('su','su','-c',''.join(args))
    print('Running at root privilege. Your euid is', os.geteuid())

def save2XML(text, targetIp):
    f = open('/tempdata/{}.xml'.format(targetIp),'a')
    f.write(text)
    f.close()

def save2Database(mydict,table):
    try:
        mySqlCommand = MySqlCommand()
        mySqlCommand.connectMySql()
    except Exception as e:
        print(e)
    try:
        mySqlCommand.insertData(mydict,table)
    except Exception as e:
        print(e)

def scanTarget(command, targetIp='127.0.0.1'):
    if '-sV' in command:
        print('scanning target {} services now ...'.format(targetIp))
    if '-O' in command:
        print('scanning target {} os now ...'.format(targetIp))
    scan_command = command.format(targetIp)
    try:
        result = os.popen(scan_command).read()
    except Exception as e:
        print(e)
    # if scan target is down, return without parsing scan result
    if('1 IP address (0 hosts up)') in result:
        print('host {} is down, returns now.'.format(targetIp))
        scan = 1
        return
    # parse service scan result
    try:
        if '-sV' in command:
            threadLock.acquire()
            ret = parseScanServiceResultXml(result)
            threadLock.release()
        if '-O' in command:
            threadLock.acquire()
            ret = parseScanOsResultXml(result)
            threadLock.release()
        return ret
    except Exception as e:
        print(e)
        return

def scan_single(targetIp='101.200.195.98'):
    start = time.time()
    result = {}
    if os.getuid():
        print('please run this python script with root privilege... returns now...')
        exit(0)
    update_time = update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    result['update_time'] = update_time
    # scan target with 2 threads : service and os
    threads = []
    threadService = MyThread(func = scanTarget,args = (scan_service,targetIp))
    threads.append(threadService)
    threadOs = MyThread(func = scanTarget,args=(scan_os,targetIp))
    threads.append(threadOs)
    for thread in threads:
        thread.setDaemon(True)
        thread.start()
    for t in threads:
        t.join()
        if t.get_result():
            result.update(t.get_result())
            # store result if success, return without storing if scan equals 1
            # write parsedInfo into database
        else:
            print('something went wrong or the host is down, exit now...')
            return
    try:
        save2Database(result, 'devs')
    except Exception as e:
        print(e)
    end = time.time()
    print('scan takes {} seconds.'.format(end - start))
    return

