from ib_insync import *
"""
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

contract = Forex('EURUSD')
bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='30 D',
            barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe:
df = util.df(bars)
print(df[['date', 'open', 'high', 'low', 'close']])
"""
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=13)

contract = Stock('TEVA', 'SMART', 'USD')
ib.qualifyContracts(contract)

limitOrder = LimitOrder('BUY', 10, 0.05)
limitTrade = ib.placeOrder(contract, limitOrder)
ib.sleep(3)
limitOrder.lmtPrice = 0.10

ib.placeOrder(contract, limitOrder)
ib.sleep(3)
#ib.cancelOrder(limitOrder)
