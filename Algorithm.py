
from CoinBaseExchangeAuth import CoinbaseExchangeAuth
import requests
from threading import Timer
from AuthenticatedClient import AuthenticatedClient
import time
import datetime

class Algorithm:
    #Time given in seconds
    UPDATE_INTERVAL = .5
    NUM_SECONDS_BUY_OR_SELL = 10
    SIZE_PRICE_TABLE = 100

    def __init__(self, alg, AuthClient, dollar_value, typeCoin):
        self.AuthClient = AuthClient
        self.MarketData = MarketData(typeCoin, AuthClient.getExchangeAuth(), UPDATE_INTERVAL, SIZE_PRICE_TABLE)
        self.alg = alg
        self.typeCoin = typeCoin
        self.dollar_value = dollar_value

        self.running = False
        self.inMarket = False

    def run(self, algorithm = None):
        self.running = True
        self.buyRSI()

    def stop(self):
        self.running = False
        
    #This simple algorithm will commit a buy order when the RSI (Relative Strength Inex) reaches a value of 35
    #This should theoretically indicate that the currency is being oversold
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
                    
    #This simple algorithm will commit a buy order when the RSI (Relative Strength Inex) reaches a value of 80
    #This should theoretically indicate that the currency is being overbought
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
