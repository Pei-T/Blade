from blade.api_send import SendMsg, factory_send
class SendPrint(SendMsg):
    def __init__(self, args): pass
    def Initialization(self) -> bool: pass

    def Send(self, msg):
        print(msg)
    def DeInitialization(): pass

factory_send ['print'] = SendPrint