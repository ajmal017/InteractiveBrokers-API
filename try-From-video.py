from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.contract import Contract as IBcontract
from ibapi.order import Order
from ibapi.execution import ExecutionFilter
from ibapi.common import *
import time
from threading import Thread
import queue
import datetime
from copy import deepcopy


class TestApp(EWrapper, EClient):
    def __init__(self):
        #TestWrapper.__init__(self)
        EClient.__init__(self, self)
    


    def error (self, reqId:TickerId, errorCode:int, errorString:str):
        print ("Error: " ,reqId ," " ,errorCode ," " ,errorString)
        


if __name__ == '__main__':
    print ("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    app = TestApp()
    app.connect ("127.0.0.1", 7497, 10)
    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.currency = "USD"
    contract.exchange = "SMART"

    app.run()
