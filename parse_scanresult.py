from bs4 import BeautifulSoup
import time
import lxml
import time
from datetime import datetime


class ParseScanResult(object):
    # initialization
    def __init__(self):
        self.dev_ip = 'null'
        self.dev_domains = []
        self.dev_state = 'null'
        self.dev_ports = []
        self.dev_portsstate = []
        self.dev_cpes = []
        self.dev_services = []
        self.dev_extrainfos = []
        self.update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # parse nmap scan result xml
    def parseScanResultXml(self,targetIp,xml):

        txt = xml.replace('<?xml version="1.0" encoding="UTF-8"?>', '<html>').replace('\n', '')
        txt = txt + '</html>'
        soup = BeautifulSoup(txt,'lxml')
        self.dev_ip = targetIp

        '''
        try:
            self.dev_ip = soup.find('address')['addr']
        except:
            self.dev_ip = 'unknown'
        '''
        #if(soup.find('hosts')['up']=='0'):
        #    return 404
        try:
            self.dev_state = soup.find('status')['state']
        except:
            self.dev_state = 'unknown'

        try:
            portsInfo = soup.find_all('port')
            for one in portsInfo:
                #print(one)
                port = one.attrs['portid']
                portstate = one.find('state').attrs['state']
                portservice = one.find('service').attrs['name']
                cpe = str(one.find('cpe')).replace('<cpe>','').replace('</cpe>','')
                self.dev_ports.append(port)
                self.dev_portsstate.append(portstate)
                self.dev_services.append(portservice)
                self.dev_cpes.append(cpe)
                try:
                    extrainfo = one.find('service').attrs['extrainfo']
                    self.dev_extrainfos.append(extrainfo)
                except:
                    continue
        except:
            return 404

