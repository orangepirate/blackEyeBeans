import nmap
import re
import datetime
from update_database import MySqlCommand
from scan_single import save2XML

commonPrefix = '[++]'
essentialPrefix = '[##]'
midfix = '[--]'
portfix = '[port]'

#scanIp = input('input the target ip address: ')
scanIp = '112.74.133.190'
targets = {}

nm = nmap.PortScanner()
ret = nm.scan(scanIp)
commandLine = ret['nmap']['command_line']
scanStats = ret['nmap']['scanstats']
scanResult = ret['scan']
scanTime = scanStats['timestr']

f = open('{}.xml'.format(scanIp),'a')
f.write(str(ret))
f.close()

print('commandline:{}'.format(commandLine))
print('scanStats:{}'.format(scanStats))
print('scanresult:{}'.format(scanResult))

def parseTargetResu(targetResult):
    retDic = {}
    domain = ''
    hostName = targetResult['hostnames'][0]['name']
    hostType = targetResult['hostnames'][0]['type']
    state = targetResult['status']['state']
    vendor = targetResult['vendor']
    #portsInfo = targetResult['tcp']
    ports = []
    portServices = []
    portCpes = []
    extraInfo = []
    if 'tcp' in targetResult.keys():
        portsInfo = targetResult['tcp']
        for port,portInfo in portsInfo.items():
            ports.append(port)
            portServices.append(portInfo['name'])
            portCpes.append(portInfo['cpe'])
            extraInfo.append(portInfo['extrainfo'])
    #print('{}state:{}'.format(midfix,state))
    #print('{}vendor:{}'.format(midfix,vendor))
    #print('{}:{} {} {}'.format(portfix,ports,portProtocals, portCpes))
    names = ['dev_domain','dev_hostname','dev_hosttype','dev_vendor','dev_state','dev_ports','dev_services','dev_cpes','dev_extrainfo']
    values = [domain,hostName,hostType,vendor,state,ports,portServices,portCpes,extraInfo]
    for i in range(len(names)):
        retDic.update({names[i]:values[i]})
    return retDic
'''
#if __name__ == '__main__':

for targetIp,targetResult in scanResult.items():
    targets[targetIp] = targetResult
    print('targetIp：{}'.format(targetIp))
    #print('{}:{}'.format(target,result))
    targetDict = parseTargetResu(targetResult)
    targetDict.update({'update_time':datetime.datetime.now()})
    targetDict.update({'dev_ip':targetIp})
    # insert target info into database
    try:
        mysqlCommand = MySqlCommand()
        mysqlCommand.connectMySql()
    except Exception as e:
        print(e)
    try:
        response = mysqlCommand.insertData(targetDict)
    except Exception as e:
        print(e)

print('\n{}'.format(scanResult))

'''