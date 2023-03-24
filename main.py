import requests
from datetime import date 
from datetime import datetime
import time
import winsound
from crypto import Crypto
import json


def crypto_register(crypto):
    short_name = crypto
    puchase_usd = float(input("Ingrese cantidad de USD en compra: "))
    purchase_crypto = float(input("Ingrese cantidad de BTC en compra: "))
    year = int(input("Ingrese año de compra: "))
    month = int(input("Ingrese mes de compra: "))
    day = int(input("Ingrese dia de compra: "))

    try:
        with open('basededatos.json') as f:
            data = json.load(f)
    except FileNotFoundError:
            data = []    

    if len(data) == 0:
        next_id = 1
    else:
        last_record = data[-1]
        next_id = last_record["id"] + 1

    data.append({
                "id": next_id,
                "short_name": short_name,
                "puchase_usd": puchase_usd,
                "purchase_crypto": purchase_crypto,
                "year": year,
                "month": month,
                "day": day
                })
    
    with open('basededatos.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    #datos = [{"short_name": short_name,
    #        "puchase_usd": puchase_usd, 
    #        "purchase_crypto": purchase_crypto, 
    #        "year": year, 
    #        "month": month, 
    #        "day": day 
    #        }]
    # w es write, si uso esto siempre sustituye el diccionario que le paso
    #with open("basededatos.json", "w") as archivo_json: 
    #    json.dump(datos, archivo_json)
    # si uso "a" = append agrega este diccionario al final


compra_2 = Crypto("ETH", 515.78, 0.314, year=2023, month=2, day= 15)

print(f"1- is_sold: {compra_2.is_sold}")

compra_2.update_prices()
compra_2.show_prices()
# MATIC 838.39824352
print(f"2- Precio actual de ETH: {compra_2.price}")
print(f"3- Precio ETH 1h: {compra_2.percent_change_1h}")
print(f"4- Precio ETH 24h: {compra_2.percent_change_24h}")
print(f"5- Precio ETH 7d: {compra_2.percent_change_7d}")
print(f"6- Api url: {compra_2.api_url}")

print(f"-------------------------------------------------")

print(f"7- Full name: {compra_2.full_name}")
print(f"8- Short name: {compra_2.short_name}")
print(f"9- Buy date: {compra_2.purchase_date}")
print(f"10- Valor ETH en USD en compra: {compra_2.purchase_value}")
print(f"11- USD gastando en compra: {compra_2.purchase_in_dollars}")
print(f"12- USD actual de compra: {compra_2.current_profit_value()}")
print(f"13- Ganancia actual: {compra_2.current_profit_state()}")



                    # MENU:
                    # 1- Iniciar aplicacion
                    # 2- Registrar Compra (pega en mongo db)
                    # 3- Registrar Venta (pega en mongo db)
                    # 4- Ver listado de Compra - Ventas + ganacias 
                    # 5- Salir
                    # 6- 

# MENU:
print("")
print("1- Iniciar aplicación")
print("2- Registrar Compra")
print("3- Registrar Venta")
print("4- Ver listado de Compra/Ventas y ganacias")
print("5- Salir")
print("")

opcion = int(input("Ingrese número de opción: "))


# OPCION 2: REGISTRAR COMPRA

print("Qué desea registrar?")
print("OPCIONES DISPONIBLES:")
print("1- BTC - Bitcoin ")
print("2- ETH - Ethereum ")
print("3- MAT - Polygon-Matic ")

opcion = int(input("Ingrese número de opción: "))

if opcion == 1:
    crypto_register("BTC")
elif opcion == 2:
    crypto_register("ETH")
elif opcion == 3:
    crypto_register("MAT")


#contador_bucle = 0
#while 1:
#    ahora = datetime.now()
#    hora_actual = ahora.strftime("%H:%M:%S")
#    print(f"N° de bucle: {contador_bucle} | HORA ACTUAL: {hora_actual} |")
   
#    contador_bucle += 1
#    time.sleep(60)
