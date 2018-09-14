from urllib.request import urlopen
from bs4 import BeautifulSoup

class GetDomains(object):
    def __init__(self):
        self.domains = []
    def get_domain_AiZhan(self,ip):
        ret = urlopen('http://dns.aizhan.com/{}/'.format(ip)).read().decode('utf8')
        soup = BeautifulSoup(ret,'lxml')
        dns_content = soup.find(class_='dns-content')
        tr = dns_content.find_all('tr')
        for i in range(1,len(tr)):
            a = tr[i].find('a').get_text()
            self.domains.append(a)
    def get_domain_YouGetSignal(self,ip):
        return


'''

def getPage(ip,page):
    ret = requests.get(yellow_page_aizhan.format(ip,page))
    print(ret)
    return ret

def getMaxPage(ip):
    ret = getPage(ip,1)
    json_data = {}
    json_data = ret.json()
    maxCount = json_data[u'conut']
    print(maxCount)
'''