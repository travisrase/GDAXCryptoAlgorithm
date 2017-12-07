
class MarketData:



    def __init__(self, MarketSocket, updateInterval, sizePriceTable):

        self.MarketSocket = MarketSocket
        self.updateInterval = updateInterval
        self.sizePriceTable = sizePriceTable
        self.priceTable = [-1]*sizePriceTable
        self.lastAverageGain = -1
        self.lastAverageLoss = -1
        self.lastSmoothedAverageGain = -1
        self.lastSmoothedAverageLoss = -1
    
    
    
    def getRSI(self, numPeriods, updatePriceTable = True):
        RSI = -1
        RS = self.getRS(numPeriods, updatePriceTable)
        if(RS == -1):
            return RSI
        else:
            RSI = 100 - 100/(1+RS)
            return RSI
    
    def getRS(self, numPeriods, updatePriceTable = True):
        RS = -1
        avgGain
        if(updatePriceTable):
            avgGain = self.getSmoothedAverageGain(numPeriods)
        else:
            avgGain = self.getSmoothedAverageGain(numPeriods, updatePriceTable)
        
        avgLoss = self.getSmoothedAverageLoss(self.sizePriceTable -1, False)
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
    
    def getSmoothedAverageLoss(self, numPeriods = self.sizePriceTable -1, updatePriceTable = True):
        smoothedAverage = -1
        
        if(self.lastSmoothedAverageGain == -1):
            smoothedAverage = (self.lastAverageLoss*(numPeriods-1) + self.getAverageLoss(numPeriods + 1, updatePriceTable))/ numPeriods
            
        else:
            smoothedAverage = (self.lastSmoothedAverageLoss*(numPeriods-1) + self.getAverageLoss(numPeriods + 1, updatePriceTable))/ numPeriods
            
        return smoothedAverage
    
    
    def getSmoothedAverageGain(self, numPeriods = self.sizePriceTable -1, updatePriceTable = True):
        smoothedAverage = -1
        
        if(self.lastSmoothedAverageGain == -1):
            smoothedAverage = (self.lastAverageGain*(numPeriods-1) + self.getAverageGain(numPeriods + 1, updatePriceTable))/ numPeriods
            
        else:
            smoothedAverage = (self.lastSmoothedAverageGain*(numPeriods-1) + self.getAverageGain(numPeriods + 1, updatePriceTable))/ numPeriods
            
        return smoothedAverage
    
    def getAverageGain(self, numPeriods = self.sizePriceTable, updatePriceTable = True):
        if(updatePriceTable):
            self.__fillPriceTable()
        
        average = -1
        gainTable = []
        if(len(self.priceTable) < numPeriods):
            return average
        else:
            for i in range(1,numPeriods):
                gain = self.priceTable[i] - self.priceTable[i-1]
                if(gain > 0):
                    gainTable.insert(i-1, loss)
                else:
                    gainTable.insert(i-1, 0)
            sm = sum(lossTable)
            average = sm/numPeriods
            self.lastAverageLoss = average
            return average
            
    def getAverageLoss(self, numPeriods = self.sizePriceTable, updatePriceTable = True):
        if(updatePriceTable):
            self.__fillPriceTable()
        
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
            self.lastAverageGain = average
            return average
            
    
    def __fillPriceTable(self):
        self.__updatePriceTable()
        while(self.__isPriceTableFull() == False):
            self.__updatePriceTable()
        
    
    def __isPriceTableFull(self):
        if(self.priceTable[-1] == -1):
            return False
        else:
            return True
    
    def __updatePriceTable(self):

        self.priceTable.insert(0, float(self.MarketSocket.getMarketPrice()))
        self.recentPriceTable = self.recentPriceTable[:-1]
        time.sleep(self.updateInterval)
   
  
   
