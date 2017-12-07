
class MarketData:



    def __init__(self, MarketSocket, updateInterval, sizePriceTable):

        self.MarketSocket = MarketSocket
        self.updateInterval = updateInterval
        self.sizePriceTable = sizePriceTable
        self.priceTable = [-1]*sizePriceTable
    
    
    
    
    
    
    
    
    def __isPriceTableFull(self):
        if(self.priceTable[-1] == -1):
            return False
        else:
            return True
    
    def __updatePriceTable(self):

        self.priceTable.insert(0, float(self.MarketSocket.getMarketPrice()))
        self.recentPriceTable = self.recentPriceTable[:-1]
        time.sleep(self.updateInterval)
   
  
   
