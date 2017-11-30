

import CoinBaseExchangeAuth
import MarketSocket
import requests
from threading import Timer



class main:




	global acceptable_loss,  total_loss, clock, market, coinbase_terminal, setPrice, dollar_buy

	#User Input information for keys
	User_API_Key = input("Input the API KEY: ")
	User_Secret= input("Input the secret Key: ")
	User_Passphrase = input("Input the Passphrase: ")

	dollar_buy = float(input("How much do you want to spend?: "))
	setPrice = float(input("What is the price you want to buy at? :"))

	#buy terminal







	coinbase_terminal = CoinBaseExchangeAuth.CoinbaseExchangeAuth(User_API_Key,User_Secret, User_Passphrase)

	market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')




	def update():
		current_price = market.getMarketPrice()
		print(current_price)
		
		if current_price >= setPrice:

			size1 = dollar_buy/setPrice
			size1 = str(size1)


			api_url = 'https://api.gdax.com/'
			auth = coinbase_terminal
			r = requests.get(api_url + 'accounts', auth=auth)

			#Manually inputted the buy size and price to fix that problem. We can change all of this later

			order = {
			      'size': '.01',
			      'price': str(setPrice),
			      'side': 'buy',
			      'product_id': 'LTC-USD',
			   	}

			r = requests.post(api_url + 'orders', json=order, auth=auth)
			print(r.status_code)
			print("------------------BOUGHT-------------")
			print(order)




	current_price = 0
	price_checker = Timer(8, update())

	recentPriceTable = []

	price_checker.start()


	#acceptable_loss = input("What is the maximum tolerable loss: ")
	#total_loss = 0








main()
