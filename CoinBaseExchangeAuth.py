import requests

import json, hmac, hashlib, time, requests, base64

from requests.auth import AuthBase



# Create custom authentication for Exchange. Saves the API Key, Secret Key and Passphrase
class CoinbaseExchangeAuth(AuthBase):
    
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        
    #any instance of this class returns a string containing a request object with a header containing nessesssary info to authenticate
    
    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').strip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

    def __str__(self):
        return self.api_key + "   " + self.secret_key + "  " + self.passphrase

