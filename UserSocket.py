import json, hmac, hashlib, time, requests, base64

from requests.auth import AuthBase

import MarketSocket
import requests
from threading import Timer
from websocket import create_connection
import json
import time


class UserSocket():


    def __init__(self,adress, api_key="", api_secret="", api_passphrase=""):
        self.CoinBaseExchangeAuth = CoinBaseExchangeAuth
        self.socket = None
        self.channels = {"ticker"}
        self.adress = adress
        self.connected = False


    def openWS(self):
        socket = websocket.WebSocket()
        socket = socket.connect("wss://ws-feed.gdax.com")
        self.listen()

    def subscribe(self):


        params = {'type': 'subscribe', 'product_ids': ["LTC-USD"], 'channels': ["full"]}

        time = str(time.time())
        verify = time + 'GET' + '/users/self/verify'
        verify = verify.encode('ascii')

        hmac_key = base64.b64decode(self.api_secret)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').strip('\n')

        params['signature'] = signature_b64
        params['key'] = self.api_key
        params['passphrase'] = self.api_passphrase
        params['timestamp'] = timestamp

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
