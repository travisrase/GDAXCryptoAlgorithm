class main:

#	import Purchase
#	import PublicClient
#	import WebsocketClient
#	import Purchase
	import CoinBaseExchangeAuth
	import MarketSocket
	import Time

	global acceptable_loss,  total_loss, clock

	#User Input information for keys
	#User_API_Key = input("Input the API KEY: ")
	#User_Passphrase = input("Input the Passphrase: ")
	#User_Secret= input("Input the secret Key: ")

	#buy terminal





	coinbase_terminal = CoinBaseExchangeAuth.CoinbaseExchangeAuth(api_key,api_secret, api_passphrase)
	#coinbase_terminal = CoinbaseExchangeAuth(User_API_Key, User_Secret, User_Passphrase)
	market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')



	#acceptable_loss = input("What is the maximum tolerable loss: ")
	#total_loss = 0

	while True: # conditions for running the program




		#Pull data from gdax

		#Algorithm:
			#when conditions are met create purchase object for given coin

main()
