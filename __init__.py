import blade.recv_api
import blade.recv_normal

__all__ = ['CreateRecvMessage']

def CreateRecvMessage(type, args):
    return blade.recv_api.CreateRecv(type, args)
