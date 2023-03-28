import requests
from datetime import date 
from datetime import datetime
import time
import winsound


def api_update():
    
    apis = ["https://api.coingecko.com/api/v3/coins/bitcoin", "https://api.coingecko.com/api/v3/coins/ethereum", "https://api.coingecko.com/api/v3/coins/matic-network"]
    crypto_names = ["BTC","ETH","MAT"]
    crypto_prices = []    
    
    for i in range(0,3):
        
        response = requests.get(apis[i])
        data = response.json()

        price = data['market_data']['current_price']['usd']
        percent_change_1h = data['market_data']['price_change_percentage_1h_in_currency']['usd']
        percent_change_24h = data['market_data']['price_change_percentage_24h_in_currency']['usd']
        percent_change_7d = data['market_data']['price_change_percentage_7d_in_currency']['usd']

        print(f"\033[1;33;100m Precio actual {crypto_names[i]}: {price} USD\033[0m")
        
        
        if percent_change_1h >= 0:
            print("\033[32m % de cambio en 1 hora: +{:.2f}%\033[0m".format(percent_change_1h))
        else:
            print("\033[31m % de cambio en 1 hora: {:.2f}%\033[0m".format(percent_change_1h))
        if percent_change_24h >= 0:
            print("\033[32m % de cambio en 24 horas: +{:.2f}%\033[0m".format(percent_change_24h))
        else:
            print("\033[31m % de cambio en 24 horas: {:.2f}%\033[0m".format(percent_change_24h))
        if percent_change_7d >= 0:
            print("\033[32m % de cambio en 7 días: +{:.2f}%\033[0m".format(percent_change_7d))
        else:
            print("\033[31m % de cambio en 7 días: {:.2f}%\033[0m".format(percent_change_7d))
        
        crypto_prices.append(float(price))
        
        
    return crypto_prices


