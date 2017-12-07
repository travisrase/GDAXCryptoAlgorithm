import CoinBaseExchangeAuth
import MarketSocket
import requests
from threading import Timer


class AuthenticatedClient:

    def __init__(self, CoinBaseExchangeAuth, MarketSocket, api_url):
        self.auth = CoinBaseExchangeAuth
        self.api_url = api_url
        self.market = MarketSocket



#if price = "Market" buy at market price
    def buy(self, size, price, product_id):
        size = str(size)
        price = str(price)
        if(price == "market"):
		          price = str(self.market.getPrice())

        r = requests.get(self.api_url + 'accounts', auth=self.auth)
        order = {
			      'size': size,
			      'price': price,
			      'side': 'buy',
			      'product_id': product_id,
                  'post_only' : 'true'
			   	}

        r = requests.post(self.api_url + 'orders', json=order, auth=self.auth)
        return(r.json())
        print(r.json())

        print(r.status_code)
		#print("------------------BOUGHT-------------")
        print(order)

    def checkOrder(self, order_id):

        resp = requests.get(self.api_url + 'orders' + "/" + str(order_id), auth=self.auth)

        if resp.status_code != 200:
            print(resp.status_code)
              # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        else:
            return resp

    def cancelOrder(self, order_id):

        resp = requests.delete(self.api_url + 'orders' + "/" + str(order_id), auth=self.auth)

        if resp.status_code != 200:
            print(resp.status_code)
              # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        else:
            return resp



    def sell(self, size, price, product_id):
        size = str(size)
        price = str(price)
        if(price == "market"):
	           price = str(float(self.market.getPrice()) + .01)

        r = requests.get(self.api_url + 'accounts', auth=self.auth)
        order = {
            'size': size,
            'price': price,
            'side': 'sell',
            'product_id': product_id,
            'post_only' : 'true'
        }

        r = requests.post(self.api_url + 'orders', json=order, auth=self.auth)
        return (r.json())
        print(r.json())
        print(r.status_code)
        print("------------------SOLD-------------")
        print(order)
