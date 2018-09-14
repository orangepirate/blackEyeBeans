import os
from IPy import IP
from update_database import MySqlCommand
from check_modules import checkModules
from parse_scanresult import ParseScanResult
from get_domains import GetDomains

commonPrefix = '[++]'
essentialPrefix = '[##]'
midfix = '[--]'
portfix = '[port]'

scaned_ip_list = []
error_ip_list = []
total_ip_list = []

scan_os_service = 'nmap -oX - -sV {}'

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


def scan_single(command, targetIp='127.0.0.1'):
    print('scanning target ip : {}\n'.format(targetIp))
    scan_command = command.format(targetIp)
    result = os.popen(scan_command).read()
    # save result
    #save(result,targetIp)
    # parse scan result
    try:
        parsedResult = ParseScanResult()
        parsedResult.parseScanResultXml(targetIp,result)
    except Exception as e:
        print(e)
    # write domains to parseResult
    try:
        domains = GetDomains()
        domains.get_domain_AiZhan(targetIp)
        vars(parsedResult)['dev_domains'] = vars(domains)['domains']
    except Exception as e:
        print(e)
    try:
        save2Database(vars(parsedResult), 'devs')
    except Exception as e:
        error_ip_list.append(targetIp)



def parseIps(s):
    ip_list = []
    for ip in IP(s):
        ip_list.append(ip)
    return ip_list

if __name__ == '__main__':
    ips = IP('112.74.133.190')
    # ips = '220.181.76.83'
    # parse ips into ip_list
    ip_list = parseIps(ips)
    # scan target according to ip_list
    for ip in ip_list:
        scan_single(scan_os_service,ip)