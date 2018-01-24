

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




	global acceptable_loss,  total_loss, clock, market, coinbase_terminal, setPrice, dollar_buy

	#User Input information for keys
	User_API_Key = "9e9254dc6ff3a31d1c1bf6221adb1e1b"
	User_Secret= "SLvLleh0Q3oKmRh/fSSB83N+9OWSbzgnVp4ccxL7NOFvrRwLODhLHXQvGcd+Szkm3E978uDzTj4yoL4fbiBGCg=="
	User_Passphrase = "Fckmac"

	#dollar_buy = float(input("How much do you want to spend?: "))
	#setPrice = float(input("What is the price you want to buy at? :"))

	coinbase_terminal = CoinbaseExchangeAuth(User_API_Key,User_Secret, User_Passphrase)


	#market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')
	#auth_client = AuthenticatedClient(coinbase_terminal, market, api_url)
	#algo = Algorithm("dummy", auth_client, market, "10.00", "LTC-USD")


	#UserSocket = UserSocket(coinbase_terminal)
	#channels = ["ticker"]
	#UserSocket.subscribe(["LTC-USD"], channels)



	market = MarketData("LTC-USD",coinbase_terminal,.5,10)
	market.runMarketData()
	print("marketPriceTable Updating")
	print("")
	print("")
	time.sleep(10)
	print("RSI")
	print("")
	print(market.getRSI())
	time.sleep(50)
	market.stopMarketData()
	#sleep(100)
	#print(market.getPriceTable())
	#market.stopPriceTable()




main()
