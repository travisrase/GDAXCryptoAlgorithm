
from CoinBaseExchangeAuth import CoinbaseExchangeAuth
import MarketSocket
import requests
from threading import Timer
from AuthenticatedClient import AuthenticatedClient
import time
import datetime


class Algorithm:
    "Running algoritm class to be used by purchase objects"
    #number of entries that will be stored in the price table all the
    #data we have to work with. will ultimetely be a very large number
    NUM_ENTRIES_PRICETABLE = 4
    #Time given in seconds
    UPDATE_INTERVAL = 1


    def __init__(self, alg, AuthClient, MarketSocket, dollar_value, typeCoin):
        self.alg = alg
        self.AuthClient = AuthClient
        self.MarketSocket = MarketSocket
        self.recentPriceTable = [Algorithm.NUM_ENTRIES_PRICETABLE*4]
        self.current_price = 0
        self.slopeTable = [Algorithm.NUM_ENTRIES_PRICETABLE-1]
        self.dollar_value = dollar_value
        self.typeCoin = typeCoin
        self.inMarket = False
        self.secondDerivTable =[Algorithm.NUM_ENTRIES_PRICETABLE - 2]
        self.averagePriceTable =[-1,-1,-1,-1]



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


                #self.AuthClient.buy(size, setPrice, self.typeCoin)
                #buyPrice = setPrice
                self.inMarket = True

                #percentSell(buyPrice)
            else:

                time.sleep(Algorithm.UPDATE_INTERVAL)


    def percentSell(self, buyPrice):
        highProfit = 0
        tolerance = .3

        if(inMarket):
            profit = MarketSocket.getMarketPrice() - buyPrice
            if(profit > highProfit):
                highProfit = profit

            if(profit < 0):
                #SELL__________________________________________
                inMarket = False

            elif(profit/highProfit < (1-tolerance)):
                #SELL_______________________
                inMarket = False

            time.sleep(1)











    def getSecondDeriv(self):

        self.updateSlopeTable()
        #first index indicates weather all second derivatives are positive
        #second index returns the average secondDerivative
        returnElement = [False, 0]
        allPositive = True

        if len(self.slopeTable) < Algorithm.NUM_ENTRIES_PRICETABLE:
            self.updateSlopeTable()

        self.secondDerivTable.insert(0, (self.slopeTable[0]-self.slopeTable[1])/Algorithm.UPDATE_INTERVAL)

        if len(self.secondDerivTable) >= len(self.slopeTable)-1:
            self.secondDerivTable = self.secondDerivTable[:-1]


        for item in self.secondDerivTable:
            if(item < 0):
                allPositive = False
             #ensures that all second derivs are positiv
        self.updateSlopeTable()
        for item in self.slopeTable:
            if(item <= 0):
                allPositive = False

        averageSecondDeriv = sum(self.secondDerivTable) / float(len(self.secondDerivTable))
        returnElement = [allPositive, averageSecondDeriv]

        return returnElement




    def updateSlopeTable(self):

        self.updatePriceTable()

        while len(self.recentPriceTable) < Algorithm.NUM_ENTRIES_PRICETABLE*4:
            self.updatePriceTable()
        self.updateAvgTable()
        while len(self.averagePriceTable) < Algorithm.NUM_ENTRIES_PRICETABLE-1:
            self.updateAvgTable()
            #if len(self.recentPriceTable) > Algorithm.NUM_ENTRIES_PRICETABLE:

            #    self.slopeTable.insert(0,(self.recentPriceTable[0] - self.recentPriceTable[1])/ Algorithm.UPDATE_INTERVAL)

        if len(self.slopeTable) > Algorithm.NUM_ENTRIES_PRICETABLE - 1:
            self.slopeTable = self.slopeTable[:-1]

        self.slopeTable.insert(0,(self.averagePriceTable[0] - self.averagePriceTable[1])/ Algorithm.UPDATE_INTERVAL)

        #for index in range(1, len(self.recentPriceTable)-1):
        #    self.slopeTable[index-1] = (self.recentPriceTable[index-1] - self.recentPriceTable[index])/ UPDATE_INTERVAL


    def updatePriceTable(self):

        if len(self.recentPriceTable) < Algorithm.NUM_ENTRIES_PRICETABLE*4:

            self.recentPriceTable.insert(0, float(self.MarketSocket.getMarketPrice()))
        else:
            self.recentPriceTable.insert(0, float(self.MarketSocket.getMarketPrice()))
            self.recentPriceTable = self.recentPriceTable[:-1]

    def updateAvgTable(self):

        i = 0
        start = 0
        end = 4
        while i < len(self.averagePriceTable):

            average = 0

            while start < end:
                average += self.recentPriceTable[start]
                start += 1
            end += 4
            average = average/len(self.averagePriceTable)

            self.averagePriceTable[i] = average
            average = 0
            i += 1
        if(len(self.averagePriceTable) > Algorithm.NUM_ENTRIES_PRICETABLE):
            self.averagePriceTable = self.averagePriceTable[:-1]
