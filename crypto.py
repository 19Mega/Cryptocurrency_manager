import requests
from datetime import date 
from datetime import datetime
import time
import winsound





class Crypto():
    def __init__(self, short_name,value_in_dollars, value_in_crypto, year, month, day):

        self.short_name = short_name
        self.full_name = None
        self.api_url = None
        
        if short_name == "BTC":
            self.full_name = "Bitcoin"
            self.api_url = "https://api.coingecko.com/api/v3/coins/bitcoin"
        elif short_name == "ETH":
            self.full_name = "Ethereum"
            self.api_url = "https://api.coingecko.com/api/v3/coins/ethereum"
        elif short_name == "MAT":
            self.full_name = "Polygon-Matic"
            self.api_url = "https://api.coingecko.com/api/v3/coins/matic-network"
        
        # Crypto purchesed values
        self.purchase_in_dollars =  value_in_dollars
        self.purchase_in_crypto = value_in_crypto
        self.purchase_value = value_in_dollars / value_in_crypto
        self.purchase_date = date(year, month, day)

        # Current crypto prices 
        self.price = None
        self.percent_change_1h = None
        self.percent_change_24h = None
        self.percent_change_7d = None

        # Sale values
        self.sold_value = None
        self.sold_date = None
        self.is_sold = False


    def current_profit_value(self):
        current_usd_profit_value = self.price * self.purchase_in_crypto
        return current_usd_profit_value
    
    def current_profit_state(self):
        current_usd_profit_value = self.price * self.purchase_in_crypto
        current_usd_profit_state = current_usd_profit_value - self.purchase_in_dollars
        return current_usd_profit_state
