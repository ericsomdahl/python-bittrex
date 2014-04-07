
import urllib
import urllib2
import json
import time
from datetime import datetime

BUY_ORDERBOOK = 'buy'
SELL_ORDERBOOK = 'sell'
BOTH_ORDERBOOK = 'both'
'''
   see https://bittrex.com/Home/Api
'''
class bittrex(object):
    def __init__(self, APIKey):
        self.APIKey = APIKey
        self.public_set = set(['getmarkets','getcurrencies','getticker','getmarketsummaries','getorderbook','getmarkethistory'])
        
    def api_query(self, method, req={}):
        if method in self.public_set:
            request_url = 'https://bittrex.com/api/v1/public/' + method + '?'
        else:
            request_url = 'https://bittrex.com/api/v1/' + method + '?'
        
        request_url += urllib.urlencode(req)
            
        if method not in self.public_set:
            request_url += '&apikey=' + self.APIKey
        
        ret = urllib2.urlopen(urllib2.Request(request_url))
        return json.loads(ret.read())
    
    #get_markets Used to get the open and available trading markets at Bittrex along with other meta data.
    #Parameters
    #None
    def get_markets(self):
        return self.api_query('getmarkets')
    
    #get_currencies Used to get all supported currencies at Bittrex along with other meta data.
    #Parameters
    #None
    def get_currencies(self):
        return self.api_query('getcurrencies')
    
    #get_ticker Used to get the current tick values for a market.
    #Parameters
    #parameter    required    description
    #market    required    a string literal for the market (ex: BTC-LTC)
    def get_ticker(self, symbol):
        return self.api_query('getticker', {'market': symbol})
    
    #get_market_summaries  Used to get the last 24 hour summary of all active exchanges
    #Parameters
    #None
    def get_market_summaries(self):
        return self.api_query('getmarketsummaries')
    
    #Used to get retrieve the orderbook for a given market
    #Parameters
    #parameter    required    description
    #market    required    a string literal for the market (ex: BTC-LTC)
    #type    required    buy, sell or both to identify the type of orderbook to return.  Use constants BUY_ORDERBOOK, SELL_ORDERBOOK, BOTH_ORDERBOOK
    #depth    optional    defaults to 20 - how deep of an order book to retrieve. Max is 100
    def get_orderbook(self, symbol, depth_type, depth=20):
        return self.api_query('getorderbook', {'market': symbol, 'type': depth_type, 'depth': depth})
    
    #/market/getmarkethistory
    #Used to retrieve the latest trades that have occured for a specific market.
    #
    #Parameters
    #parameter    required    description
    #market    required    a string literal for the market (ex: BTC-LTC)
    #count    optional    a number between 1-100 for the number of entries to return (default = 20)
    def get_market_history(self, symbol, count):
        return self.api_query('getmarkethistory', {'market': symbol, 'count': count})
        
