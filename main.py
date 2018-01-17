

from CoinBaseExchangeAuth import CoinbaseExchangeAuth
import MarketSocket
import requests
from threading import Timer
from AuthenticatedClient import AuthenticatedClient
from Algorithm import Algorithm
from UserSocket import UserSocket


class main:




	global acceptable_loss,  total_loss, clock, market, coinbase_terminal, setPrice, dollar_buy

	#User Input information for keys
	User_API_Key = ""
	User_Secret= ""
	User_Passphrase = ""

	#dollar_buy = float(input("How much do you want to spend?: "))
	#setPrice = float(input("What is the price you want to buy at? :"))

	#buy terminal

	api_url = 'wss://ws-feed.gdax.com'

	#coinbase_terminal = CoinbaseExchangeAuth(User_API_Key,User_Secret, User_Passphrase)
	#coinbase_terminal = CoinbaseExchangeAuth()


	#market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')
	#auth_client = AuthenticatedClient(coinbase_terminal, market, api_url)
	#algo = Algorithm("dummy", auth_client, market, "10.00", "LTC-USD")

	user = UserSocket(api_url, )

	user.openWS()
	user.listen()
















main()
