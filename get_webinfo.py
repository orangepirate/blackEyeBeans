from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
if __name__ == "__main__":
    #以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://www.csdn.net/'
    head = {}
    #写入User Agent信息
    
 #创建Request对象
    req = request.Request(url, headers=head)
    #传入创建好的Request对象
    response = request.urlopen(req)
    #读取响应信息并解码
    html = response.read().decode('utf-8')
    #打印信息
    print(html)
'''
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'

class GetWebInfo(object):
    def __init__(self):
        self.ip = ''
        self.title = ''
        self.footer = ''

    def getWebInfo80(self,ip):
        self.ip = ip
        ret = urlopen('http://{}'.format(ip)).read().decode('utf8')
        soup = BeautifulSoup(ret,'lxml')
        try:
            self.title = soup.find('title').get_text()
        except:
            self.title = 'null'
            #self.footer = soup.find(class_='footer').get_text().strip().replace('\r','').replace('\n','')
