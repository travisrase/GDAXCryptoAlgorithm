import CoinBaseExchangeAuth
from UserSocket import UserSocket
import json

class Ticker:
    def __init__(self, coinBaseExchangeAuth):
        self.TickerUserSocket = UserSocket(coinBaseExchangeAuth)
        self.running = False
        self.ticker = {"price":"-1", "volume_24h": "0.0", "best_bid": "0.0", "best_ask" : "0.0", "last_size": "0.0", "high_24h": "0.0", "low_24h": "0.0"}

    def open(self, product_id):
        TickerChannels = {"name": "ticker"}
        self.TickerUserSocket.subscribe(product_id, TickerChannels)
        self.TickerUserSocket.flush()
        self.running = True

    def close(self):
        self.TickerUserSocket.closeSocket()
        self.running = False

    def isRunning(self):
        return self.running

    def update(self):
        if(self.TickerUserSocket.isConnected()):
            tickerResponse = self.TickerUserSocket.listen()
            self.ticker = tickerResponse
        else:
            self.close()

    def getPrice(self):
        price = float(self.ticker["price"])
        return price

    def get24HourVolume(self):
        volume = float(self.ticker["volume_24h"])
        return volume

    def getBestBid(self):
        bestBid = float(self.ticker["best_bid"])
        return bestBid

    def getBestAsk(self):
        bestAsk = float(self.ticker["best_ask"])
        return bestAsk

    def getLastVolume(self):
        volume = float(self.ticker["last_size"])
        return volume

    def get24HourHigh(self):
        price = float(self.ticker["high_24h"])
        return price

    def get24HourLow(self):
        price = float(self.ticker["low_24h"])
        return price
