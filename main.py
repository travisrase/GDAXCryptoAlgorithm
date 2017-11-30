class main:

#	import Purchase
#	import PublicClient
#	import WebsocketClient
#	import Purchase
	import CoinBaseExchangeAuth
	import MarketSocket
	import time

	global acceptable_loss,  total_loss, clock, market, coinbase_terminal

	#User Input information for keys
	User_API_Key = input("Input the API KEY: ")
	User_Passphrase = input("Input the Passphrase: ")
	User_Secret= input("Input the secret Key: ")
	dollar_buy = input("How much do you want to spend?: ")
	setPrice = input("What is the price you want to buy at? :")

	#buy terminal





	coinbase_terminal = CoinBaseExchangeAuth.CoinbaseExchangeAuth(User_API_Key,User_Secret, User_Passphrase)
	#coinbase_terminal = CoinbaseExchangeAuth(User_API_Key, User_Secret, User_Passphrase)
	market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')



	#acceptable_loss = input("What is the maximum tolerable loss: ")
	#total_loss = 0

	while True: # conditions for running the program

		#time interval code
		if market.getMarketPrice() >= setPrice:

			size1 = setPrice * dollar_buy
			test = CoinbaseExchangeAuth(api, secret, passphrase)

			api_url = 'https://api.gdax.com/'
			auth = coinbase_terminal
			r = requests.get(api_url + 'accounts', auth=auth)

			order = {
			      'size': size1,
			      'price': setPrice,
			      'side': 'buy',
			      'product_id': 'LTC-USD',
			   	}

			r = requests.post(api_url + 'orders', json=order, auth=auth)





main()
