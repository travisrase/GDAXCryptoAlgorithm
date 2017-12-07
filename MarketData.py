
class MarketData:



    def __init__(self, MarketSocket, updateInterval, sizePriceTable):

        self.MarketSocket = MarketSocket
        self.updateInterval = updateInterval
        self.sizePriceTable = sizePriceTable
        self.priceTable = [-1]*sizePriceTable
    
    
    
    
    
    
    
    
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
   
  
   
