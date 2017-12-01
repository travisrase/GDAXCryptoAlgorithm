import CoinBaseExchangeAuth
import MarketSocket
import requests
from threading import Timer


class AuthenticatedClient:

    def __init__(self, CoinBaseExchangeAuth, api_url):
        self.auth = CoinBaseExchangeAuth
        self.api_url = api_url




    def buy(self, size, price, product_id):
        size = str(size)
        price = str(price)
        r = requests.get(self.api_url + 'accounts', auth=self.auth)
        print(type(size))
        print(type(price))
        order = {
			      'size': size,
			      'price': price,
			      'side': 'buy',
			      'product_id': product_id
			   	}
        print(self.api_url + 'orders')
        print(self.auth)
        print(order)
        r = requests.post(self.api_url + 'orders', json=order, auth=self.auth)
        print(r)

        print(r.status_code)
		#print("------------------BOUGHT-------------")
        print(order)
