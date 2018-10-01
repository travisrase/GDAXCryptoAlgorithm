

from CoinBaseExchangeAuth import CoinbaseExchangeAuth
import requests
from Ticker import Ticker
from threading import Timer
from AuthenticatedClient import AuthenticatedClient
from Algorithm import Algorithm
from UserSocket import UserSocket
from MarketData import MarketData
import time


class main:
	User_API_Key = ""
	User_Secret= ""
	User_Passphrase = ""
	coinbase_terminal = CoinbaseExchangeAuth(User_API_Key,User_Secret, User_Passphrase)

	market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')
	auth_client = AuthenticatedClient(coinbase_terminal, market, api_url)
	algo = Algorithm("dummy", auth_client, market, "10.00", "LTC-USD")

	UserSocket = UserSocket(coinbase_terminal)
	channels = ["ticker"]
	UserSocket.subscribe(["LTC-USD"], channels)

main()
