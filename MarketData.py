from Ticker import Ticker
from threading import Thread
import time
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

        self.smoothedAverageGain = -1
        self.smoothedAverageLoss = -1

        self.updatingPriceTable = False
        self.scheduler = BackgroundScheduler()
        self.Ticker = Ticker(coinBaseExchangeAuth)

    #will auto update the price table every updateInterval seconds
    def runMarketData(self):
        self.scheduler.start()
        self.scheduler.add_job(self.__updateAll,'interval', seconds = self.updateInterval)
        self.updatingPriceTable = True
        print("Market Data Updating")

    #will stop auto updating the price table
    def stopMarketData(self):
        self.scheduler.shutdown()
        self.updatingPriceTable = False
        print("Market Data No Longer Updating")

    def updateAll(self):
        self.__updatePriceTable()
        self.__updateSmoothedAverageGain()
        self.__updateSmoothedAverageLoss()


    def getRSI(self, numPeriods):
        RSI = -1
        RS = self.getRS(numPeriods)
        if(RS == -1):
            return RSI
        else:
            RSI = 100 - 100/(1+RS)
            return RSI

    def getRS(self, numPeriods):
        RS = -1
        avgGain = self.getSmoothedAverageGain(numPeriods)
        avgLoss = self.getSmoothedAverageLoss(numPeriods)

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

    def getSmoothedAverageLoss(self):
        return self.smoothedAverageLoss

    def __updateSmoothedAverageLoss(self, numPeriods = 0, updatePriceTable = True):
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

    def getSmoothedAverageGain(self):
        return self.smoothedAverageGain()

    def __updateSmoothedAverageGain(self, numPeriods = 0, lastSmoothedAverageGain):
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


    def __fillPriceTable(self):
        self.__updatePriceTable()
        while(self.__isPriceTableFull() == False):
            self.__updatePriceTable()

    def __getSizePriceTable(self):
        return self.sizePriceTable

    def getPriceTable(self):
        return self.priceTable

    def __isPriceTableFull(self):
        if(self.priceTable[-1] == -1):
            return False
        else:
            return True

    def __updatePriceTable(self):
        if(not self.Ticker.isRunning()):
            self.Ticker.openTicker([self.product_id])

        self.priceTable.insert(0, float(self.Ticker.getPrice()))
        self.priceTable = self.priceTable[0:self.sizePriceTable]
