recv_factory = {}


class RecvMsg:
    def Initialization() -> bool: pass
    def Recv() -> bytes: pass
    def DeInitialization(): pass


def CreateRecv(type, args):
    print(recv_factory)
    res = recv_factory[type](args)
    if res.Initialization() == True:
        return res
    return None
