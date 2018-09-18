from bs4 import BeautifulSoup
import time
import lxml
import re
from datetime import datetime


class ParseScanResult(object):
    # initialization
    def __init__(self):
        self.dev_ip = 'null'
    # parse os scan result
    def parseScanOsResult(self,xml):
        text = xml.splitlines()
        for one in text:
            if 'MAC Address:' in one:
                self.dev_mac = one
            if 'OS CPE:' in one:
                self.dev_oscpe = one
            if 'OS details:' in one:
                self.dev_os = one
        return
    # parse service scan result xml
    def parseScanServiceResultXml(self,xml):
        self.dev_state = 'null'
        self.dev_ports = []
        self.dev_portsstate = []
        self.dev_services = []
        self.dev_products = []
        self.dev_cpes = []
        self.dev_extrainfos = []
        self.update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        txt = xml.replace('<?xml version="1.0" encoding="UTF-8"?>', '<html>').replace('\n', '')
        txt = txt + '</html>'
        soup = BeautifulSoup(txt,'lxml')
        try:
            self.dev_ip = soup.find('address')['addr']
        except Exception as e:
            dev_ip = e
        try:
            self.dev_state = soup.find('status')['state']
        except:
            self.dev_state = 'unknown'

        try:
            portsInfo = soup.find('ports').find_all('port')
            for one in portsInfo:
                #self.dev_ports.append(one.attrs['portid'])
                self.dev_ports.append(one.attrs['portid'])
                state = one.find('state')
                service = one.find('service')
                self.dev_portsstate.append(state.attrs['state'])
                self.dev_services.append(service.attrs['name'])
                try:
                    self.dev_products.append(service.attrs['product']+':'+service.attrs['version'])
                except:
                    self.dev_products.append('unknown')
                try:
                    self.dev_extrainfos.append(service.attrs['extrainfo'])
                except:
                    self.dev_extrainfos.append('null')
                try:
                    self.dev_cpes.append(one.find('cpe').get_text())
                except:
                    self.dev_cpes.append('null')
        except Exception as e:
            return


