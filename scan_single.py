import os,sys,threading,time
from IPy import IP
from multiprocessing import Process,Queue
# my own module
from update_database import MySqlCommand
from check_modules import checkModules
from parse_scanresult import ParseScanResult
from get_domains import GetDomains
from get_webinfo import GetWebInfo

parsedResult = ParseScanResult()
threadLock = threading.Lock()
scan = 0

#scan_port = 'nmap -oX - -Pn {}'
scan_service = 'nmap -oX - -sV {}'
scan_os = 'sudo nmap -O {}'

def get_privilege():
    if os.getuid():
        args = [sys.executable]+ sys.argv
        os.execlp('su','su','-c',''.join(args))
    print('Running at root privilege. Your euid is', os.geteuid())

def save2XML(text, targetIp):
    f = open('{}.xml'.format(targetIp),'a')
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
            parsedResult.parseScanServiceResultXml(result)
            threadLock.release()
        if '-O' in command:
            threadLock.acquire()
            parsedResult.parseScanOsResult(result)
            threadLock.release()
        return parsedResult
    except Exception as e:
        print(e)
    return

def parseIps(s):
    ip_list = []
    for ip in IP(s):
        ip_list.append(ip)
    return ip_list

if __name__ == '__main__':
    start = time.time()
    if os.getuid():
        print('please run this python script with root privilege... returns now...')
        exit(0)
    # get target ip
    targetIp = '112.74.133.190'
    update_time = update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    parsedResult.update_time = update_time
    # scan target with 2 threads : service and os
    threads = []
    threadService = threading.Thread(target = scanTarget,args = (scan_service,targetIp))
    threads.append(threadService)
    threadOs = threading.Thread(target=scanTarget,args=(scan_os,targetIp))
    threads.append(threadOs)
    for thread in threads:
        thread.setDaemon(True)
        thread.start()
    for thread in threads:
        thread.join()
    # store result if success, return without storing if scan equals 1
    if scan == 0:
        # write parsedInfo into database
        try:
            save2Database(vars(parsedResult), 'devs')
        except Exception as e:
            print(e)
        end = time.time()
        print('scan target {} success....\n {}'.format(targetIp,vars(parsedResult)))
        print('scan takes {} seconds.'.format(end-start))
        exit()
    else:
        print('something went wrong or the host is down, exit now...')
        exit()
