from blade.recv_api import RecvMsg, recv_factory
import tushare as ts
from datetime import datetime

tushare_token = 'db11129040085642ce635dd20923d2aa6bc5bc04dd07b42afc271ad4'
# df = ts.get_realtime_quotes('600203')  # Single stock symbol
# df[['code', 'name', 'price', 'bid', 'ask', 'volume', 'amount', 'time']]
# print(df)

# current_date_and_time = datetime.now()

class RecvTushareOnlien(RecvMsg):
    def __init__(self, code) -> None:
        self.code = code
        self.last_time = datetime.now()

    def Initialization(self) -> bool:
        return True

    def Recv(self) -> bytes:
        res = ts.get_realtime_quotes(self.code)
        return res.loc[0]

    def DeInitialization(self):
        pass


recv_factory['tushare_online'] = RecvTushareOnlien
