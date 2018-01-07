# CyrptoCurrencyTrading1


Main: Runs algorithms, may run several algorithms simultaniuosly

  Algorithm: 
    Buys and sells through authenticated client based on results from indicies from the MarketData class

    MarketData: 
      Uses Level 1 and Level 2 market data from market socket and computes technical indicies

      (Market or User)Socket: Gets Level 1 and Level 2 market data in real time


    AuthenticatedClient: Allows you to buy and sell currencies 

      CoinbaseExchangeAuth: Used to store API key, API passphrase, and API secret, 
      used for any interaction with either APIs that requires authentication
