
from CoinBaseExchangeAuth import CoinbaseExchangeAuth
import requests
from threading import Timer
from AuthenticatedClient import AuthenticatedClient
import time
import datetime


class Algorithm:
    "Running algoritm class to be used by purchase objects"
    #number of entries that will be stored in the price table all the
    #data we have to work with. will ultimetely be a very large number
    NUM_ENTRIES_AVERAGEPRICETABLE = 4
    ENTRIES_PER_AVERAGE = 4
    #Time given in seconds
    UPDATE_INTERVAL = 15
    NUM_SECONDS_BUY_OR_SELL = 10


    def __init__(self, alg, AuthClient, MarketData, dollar_value, typeCoin):
        self.alg = alg
        self.AuthClient = AuthClient
        self.MarketData = MarketData
        self.recentPriceTable = [0]*(Algorithm.NUM_ENTRIES_AVERAGEPRICETABLE * Algorithm.ENTRIES_PER_AVERAGE)
        self.current_price = 0
        self.slopeTable = [-100]*(Algorithm.NUM_ENTRIES_AVERAGEPRICETABLE-1)
        self.dollar_value = dollar_value
        self.typeCoin = typeCoin
        self.inMarket = False
        self.secondDerivTable =[0]*(Algorithm.NUM_ENTRIES_AVERAGEPRICETABLE - 2)
        self.averagePriceTable =[0]*(Algorithm.NUM_ENTRIES_AVERAGEPRICETABLE)
        self.averageGain = -1
        self.averageLoss = -1



    def secondDerivBuyAlgo(self):
        minSecondDeriv = .01
        buyPrice = 0


        while(not self.inMarket):
            secondDeriv = self.getSecondDeriv()
            print("Recent Price Table ---------- " + str(self.recentPriceTable))
            print("Average Price Table ---------- " + str(self.averagePriceTable))
            print("Slope Table ---------- " + str(self.slopeTable))
            print("Second Deriv Object ---------- " + str(secondDeriv))
            print("Second Derriv Table ---------- " + str(self.secondDerivTable) + "\n")



            if(secondDeriv[0] and secondDeriv[1] > minSecondDeriv):
                print("-------------BUY----------------------" + "\n")
                print("\n")
                print("----Bought with Second Deriv At: " + str(self.secondDerivTable))
                currentDT = datetime.datetime.now()
                print (str(currentDT))
                print("\n")
                print("\n")
                #WILL RETURN WRONG TYPE _______________________________________

                size = float(self.dollar_value) / float(self.MarketSocket.getMarketPrice())


                setPrice = float(self.MarketSocket.getMarketPrice())
                setPrice = round(setPrice,3)
                setPrice = str(setPrice)
                size = str(round(size,2))


                self.AuthClient.buy(size, setPrice, self.typeCoin)
                buyPrice = setPrice
                self.inMarket = True
                percentSell(buyPrice)


    def percentSell(self, buyPrice):
        highProfit = 0
        tolerance = .3

        if(inMarket):
            profit = MarketSocket.getMarketPrice() - buyPrice
            if(profit > highProfit):
                highProfit = profit

            if(profit < 0 or profit/highProfit < (1-tolerance)):
                price = Market.getMarketPrice()
                size = self

                self.AuthClient.sell(size, "market", self.typeCoin)
                inMarket = False

            time.sleep(1)


    def getSecondDeriv(self):

        self.updateSlopeTable()
        #first index indicates weather all second derivatives are positive
        #second index returns the average secondDerivative
        returnElement = [False, 0]
        allPositive = True

        self.secondDerivTable.insert(0, (self.slopeTable[1]-self.slopeTable[0])/Algorithm.UPDATE_INTERVAL)
        self.secondDerivTable = self.secondDerivTable[:-1]

        previousItem = 0
        for item in self.secondDerivTable:
            if(item < 0):
                allPositive = False
            if(item < previousItem):
                allPositive = False
            previousItem = item
             #ensures that all second derivs are positiv

        for item in self.slopeTable:
            if(item <= 0):
                allPositive = False

        averageSecondDeriv = sum(self.secondDerivTable) / float(len(self.secondDerivTable))
        returnElement = [allPositive, averageSecondDeriv]

        return returnElement


    def updateSlopeTable(self):
        self.updateAvgTable()
        iterator = 0

        if(self.slopeTable[len(self.slopeTable)-1] == -100):
            while(iterator < len(self.slopeTable)):
                self.slopeTable[iterator] = (self.averagePriceTable[iterator] - self.averagePriceTable[iterator+1])/ Algorithm.UPDATE_INTERVAL
                iterator +=1

        else:
            self.slopeTable.insert(0,(self.averagePriceTable[0] - self.averagePriceTable[1])/ Algorithm.UPDATE_INTERVAL)
            self.slopeTable = self.slopeTable[:-1]

    def updateAvgTable(self):
        iterator = 0
        while(iterator < Algorithm.ENTRIES_PER_AVERAGE):
            self.updatePriceTable()
            iterator += 1

        i = 0
        start = 0
        end = Algorithm.ENTRIES_PER_AVERAGE
        while i < len(self.averagePriceTable):
            average = 0

            while start < end:
                average += self.recentPriceTable[start]
                start += 1
            end += Algorithm.ENTRIES_PER_AVERAGE
            average = average/len(self.averagePriceTable)

            self.averagePriceTable[i] = average
            average = 0
            i += 1
        if(len(self.averagePriceTable) > Algorithm.NUM_ENTRIES_AVERAGEPRICETABLE):
            self.averagePriceTable = self.averagePriceTable[:-1]

    def buyRSI(self):
        numPeriods = 14
        print("wait: " + numPeriods*marketData.updateInterval)

              #THINGS TO FIX HERE

        while self.inMarket == False:

            RSI = self.marketData.getRSI(numPeriods)

            print("------------------------------------------")
            print("looking for buy")
            print("Current Market Price: " + str(self.recentPriceTable[0]))
            print("RSI: " + str(RSI))
            print("\n")
            print("\n")

            if(RSI < 35):

                size = float(self.dollar_value) / float(self.MarketData.getMarketPrice())
                setPrice = float(self.MarketSocket.getMarketPrice()) -.01
                setPrice = round(setPrice,3)

                setPrice = str(setPrice)
                size = str(round(size,2))

                response = self.AuthClient.buy(size, setPrice , self.typeCoin)
                buyPrice = setPrice

                numSeconds = 0
                while(response["status"] == "pending" and numSeconds < NUM_SECONDS_BUY_OR_SELL):
                    response = self.AuthClient.checkOrder()
                    numSeconds += 1
                    time.sleep(1)

                if(numSeconds != NUM_SECONDS_BUY_OR_SELL):
                    self.inMarket = True
                    self.sellRSI(size)
                else:
                    response = self.AuthClient.cancelOrder()
                    print("order canceled")




    def sellRSI(self, size):
        numPeriods = 14
        while(self.inMarket == True):
            RSI = self.getRSI(numPeriods)

            print("------------------------------------------")
            print("looking for sell")
            print("Current Market Price: " + str(self.recentPriceTable[0]))
            print("RSI: " + str(RSI))
            print("\n")
            print("\n")

            if(RSI > 80):

                setPrice = float(self.MarketSocket.getMarketPrice())
                setPrice = round(setPrice,3)
                setPrice = str(setPrice)
                size = str(round(size,2))

                self.AuthClient.sell(size, "market", self.typeCoin)
                self.inMarket = False
                buyRSI(numPeriods)
