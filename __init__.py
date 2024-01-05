import blade.api_recv
import blade.api_send
import blade.recv_normal
import blade.recv_tushare
import blade.send_normal
import blade.send_server_jiang
__all__ = ['CreateRecvMessage']

def CreateRecvMessage(type, args):
    return blade.api_recv.CreateRecv(type, args)

def CreateSendMessage(type, args):
    return blade.api_send.CreateSend(type, args)