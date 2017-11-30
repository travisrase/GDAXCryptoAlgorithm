

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





	api_url = 'https://api.gdax.com/'

	coinbase_terminal = CoinBaseExchangeAuth.CoinbaseExchangeAuth(User_API_Key,User_Secret, User_Passphrase)

	market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')
	
	AuthenticatedClient = AuthenticatedClient.AuthenticatedClient(coinbase_terminal, api_url)



	current_price = 0
	
	recentPriceTable = []
	
	def update():
		current_price = market.getMarketPrice()
		print(current_price)
		
		if current_price >= setPrice:

			size1 = dollar_buy/setPrice
			size1 = str(size1)
			
			AuthenticatedClient.buy(.01, setPrice, 'LTC-USD'





	price_checker = Timer(8, update())

	price_checker.start()


	#acceptable_loss = input("What is the maximum tolerable loss: ")
	#total_loss = 0








main()
