
import WebsocketClient
import Purchase

class Purchase:


    def __init__(self, API_KEY, Passphrase, Secret, Type_Coin, Price, Number_Coins): #, Algo_Model
        self.API_KEY = API_KEY
		self.Passphrase = Passphrase
		self.Secret = Secret
        self.Type_Coin = Type_Coin
        self.Price = price
        self.Number_Coins = Number_Coins



    #API Client
    client = AuthenticatedClient(API_KEY, Secret, Passphrase)
    #prints accounts (a test)
    print(auth_client.get_accounts())
    #webSocket client
    wsClient = WebsocketClient(url="wss://ws-feed.gdax.com", products="LTC-USD")

    #update size1


    def buy():
        "Method to buy currency"
        clinet.buy(price=Price, #USD # Template
        size=Number_Coins, LTCproduct_id=Type_Coin)

        

    def sell():
        "Method to sell currency"
