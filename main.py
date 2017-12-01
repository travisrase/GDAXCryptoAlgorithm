

from CoinBaseExchangeAuth import CoinbaseExchangeAuth
import MarketSocket
import requests
from threading import Timer
from AuthenticatedClient import AuthenticatedClient
from Algorithm import Algorithm


class main:




	global acceptable_loss,  total_loss, clock, market, coinbase_terminal, setPrice, dollar_buy

	#User Input information for keys
	#User_API_Key = input("Input the API KEY: ")
	#User_Secret= input("Input the secret Key: ")
	#User_Passphrase = input("Input the Passphrase: ")

	#dollar_buy = float(input("How much do you want to spend?: "))
	#setPrice = float(input("What is the price you want to buy at? :"))

	#buy terminal





	api_url = 'https://api.gdax.com/'

	#coinbase_terminal = CoinBaseExchangeAuth.CoinbaseExchangeAuth(User_API_Key,User_Secret, User_Passphrase)
	coinbase_terminal = CoinbaseExchangeAuth()


	market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')

	auth_client = AuthenticatedClient(coinbase_terminal, api_url)

	algo = Algorithm("dummy", auth_client, market, ".01", "LTC-USD")



	algo.secondDerivBuyAlgo()













main()
