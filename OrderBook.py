import CoinBaseExchangeAuth
from UserSocket import UserSocket
import json

class OrderBook:

    def __init__(self, coinBaseExchangeAuth):
        self.OrderBookUserSocket = UserSocket(coinBaseExchangeAuth)
        self.running = False
        self.orderbook = {}

    def open(self, product_id):
        OrderBookchannels = {"name": "level2"}
        self.OrderBookUserSocket.subscribe(product_id, OrderBookchannels)
        self.running = True

    def close(self):
        self.OrderBookUserSocket.closeSocket()
        self.running = False

    def isRunning(self):
        return self.running

    def update(self):
        if(self.OrderBookUserSocket.isConnected()):

            response = self.OrderBookUserSocket.listen()
            if(str(response["type"]) == "snapshot"):

                self.orderbook = {d[0]: d[1:][0] for d in response["asks"]}
            if(str(response["type"]) == "l2update"):
                self.orderBookUpdater(response)

        else:
            self.close()

    def orderBookUpdater(self, response):

        changes = (response["changes"])
        changes = changes[0]
        price = changes[1]
        volume = changes[2]
        self.orderbook[price] = volume

    def getOrderBook(self):
        self.update()
        return self.orderbook
