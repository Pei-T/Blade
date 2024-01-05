factory_recv = {}


class RecvMsg:
    def Initialization() -> bool: pass
    def Recv() : pass
    def DeInitialization(): pass


def CreateRecv(type, args):
    res = factory_recv[type](args)
    return res
