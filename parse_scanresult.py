from bs4 import BeautifulSoup
import time
import lxml
import re
from datetime import datetime


def parseScanOsResultXml(xml):
    text = xml.splitlines()
    ret = {}
    for one in text:
        if 'MAC Address:' in one:
            ret['dev_mac'] = one
        # if 'OS CPE:' in one:
        #    self.dev_oscpe = one
        if 'OS details:' in one:
            ret['dev_os'] = one
        if 'Aggressive OS guesses:' in one:
            ret['dev_os'] = one
        if 'Too many fingerprints match this host to give specific OS details' in one:
            ret['dev_os'] = 'unkown'
    return ret


def parseScanServiceResultXml(xml):
    dev_state = 'null'
    dev_ports = []
    dev_portsstate = []
    dev_services = []
    dev_products = []
    dev_cpes = []
    dev_extrainfos = []
    ret = {}
    # self.update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    txt = xml.replace('<?xml version="1.0" encoding="UTF-8"?>', '<html>').replace('\n', '')
    txt = txt + '</html>'
    soup = BeautifulSoup(txt, 'lxml')
    try:
        dev_ip = soup.find('address')['addr']
    except Exception as e:
        dev_ip = e
    try:
        dev_state = soup.find('status')['state']
    except:
        dev_state = 'unknown'
    try:
        portsInfo = soup.find('ports').find_all('port')
        for one in portsInfo:
            # self.dev_ports.append(one.attrs['portid'])
            dev_ports.append(one.attrs['portid'])
            state = one.find('state')
            service = one.find('service')
            dev_portsstate.append(state.attrs['state'])
            dev_services.append(service.attrs['name'])
            try:
                dev_products.append(service.attrs['product'] + ':' + service.attrs['version'])
            except:
                dev_products.append('unknown')
            try:
                dev_extrainfos.append(service.attrs['extrainfo'])
            except:
                dev_extrainfos.append('null')
            try:
                dev_cpes.append(one.find('cpe').get_text())
            except:
                dev_cpes.append('null')
        ret['dev_ip'] = dev_ip
        ret['dev_state'] = dev_state
        ret['dev_products'] = dev_products
        ret['dev_extrainfos'] = dev_extrainfos
        ret['dev_cpes'] = dev_cpes
        ret['dev_portsstate'] = dev_portsstate
        ret['dev_services'] = dev_services
        ret['dev_ports'] = dev_ports
        return ret
    except Exception as e:
        return
'''
class ParseScanResult(object):
    # initialization
    def __init__(self):
        self.dev_ip = 'null'
        self.update_time = ''
    # parse os scan result
    def parseScanOsResult(self,xml):
        text = xml.splitlines()
        for one in text:
            if 'MAC Address:' in one:
                self.dev_mac = one
            #if 'OS CPE:' in one:
            #    self.dev_oscpe = one
            if 'OS details:' in one:
                self.dev_os = one
            if 'Aggressive OS guesses:' in one:
                self.dev_os = one
            if 'Too many fingerprints match this host to give specific OS details' in one:
                self.dev_os = 'unkown'
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
        #self.update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
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

'''
