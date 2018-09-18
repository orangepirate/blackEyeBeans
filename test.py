#from urllib.request import urlopen
#from parse_scanresult import ParseScanResult
#from get_webinfo import GetWebInfo
#from get_domains import GetDomains
from scan_single import *
#import time
ip = '192.168.1.101'
import os
import sys

scanOs(scan_os,ip)


'''
f = open('112.74.133.190(nmap -oX - -sV {}).xml','r').read()
test = ParseScanResult()
test.parseScanResultXml(f)
print(vars(test))
'''
'''
def scan_single(ip):
    print('start scan {}'.format(ip))
    time.sleep(1)
    print('end scan {}'.format(ip))

'''

'''
ip = '112.74.133.190'
webinfo = GetWebInfo()
webinfo.getWebInfo80(ip)
print(vars(webinfo))
if '112' in vars(webinfo)['ip']:
    print('true')
else:
    print('no')
'''

'''
domains = GetDomains()
domains.get_domain_AiZhan(ip)
print(vars(domains))
'''

'''
#ret = urlopen('http://{}'.format(ip)).read().decode('utf8')
targetIp = '123.58.182.251.xml'
f = open('123.58.182.251.xml','r').read()
parsedxml = ParseScanResult()
parsedxml.parseScanResultXml(targetIp,f)
for i in range(len(vars(parsedxml)['dev_ports'])):
    if vars(parsedxml)['dev_ports'][i] == '53' and vars(parsedxml)['dev_portsstate'][i] == 'open':
        getWebInfo(vars(parsedxml)['dev_services'][i],targetIp)
    #print(vars(parsedxml)['dev_ports'])
    #print(vars(parsedxml)['dev_portsstate'])
    #print(vars(parsedxml)['dev_services'])
    #print(vars(parsedxml)['dev_cpes'])
print(vars(parsedxml))

'''