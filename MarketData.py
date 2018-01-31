from Ticker import Ticker
from threading import Thread
import time
from OrderBook import OrderBook
from apscheduler.schedulers.background import BackgroundScheduler

class MarketData:


    #product_id is a String such as "LTC-USD"
    #updateInterval is an int
    #sizePriceTable is an int

    def __init__(self, product_id, coinBaseExchangeAuth, updateInterval, sizePriceTable):

        self.product_id = product_id
        self.updateInterval = updateInterval
        self.sizePriceTable = sizePriceTable
        self.priceTable = [-1]*sizePriceTable
        self.localOrderBook = {}

        self.smoothedAverageGain = -1
        self.smoothedAverageLoss = -1

        self.updating = False
        self.scheduler = BackgroundScheduler()
        self.Ticker = Ticker(coinBaseExchangeAuth)
        self.OrderBook = OrderBook(coinBaseExchangeAuth)

    #will auto update the price table every updateInterval seconds
    def runMarketData(self):
        self.scheduler.start()
        self.Ticker.open([self.product_id])
        self.OrderBook.open([self.product_id])

        self.scheduler.add_job(self.updateAll,'interval', seconds = self.updateInterval)
        self.scheduler.add_job(self.Ticker.update,'interval', seconds = self.updateInterval)
        self.scheduler.add_job(self.__updateOrderBook,'interval', seconds = self.updateInterval)

        self.updating = True
        print("Market Data Updating")

    #will stop auto updating the price table
    def stopMarketData(self):
        self.scheduler.shutdown()
        self.updating = False
        print("Market Data No Longer Updating")

    def isRunning(self):
        return self.updating

    def updateAll(self):
        self.__updatePriceTable()
        self.__updateSmoothedAverageGain()
        self.__updateSmoothedAverageLoss()

    #CURRENT RSI IS USELESS, DOES NOT WORK
    def getRSI(self, numPeriods, timeInterval):
        if(numPeriods*timeInterval > self.sizePriceTable*self.updateInterval):
            print("Invalid RSI Conditions")
            return -1
        else:
            RSI = -1
            RS = self.getRS(numPeriods, timeInterval)
            if(RS == -1):
                return RSI
            else:
                RSI = 100 - 100/(1+RS)
                return RSI

    #need to figure out a way to update
    def getRS(self, numPeriods, timeInterval):
        RS = -1
        avgGain = self.smoothedAverageGain
        avgLoss = self.smoothedAverageLoss

        if(avgGain == -1 or avgLoss == -1):
            return RS
        elif(avgGain == 0 and avgLoss == 0):
            RS = 1
            return RS
        elif(avgLoss == 0):
            RS = 0
        elif(avgGain == 0):
            RS = 99
        else:
            RS = avgGain/avgLoss
        return RS

    def __updateSmoothedAverageLoss(self, numPeriods = 0):
        if(numPeriods == 0):
            numPeriods = self.sizePriceTable -1

        smoothedAverage = -1
        previousSmoothedAverage = self.smoothedAverageLoss

        if(previousSmoothedAverage == -1):
            smoothedAverage = self.getAverageLoss(numPeriods + 1)

        else:
            smoothedAverage = (previousSmoothedAverage*(numPeriods-1) + self.getAverageLoss(numPeriods + 1))/ numPeriods

        self.smoothedAverageLoss = smoothedAverage
        return smoothedAverage

    def __updateSmoothedAverageGain(self, numPeriods = 0):
        if(numPeriods == 0):
            numPeriods = self.sizePriceTable -1

        smoothedAverage = -1
        previousSmoothedAverage = self.smoothedAverageGain

        if(previousSmoothedAverage == -1):
            smoothedAverage = self.getAverageLoss(numPeriods + 1)

        else:
            smoothedAverage = (previousSmoothedAverage*(numPeriods-1) + self.getAverageGain(numPeriods + 1))/ numPeriods

        self.smoothedAverageGain = smoothedAverage
        return smoothedAverage

    def getAverageGain(self, numPeriods = 0):

        if(numPeriods == 0):
            numPeriods = self.sizePriceTable

        average = -1
        gainTable = []
        if(len(self.priceTable) < numPeriods):
            return average
        else:
            for i in range(1,numPeriods):
                gain = self.priceTable[i] - self.priceTable[i-1]
                if(gain > 0):
                    gainTable.insert(i-1, gain)
                else:
                    gainTable.insert(i-1, 0)

            sm = sum(gainTable)
            average = sm/numPeriods
            if(not self.__isPriceTableFull()):
                return -1
            else:
                return average

    #returns an integer value of the sum of the losses between entries in
    #priceTable. Returns -1 if numPeriods is greater than the number of
    #entries in priceTable or if priceTable is not full.

    def getAverageLoss(self, numPeriods = 0):

        if(numPeriods == 0):
            numPeriods = self.sizePriceTable

        average = -1
        lossTable = []
        if(len(self.priceTable) < numPeriods):
            return average
        else:
            for i in range(1,numPeriods):
                loss = self.priceTable[i-1] - self.priceTable[i]
                if(loss > 0):
                    lossTable.insert(i-1, loss)
                else:
                    lossTable.insert(i-1, 0)

            sm = sum(lossTable)
            average = sm/numPeriods
            if(not self.__isPriceTableFull()):
                return -1
            else:
                return average

    def __isPriceTableFull(self):
        if(self.priceTable[-1] == -1):
            return False
        else:
            return True

    def __updatePriceTable(self):
        if(self.Ticker.isRunning()):
            self.priceTable.insert(0, self.Ticker.getPrice())
            self.priceTable = self.priceTable[0:self.sizePriceTable]
        else:
            self.stopMarketData()

    def getPriceTable(self):
        return self.priceTable

    def __updateOrderBook(self):
        if(self.self.OrderBook.isRunning()):
            self.localOrderBook = self.OrderBook.getOrderBook()
        else:
            self.stopMarketData()

    def getOrderBook(self):
        return self.localOrderBook
