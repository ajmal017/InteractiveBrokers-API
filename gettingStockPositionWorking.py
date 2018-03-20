import datetime
from pprint import pprint
from ib_insync import *

"""
the function get a ib_insync.ib.IB object and a string symbol (that represent a stock).
the function returns the position of this symbol stock.
"""
def getSymbolPosition(ib , symbol):
	data = ib.positions()
	for pos in data:
		if (pos.contract.symbol == symbol):
			return  pos.position
	print ("symbol %s not found!" %(symbol))
	return 0 


ib = IB()
print (type(ib))
ib.connect('127.0.0.1', 7497, clientId=15)
sy = "SPY"
x = getSymbolPosition(ib , sy)
print ("from the stock %s there is %s left" %(sy, x))
