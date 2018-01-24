
from CoinBaseExchangeAuth import CoinbaseExchangeAuth
import requests
from threading import Timer
from AuthenticatedClient import AuthenticatedClient
import time
import datetime


class Algorithm:
    #number of entries that will be stored in the price table all the
    #data we have to work with. will ultimetely be a very large number
    NUM_ENTRIES_AVERAGEPRICETABLE = 4
    ENTRIES_PER_AVERAGE = 4
    #Time given in seconds
    UPDATE_INTERVAL = 15
    NUM_SECONDS_BUY_OR_SELL = 10


    def __init__(self, alg, AuthClient, MarketData, dollar_value, typeCoin):

        self.AuthClient = AuthClient
        self.MarketData = MarketData
        self.alg = alg
        self.typeCoin = typeCoin
        self.dollar_value = dollar_value

        self.running = False
        self.current_price = 0
        self.inMarket = False

    def run(self, algorithm = None):
        self.running = True
        self.buyRSI()

    def stop(self):
        self.running = False


    def buyRSI(self):
        numPeriods = 14
        TargetRSI = 35

        while self.running and self.inMarket == False:

            RSI = self.marketData.getRSI(numPeriods)

            print("------------------------------------------")
            print("looking for buy")
            print("Current Market Price: " + str(self.recentPriceTable[0]))
            print("RSI: " + str(RSI))
            print("\n")
            print("\n")

            if(RSI < TargetRSI):

                size = float(self.dollar_value) / float(self.MarketData.getMarketPrice())
                size = str(round(size,2))
                response = self.AuthClient.buy(size, "market" ,self.typeCoin)
                #WE NEED ORDER ID NUMBER
                orderID = response["id"]

                numSeconds = 0
                while(response["status"] == "pending" and numSeconds < NUM_SECONDS_BUY_OR_SELL):
                    response = self.AuthClient.checkOrder()
                    numSeconds += .5
                    time.sleep(.5)

                if(numSeconds < NUM_SECONDS_BUY_OR_SELL):
                    self.inMarket = True
                    self.sellRSI(size)
                else:
                    #CANCEL ORDER REQUIRES ORDER ID NUMBER
                    response = self.AuthClient.cancelOrder(orderID)
                    print("Order Canceled")


    def sellRSI(self):
        numPeriods = 14
        TargetRSI = 80

        while self.running and self.inMarket == False:

            RSI = self.marketData.getRSI(numPeriods)

            print("------------------------------------------")
            print("looking for sell")
            print("Current Market Price: " + str(self.recentPriceTable[0]))
            print("RSI: " + str(RSI))
            print("\n")
            print("\n")

            if(RSI > TargetRSI):

                size = float(self.dollar_value) / float(self.MarketData.getMarketPrice())
                size = str(round(size,2))
                response = self.AuthClient.buy(size, "market" ,self.typeCoin)
                #WE NEED ORDER ID NUMBER
                orderID = response["id"]

                numSeconds = 0
                while(response["status"] == "pending" and numSeconds < NUM_SECONDS_BUY_OR_SELL):
                    response = self.AuthClient.checkOrder()
                    numSeconds += .5
                    time.sleep(.5)

                if(numSeconds < NUM_SECONDS_BUY_OR_SELL):
                    self.inMarket = True
                    self.sellRSI(size)
                else:
                    #CANCEL ORDER REQUIRES ORDER ID NUMBER
                    response = self.AuthClient.cancelOrder()
                    print("Order Canceled")
                    #if sell order is not filled within the allowed time
                    #rerun the sell RSI algorithm
                    self.sellRSI(orderID)
