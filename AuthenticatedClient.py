import CoinBaseExchangeAuth
import MarketSocket
import requests
from threading import Timer


class AuthenticatedClient:

      def __init__(self, CoinBaseExchangeAuth, api_url):
          self.auth = CoinBaseExchangeAuth
          self.api_url = api_url


     #size and price may be given as ints or strings, product_id must be a string
     def buy(size, price, product_id):
         size = str(size)
         price = str(price)
         r = requests.get(api_url + 'accounts', auth=self.auth)
         order = {
			      'size': size,
			      'price': price,
			      'side': 'buy',
			      'product_id': product_id,
			   	}

        r = requests.post(api_url + 'orders', json=order, auth=auth)
		print(r.status_code)
		print("------------------BOUGHT-------------")
		print(order)
