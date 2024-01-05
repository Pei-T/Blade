# package
import zmq
from blade.api_recv import RecvMsg, factory_recv


context = zmq.Context()


class RecvZmq(RecvMsg):
    def __init__(self, addr) -> None:
        self.addr = addr
        self.socket = context.socket(zmq.SUB)

    def Initialization(self) -> bool:
        self.socket.subscribe('')
        self.socket.connect(self.addr)
        return True

    def Recv(self) -> bytes:
        while True:
            ret = self.socket.recv()
            if ret is None:
                continue
            return ret
    def DeInitialization(self):
        self.socket.close()


factory_recv['zmq'] = RecvZmq


class RecvInput(RecvMsg):
    def __init__(self, args):
        self.args = args

    def Initialization(self) -> bool:
        return True

    def Recv(self) -> bytes:
        data = input()
        return data.encode('utf-8')


factory_recv['input'] = RecvInput
