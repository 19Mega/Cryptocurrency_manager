import requests
from datetime import date 
import time
import winsound

class Crypto():
    def __init__(self, short_name,value_in_dollars, value_in_crypto, year, month, day):
        
        __purchase_number = 0
        
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
        
        # Current own values 
        self.current_usd_profit_value = self.price * self.purchase_in_crypto
        self.current_usd_profit_state = self.purchase_in_dollars - self.current_profit_value
        
        # Sale values
        self.sold_value = None
        self.sold_date = None
        self.is_sold = False

    def update_prices(self):
        response = requests.get(self.api_url)
        data = response.json()
        
        self.price = data['market_data']['current_price']['usd']
        self.percent_change_1h = data['market_data']['price_change_percentage_1h_in_currency']['usd']
        self.percent_change_24h = data['market_data']['price_change_percentage_24h_in_currency']['usd']
        self.percent_change_7d = data['market_data']['price_change_percentage_7d_in_currency']['usd']

    def show_prices(self):
        
        print(f"\033[1;33;100mPrecio actual {self.name} (USD): {self.price} \033[0m")
        
        if self.percent_change_1h >= 0:
            print("\033[32m % de cambio en 1 hora: +{:.2f}%\033[0m".format(self.percent_change_1h))
        else:
            print("\033[31m % de cambio en 1 hora: {:.2f}%\033[0m".format(self.percent_change_1h))
        if self.percent_change_24h >= 0:
            print("\033[32m % de cambio en 24 horas: +{:.2f}%\033[0m".format(self.percent_change_24h))
        else:
            print("\033[31m % de cambio en 24 horas: {:.2f}%\033[0m".format(self.percent_change_24h))
        if self.percent_change_7d >= 0:
            print("\033[32m % de cambio en 7 días: +{:.2f}%\033[0m".format(self.percent_change_7d))
        else:
            print("\033[31m % de cambio en 7 días: {:.2f}%\033[0m".format(self.percent_change_7d))