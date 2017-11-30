
import requests
import CoinBaseExchangeAuth


class MarketSocket:



    def __init__(self, exchangeAuth, endpoint):

        self.exchangeAuth = exchangeAuth
        self.endpoint = endpoint



    def getMarketPrice(self):


        auth = self.exchangeAuth
        resp = requests.get(self.endpoint, auth=auth )

        if resp.status_code != 200:
            print(resp.status_code)
              # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))


        return resp.json().get("price")

    def getMarketVolume24(self):


        auth = self.exchangeAuth
        resp = requests.get(self.endpoint, auth=auth )

        if resp.status_code != 200:
            print(resp.status_code)
                      # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))


        return resp.json().get("volume")

    def getMarketSize(self):


        auth = self.exchangeAuth
        resp = requests.get(self.endpoint, auth=auth )

        if resp.status_code != 200:
            print(resp.status_code)
                      # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))


        return resp.json().get("size")

        #print(resp.json.get("price"))
