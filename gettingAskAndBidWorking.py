import datetime
from pprint import pprint
from ib_insync import *
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=15)
spy = []
spy = Stock('GLD','SMART','USD')

#spy = Stock('MSFT', 'SMART', 'USD') // this will create an ambligous error.
#spy = Stock('MSFT', 'SMART', 'USD', primaryExchange='NASDAQ') // this is the solution for the ambligous error.

ticker = ib.reqTickers(spy)
#pprint (ticker)

#geeting the ask and bid from the ticker.
bid = ticker[0].bid
ask = ticker[0].ask

print ("the ask value is: %s"  %ask )
print ("the ask value is: %s"  %bid )
