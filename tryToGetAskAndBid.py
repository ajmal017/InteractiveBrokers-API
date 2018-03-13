import datetime
import pprint
from ib_insync import *
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=15)
spy = []
spy = Stock('TEVA','SMART','USD')
[ticker] = ib.reqTickers(spy)
ticker
#Ticker(contract=Stock(symbol='SPY', exchange='SMART', currency='USD'), time=datetime.datetime(2017, 7, 10, 11, 8, 37, 789572), bid=242.3, bidSize=26, ask=242.3, askSize=75, last=242.3, lastSize=1, volume=456, close=242.11, ticks='[...]')
