import Purchase
import WebsocketClient
import AuthenticatedClient
import Time

class Algorithm:
    "Running algoritm class to be used by purchase objects"
    #number of entries that will be stored in the price table all the
    #data we have to work with. will ultimetely be a very large number
    NUM_ENTRIES_PRICETABLE = 4
    #Time given in seconds
    UPDATE_INTERVAL = 10


    def __init__(self, alg, AuthClient, MarketSocket, dollar_value, typeCoin):
        self.alg = alg
        self.AuthClient = AuthClient
        self.MarketSocket = MarketSocket
        self.recentPriceTable = {NUM_ENTRIES_PRICETABLE}
        self.current_price = 0
        self.slopeTable = {NUM_ENTRIES_PRICETABLE - 1}
        self.dollar_value = dollar_value
        self.typeCoin = typeCoin
        self.inMarket = False


    def secondDerivBuyAlgo():
        minSecondDeriv = .01
        buyPrice = 0


        while(!inMarket):
            secondDeriv = getSecondDeriv()
            if(secondDeriv[0] = true && secondDeriv[1] > minSecondDeriv):
                #WILL RETURN WRONG TYPE _______________________________________
                size = dollar_value / MarketSocket.getMarketPrice()
                setPrice = MarketSocket.getMarketPrice() -1

                AuthClient.buy(size, setPrice, typeCoin)
                buyPrice = setPrice
                inMarket = True
                percentSell(buyPrice)
            else
                time.sleep(UPDATE_INTERVAL)


    def percentSell(buyPrice)
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


















    def getSecondDeriv():

        #first index indicates weather all second derivatives are positive
        #second index returns the average secondDerivative
        returnElement = {False, 0}
        allPositive = True
        secondDerivTable = {len(slopeTable) -1}
        for index in range(1, len(secondDerivTable))
            if(index < 0):
                allPositive = False

            secondDerivTable[index-1] = (slopeTable[index-1]-slopeTable[index])/UPDATE_INTERVAL


        averageSecondDeriv = sum(secondDerivTable) / float(len(secondDerivTable))
        returnElement = {allPositive, averageSecondDeriv}
        return returnElement

    def update():



    	if current_price >= setPrice:

    		size1 = dollar_buy/setPrice
    		AuthenticatedClient.buy(size1, setPrice, 'LTC-USD')



    def updateSlopeTable():
        updatePriceTable()
        for index in range(1, len(recentPriceTable)-1):
            sloepTable[index-1] = (recentPriceTable[index-1] - recentPriceTable[index])/ UPDATE_INTERVAL


    def updatePriceTable():

        for index in range(len(recentPriceTable)-1, 0, -1)
            if(index == 0):
                priceTable[0] = MarketSocket.getMarketPrice()
            else:
                priceTable[index] = priceTable[index-1]
