import CoinBaseExchangeAuth
import MarketSocket
import requests
from threading import Timer


class AuthenticatedClient:

    def __init__(self, CoinBaseExchangeAuth, api_url):
        self.auth = CoinBaseExchangeAuth
        self.api_url = api_url
	self.market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')



#if price = "Market" buy at market price
    def buy(self, size, price, product_id):
        size = str(size)
        price = str(price)
	if(price == "market"):
		price = str(self.market.getPrice())
	
        r = requests.get(self.api_url + 'accounts', auth=self.auth)

        order = {
			      'size': ".01",
			      'price': price,
			      'side': 'buy',
			      'product_id': product_id
			   	}


        r = requests.post(self.api_url + 'orders', json=order, auth=self.auth)
        print(r.json())

        print(r.status_code)
		#print("------------------BOUGHT-------------")
        print(order)


    def sell(self, size, price, product_id):
        size = str(size)
        price = str(price)
	if(price == "market"):
		price = str(self.market.getPrice())
        r = requests.get(self.api_url + 'accounts', auth=self.auth)

        order = {
			      'size': size,
			      'price': price,
			      'side': 'sell',
			      'product_id': product_id
			   	}


        r = requests.post(self.api_url + 'orders', json=order, auth=self.auth)
        print(r.json())

        print(r.status_code)
		print("------------------SOLD-------------")
        print(order)
