recv_factory = {}


class RecvMsg:
    def Initialization() -> bool: pass
    def Recv() : pass
    def DeInitialization(): pass


def CreateRecv(type, args):
    res = recv_factory[type](args)
    if res.Initialization() == True:
        return res
    return None
