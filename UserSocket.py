import CoinBaseExchangeAuth
import MarketSocket
import requests
from threading import Timer
from websocket import create_connection
import json
import time


class UserSocket():


    def __init__(self,adress, CoinBaseExchangeAuth):
        self.CoinBaseExchangeAuth = CoinBaseExchangeAuth
        self.socket = None
        self.channels = {"ticker"}
        self.adress = adress
        self.connected = False


    def openWS(self):
        socket = websocket.WebSocket()
        socket = socket.connect("wss://ws-feed.gdax.com")
        return socket

    def subscribe(self):

        params = {'type': 'subscribe', 'product_ids': ["LTC-USD"], 'channels': ["full"]}
        self.socket = create_connection(self.adress)
        print(self.socket)
        self.socket.send(json.dumps(params))
        self.connected = True


        #subscription = json.loads(subscription)

        print(self.socket.json())

    def listen(self):
        while self.connected:
            try:
`               if int(time.time() % 31) == 0:
                self.socket.ping("")
                response = self.socket.recv()
                response = json.loads(response)
                return response
            except Exception as e:
                self.connected = False
