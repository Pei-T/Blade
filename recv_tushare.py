from blade.recv_api import RecvMsg, recv_factory
import tushare as ts
import time


tushare_token = 'db11129040085642ce635dd20923d2aa6bc5bc04dd07b42afc271ad4'

class RecvTushareOnlien(RecvMsg):
    def __init__(self, code) -> None:
        self.code = code

    def Initialization(self) -> bool:
        return True

    def Recv(self) -> bytes:
        time.sleep(1)
        res = ts.get_realtime_quotes(self.code)
        return res.loc[0]

    def DeInitialization(self):
        pass


recv_factory['tushare_online'] = RecvTushareOnlien

