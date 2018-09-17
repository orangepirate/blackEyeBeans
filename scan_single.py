import os,sys
from IPy import IP
from update_database import MySqlCommand
from check_modules import checkModules
from parse_scanresult import ParseScanResult
from get_domains import GetDomains
from get_webinfo import GetWebInfo

commonPrefix = '[++]'
essentialPrefix = '[##]'
midfix = '[--]'
portfix = '[port]'

scaned_ip_list = []
error_ip_list = []
total_ip_list = []

scan_port = 'nmap -oX - -Pn {}'
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


def scanService(command, targetIp='127.0.0.1'):
    print('scanning target {} services now...'.format(targetIp))
    scan_command = command.format(targetIp)
    result = os.popen(scan_command).read()
    # if scan target is down, return without parsing scan result
    if('1 IP address (0 hosts up)') in result:
        print('host {} is down, returns now.'.format(targetIp))
        return
    # parse scan result
    try:
        parsedResult = ParseScanResult()
        parsedResult.parseScanResultXml(result)
    except Exception as e:
        print(e)
    # save data into database
    try:
        save2Database(vars(parsedResult), 'devs')
    except Exception as e:
        error_ip_list.append(targetIp)

def scanOs(command,targetIp='127.0.0.1'):
    print('scanning target {} os now...'.format(targetIp))
    scan_command = command.format(targetIp)
    result = os.popen(scan_command,).read()

    print(result)



def parseIps(s):
    ip_list = []
    for ip in IP(s):
        ip_list.append(ip)
    return ip_list

if __name__ == '__main__':
    ips = IP('123.58.182.240/29')
    # ips = '220.181.76.83'
    # parse ips into ip_list
    ip_list = parseIps(ips)
    # scan target according to ip_list
    for ip in ip_list:
        scanService(scan_service,ip)
        scanOs(scan_os,ip)