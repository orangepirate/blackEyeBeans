
class checkModules(object):
    # initialization
    def __init__(self):
        self.url = ''
        self.command = 'pip install {}'

    # check IPy
    def checkIpy(self):
        return
    # check fake-useragent
    def checkFakeUserAgent(self):
        return
    def checkNmap(self,errmsg):
        if 'nmap: not found' in errmsg:
            return