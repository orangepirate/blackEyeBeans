import urllib,requests,os,sys,json

yellow_page_aizhan = 'https://dns.aizhan.com/{}/'

'''
http://bgp.he.net/，IP地址查对应机房：IP地址在 bgp.he.net 直接能查到IP所属机房或运营商的AS号。 
http://cn.bing.com/search?q=ip%3A220.181.111.85
http://dns.aizhan.com/?q=www.baidu.com
http://domains.yougetsignal.com/domains.php?remoteAddress=lcx.cc
http://i.links.cn/sameip/61.164.241.103.html
http://ip.robtex.com/
http://rootkit.net.cn/index.aspx，查c段的话：http://c.wlan.im/
http://sameip.org/
http://tool.114la.com/sameip/
http://tool.chinaz.com/Same/
http://www.114best.com/ip/114.aspx?w=61.164.241.103
http://www.yougetsignal.com/tools/web-sites-on-web-server/，菜刀里面的。
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