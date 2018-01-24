import CoinBaseExchangeAuth
from UserSocket import UserSocket
import json

class Ticker:

    def __init__(self, coinBaseExchangeAuth):
        self.UserSocket = UserSocket(coinBaseExchangeAuth)
        self.running = False
        self.ticker = {}
        self.orderbook = {}


    def openTicker(self, product_id):
        channels = ["ticker"]
        self.UserSocket.subscribe(product_id, channels)
        self.UserSocket.flush()
        self.running = True

    def closeTicker(self):
        self.UserSocket.closeSocket()
        self.running = False

    def isRunning(self):
        return self.running

    def update(self):
        response = self.UserSocket.listen()
        self.ticker = response

    def getPrice(self):
        self.update()
        price = (self.ticker["price"])
        return price
