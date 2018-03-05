
from ib_insync import *
from ibapi.order_condition import *

ib = IB()

ib.connect('127.0.0.1', 7497, clientId=15)
contract = []
contract = Stock('TEVA','SMART','USD')

ib.qualifyContracts(contract)
"""
conContract = IBcontract()
conContract.symbol = "SPY"
conContract.secType = "STK"
#conContract.exchange = "SMART"
conContract.exchange = "BATS"
"""
conContract = Stock('SPY','SMART','USD')
ib.qualifyContracts(conContract)

conParams = []

#conParams.append(PriceCondition(0, contract.conId, "SMART", False, 112.0))
lmt = LimitOrder('BUY', 1 ,10,
                     conditions = [PriceCondition(0, conContract.conId, exch= "SMART", isMore= True, price = 1000)])
lmt.conditionsCancelOrder = True
# print(lmt)
ib.placeOrder(contract, lmt)
