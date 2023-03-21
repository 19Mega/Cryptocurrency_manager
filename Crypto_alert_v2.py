import requests
from datetime import datetime
from datetime import date 
import time
import winsound

class Crypto():
    def __init__(self, name,short_name, api_url):
        
        self.name = name
        self.short_name = short_name
        self.api_url = api_url
        
        
    def extraer_datos(self):
        response = requests.get(self.api_url)
        data = response.json()
        
        price = data['market_data']['current_price']['usd']
        percent_change_1h = data['market_data']['price_change_percentage_1h_in_currency']['usd']
        percent_change_24h = data['market_data']['price_change_percentage_24h_in_currency']['usd']
        percent_change_7d = data['market_data']['price_change_percentage_7d_in_currency']['usd']

        return price, percent_change_1h, percent_change_24h, percent_change_7d    


    def estado_actual(self):        
        price, percent_change_1h, percent_change_24h, percent_change_7d = self.extraer_datos()
        
        print(f"\033[1;33;100mPrecio actual {self.name} (USD): {price} \033[0m")
        
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



class Compra(Crypto):
    def __init__(self, total_usd, total_crypto, year=0, month=0, day=0):

        self.total_usd =  total_usd
        self.total_crpyto = total_crypto
        self.fecha = date(year, month, day)



Bitcoin = Crypto("Bitcoin", "BTC", "https://api.coingecko.com/api/v3/coins/bitcoin")
Ethereum = Crypto("Ethereum", "ETH", "https://api.coingecko.com/api/v3/coins/ethereum")
Polygon_Matic = Crypto("Polygon-Matic", "MAT", "https://api.coingecko.com/api/v3/coins/matic-network")


compra_eth_1 = Compra(515.78, 0.314, year=2023, month=2, day= 15)
compra_eth_1.name = "Ethereum"
compra_eth_1.short_name = "ETH"
compra_eth_1.api_url = "https://api.coingecko.com/api/v3/coins/ethereum"

compra_eth_2 = Compra(45.59, 0.029, year=2023, month=2, day= 26)
compra_eth_2.name = "Ethereum"
compra_eth_2.short_name = "ETH"
compra_eth_2.api_url = "https://api.coingecko.com/api/v3/coins/ethereum"

compra_eth_3 = Compra(101.00, 0.065, year=2023, month=2, day= 28)
compra_eth_3.name = "Ethereum"
compra_eth_3.short_name = "ETH"
compra_eth_3.api_url = "https://api.coingecko.com/api/v3/coins/ethereum"

compra_mat_1 = Compra(279.98, 230.128, year=2023, month=3, day= 3)
compra_mat_1.name = "Polygon-Matic"
compra_mat_1.short_name = "MAT"
compra_mat_1.api_url = "https://api.coingecko.com/api/v3/coins/matic-network"




contador_bucle = 0
while 1:
    
    ahora = datetime.now()
    hora_actual = ahora.strftime("%H:%M:%S")
    print(f"N° de bucle: {contador_bucle} | HORA ACTUAL: {hora_actual} |")
    
    
    # A mejorar: sacar precio y mostrarlo asi solamente usamos 1 vez la api
    Bitcoin.estado_actual()
    Ethereum.estado_actual()
    Polygon_Matic.estado_actual()
    
    # Crypto.extraer_datos() >> return >> price, percent_change_1h, percent_change_24h, percent_change_7d    
    # precio = lugar [0] de la tupla
    price_btc = Bitcoin.extraer_datos()[0]
    price_eth = Ethereum.extraer_datos()[0]
    price_mat = Polygon_Matic.extraer_datos()[0]
    
    print(" - - - - - - - - - - - - - - - - - - - - ")
    print(f"\033[1;35;45m Compra {compra_eth_1.fecha} {compra_eth_1.short_name}: {compra_eth_1.total_crpyto} = {compra_eth_1.total_usd} USD \033[0m")
    print(f"\033[48;5;17m\033[38;5;51m## Valor actual de {compra_eth_1.short_name}: {compra_eth_1.total_crpyto} = {(compra_eth_1.total_crpyto * price_eth):.2f} USD\033[0m")
    ganancia_eth_1 = ((compra_eth_1.total_crpyto * price_eth) - compra_eth_1.total_usd)
    print(f"\033[1;36;100m## Ganancia actual: {(ganancia_eth_1):.2f} USD \033[0m")
    print(" - - - - - - - - - - - - - - - - - - - - ")
    
    
    print(f"\033[1;35;45m Compra {compra_eth_2.fecha} {compra_eth_2.short_name}: {compra_eth_2.total_crpyto} = {compra_eth_2.total_usd} USD \033[0m")
    print(f"\033[48;5;17m\033[38;5;51m## Valor actual de {compra_eth_2.short_name}: {compra_eth_2.total_crpyto} = {(compra_eth_2.total_crpyto * price_eth):.2f} USD\033[0m")
    ganancia_eth_2 = ((compra_eth_2.total_crpyto * price_eth) - compra_eth_2.total_usd)
    print(f"\033[1;36;100m## Ganancia actual: {(ganancia_eth_2):.2f} USD \033[0m")
    print(" - - - - - - - - - - - - - - - - - - - - ")  
    
    
    print(f"\033[1;35;45m Compra {compra_eth_3.fecha} {compra_eth_3.short_name}: {compra_eth_3.total_crpyto} = {compra_eth_3.total_usd} USD \033[0m")
    print(f"\033[48;5;17m\033[38;5;51m## Valor actual de {compra_eth_3.short_name}: {compra_eth_3.total_crpyto} = {(compra_eth_3.total_crpyto * price_eth):.2f} USD\033[0m")
    ganancia_eth_3 = ((compra_eth_3.total_crpyto * price_eth) - compra_eth_3.total_usd)
    print(f"\033[1;36;100m## Ganancia actual: {(ganancia_eth_3):.2f} USD \033[0m")
    print(" - - - - - - - - - - - - - - - - - - - - ") 
    
    
    print(f"\033[1;35;45m Compra {compra_mat_1.fecha} {compra_mat_1.short_name}: {compra_mat_1.total_crpyto} = {compra_mat_1.total_usd} USD \033[0m")
    print(f"\033[48;5;17m\033[38;5;51m## Valor actual de {compra_mat_1.short_name}: {compra_mat_1.total_crpyto} = {(compra_mat_1.total_crpyto * price_mat):.2f} USD\033[0m")
    ganancia_mat_1 = ((compra_mat_1.total_crpyto * price_mat) - compra_mat_1.total_usd)
    print(f"\033[1;36;100m## Ganancia actual: {(ganancia_mat_1):.2f} USD \033[0m")
    print(" - - - - - - - - - - - - - - - - - - - - ")

    
    print(f"\033[1;37;44m USD TOTAL GASTADO: {(compra_eth_1.total_usd + compra_eth_2.total_usd + compra_eth_3.total_usd + compra_mat_1.total_usd):.2f} \033[0m")
    print(f"\033[1;37;44m USD TOTAL ACTUAL: {((compra_eth_1.total_crpyto * price_eth) + (compra_eth_2.total_crpyto * price_eth)+(compra_eth_3.total_crpyto * price_eth)+(compra_mat_1.total_crpyto * price_mat)):.2f} \033[0m")
    print(" ")

    
    contador_bucle += 1
    time.sleep(60)
    