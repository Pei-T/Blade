from blade.api_recv import RecvMsg, factory_recv
import tushare as ts
import time


tushare_token = 'db11129040085642ce635dd20923d2aa6bc5bc04dd07b42afc271ad4'

class RecvTushareOnlien(RecvMsg):
    def __init__(self, code) -> None:
        self.code = code

    def Initialization(self) -> bool:
        return True

    def Recv(self) -> bytes:
        time.sleep(0.5)
        res = ts.get_realtime_quotes(self.code)
        return res.loc[0]

    def DeInitialization(self):
        pass


factory_recv['tushare_online'] = RecvTushareOnlien

