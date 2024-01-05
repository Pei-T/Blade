factory_send = {}


class SendMsg:
    def Initialization() -> bool: pass
    def Send() : pass
    def DeInitialization(): pass


def CreateSend(type, args):
    res = factory_send[type](args)
    return res
