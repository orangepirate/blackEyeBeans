from urllib.request import *
from parse_scanresult import ParseScanResult
from get_webinfo import getWebInfo

ip = '112.74.133.190'

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
