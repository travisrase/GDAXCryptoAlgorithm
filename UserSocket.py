import json, hmac, hashlib, time, requests, base64

from requests.auth import AuthBase

import requests
from threading import Timer
from websocket import create_connection
import json
import time
import CoinBaseExchangeAuth


class UserSocket():


    def __init__(self, coinBaseExchangeAuth):
        self.socket = None
        self.channels = []
        self.product_id = []
        self.connected = False
        self.api_key = coinBaseExchangeAuth.getAPIKey()
        self.api_secret = coinBaseExchangeAuth.getSecretKey()
        self.api_passphrase = coinBaseExchangeAuth.getPassphrase()
        self.address = "wss://ws-feed.gdax.com"


    def subscribe(self,product_id, channels):
        self.product_id = product_id
        self.channels = channels

        #product_id is a list of strings string such as ["LTC-USD"]
        #channels is a list that contains the channels as strings
        #such as ["ticker"]
        params = {'type': 'subscribe', 'product_ids': product_id, 'channels': channels}

        time1 = str(time.time())
        verify = time1 + 'GET' + '/users/self/verify'
        verify = verify.encode('ascii')

        hmac_key = base64.b64decode(self.api_secret)
        signature = hmac.new(hmac_key, verify, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').strip('\n')

        params['signature'] = signature_b64
        params['key'] = self.api_key
        params['passphrase'] = self.api_passphrase
        params['timestamp'] = time1

        self.socket = create_connection(self.address)

        print(self.socket)
        self.socket.send(json.dumps(params))
        self.connected = True
        print("------CONNECTED------")

        #subscription = json.loads(subscription)
        print(self.socket)

    def listen(self):
        if self.connected:
            try:
                self.socket.ping("")
                response = self.socket.recv()
                response = json.loads(response)
                return response
            except Exception as e:
                self.connected = False
