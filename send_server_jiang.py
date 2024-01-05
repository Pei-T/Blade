from blade.api_send import SendMsg, factory_send
import urllib.parse
import urllib.request



class SendServerJiang(SendMsg):
    def __init__(self, args): pass
    def Initialization(self) -> bool: pass
    def Send(self, msg): 
        postdata = urllib.parse.urlencode({'text': msg['head'], 'desp': msg['body']}).encode('utf-8')
        url = f'https://sctapi.ftqq.com/SCT224501TFIQqolnYZ1oDi3DNv1dLgGvu.send'
        req = urllib.request.Request(url, data=postdata, method='POST')
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8')
        return result
    def DeInitialization(self): pass


factory_send['server_jiang'] = SendServerJiang
