from datetime import date 
from datetime import datetime
import json, os, keyboard, signal, requests, time, winsound
from crypto_function import api_update

################################################################################################


def clear_console():
    os.system('cls')

#################################################################################################
salir = False

def detectar_tecla_escape(event):
    global salir
    if event.name == 'esc':
        print("\nSe ha presionado la tecla Escape. Saliendo...")
        salir = True

keyboard.on_press(detectar_tecla_escape)

#################################################################################################

def crypto_register(crypto):
    short_name = crypto
    puchase_usd = float(input("Enter the buy amount in USD: "))
    purchase_crypto = float(input(f"Enter the buy amount in {crypto}: "))
    year = int(input("Enter year of purchase: "))
    month = int(input("Enter month of purchase: "))
    day = int(input("Enter day of purchase: "))

    try:
        with open('crypto_db.json') as f:
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
                "purchase_usd": puchase_usd,
                "purchase_crypto": purchase_crypto,
                "year": year,
                "month": month,
                "day": day
                })
    
    with open('crypto_db.json', 'w') as f:
        json.dump(data, f, indent=2)

#################################################################################################

def delete_crypto_register():
    try:
        with open('crypto_db.json') as f:
            data = json.load(f)
    except FileNotFoundError:
            data = []

    print("Existing records:")
    for record in data:
        print(f"ID: {record['id']}, Crypto: {record['short_name']}, USD spend: {record['purchase_usd']}, Crypto amount: {record['purchase_crypto']}, Date of purchase: {record['day']}/{record['month']}/{record['year']}")

    id_to_delete = int(input("Ingrese el ID del registro que desea eliminar: "))

    filtered_data = [record for record in data if record["id"] != id_to_delete]

    with open('crypto_db.json', 'w') as f:
        json.dump(filtered_data, f, indent=2)

    print(f"ID: {id_to_delete} has been successfully deleted.")

#################################################################################################

def crypto_sold_register():
    try:
        with open('crypto_db.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    print("Registros existentes:")
    for record in data:
        print(f"ID: {record['id']}, Crypto: {record['short_name']}, USD spend: {record['purchase_usd']}, Crypto amount: {record['purchase_crypto']}, Date of purchase: {record['day']}/{record['month']}/{record['year']}")

    sell_id = int(input("Enter the ID of the register that was sold: "))

    for record in data:
        if record['id'] == sell_id:
            sell_value = float(input("Ingrese el valor de venta en USD: "))
            profit = sell_value - record['purchase_usd']
            record['sell_value'] = sell_value
            record['profit'] = profit

            try:
                with open('crypto_sales.json') as f:
                    sales_data = json.load(f)
            except FileNotFoundError:
                sales_data = []

            sales_data.append(record)

            with open('crypto_sales.json', 'w') as f:
                json.dump(sales_data, f, indent=2)

            break
    else:
        print(f"No se encontró un registro con ID {sell_id}")
        return

    filtered_data = [record for record in data if record["id"] != sell_id]

    with open('crypto_db.json', 'w') as f:
        json.dump(filtered_data, f, indent=2)

    print(f"ID: {sell_id} has been removed from database.json and added to sales_made.json successfully.")


#################################################################################################

def view_all_sold_crypto_registers():
    try:
        with open('crypto_sales.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    print("Existing records:")
    for record in data:
        print(f"Crypto: {record['short_name']}, USD spend: {record['purchase_usd']}, Crypto amount: {record['purchase_crypto']}, Date of purchase: {record['day']}/{record['month']}/{record['year']}, Sell value: {record.get('sell_value', '-')}, Profit: {record.get('profit', '-')}")

    total_profit = sum(record.get('profit', 0) for record in data)
    print(f"Total profits: {total_profit} USD")

#################################################################################################

def view_all_crypto_register():
    try:
        with open('crypto_db.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    print("Existing records:")
    for record in data:
        print(f"Crypto: {record['short_name']}, USD spend: {record['purchase_usd']}, Crypto amount: {record['purchase_crypto']}, Date of purchase: {record['day']}/{record['month']}/{record['year']}")


#################################################################################################
#######################################        MENU        ######################################
#################################################################################################

while True:
    print("")
    print("1- Start application")
    print("2- Register Crypto-Purchase")
    print("3- Delete Crypto-Purchase")
    print("4- Register Sale")
    print("5- See the list of the actual registers")
    print("6- See the list of Purchases Profits")
    print("7- Exit")
    print("")

    opcion = int(input("Enter an option number: "))
    
    clear_console()
    
    if opcion == 1:
        
        contador_bucle = 0

        while not salir:
            ahora = datetime.now()
            hora_actual = ahora.strftime("%H:%M:%S")
            print(f"N° de bucle: {contador_bucle} | HORA ACTUAL: {hora_actual} |")
            
            # Sacamos los precios actuales de las cryptomonedas
            crypto_prices = api_update()
            
            actual_btc_price = crypto_prices [0]
            actual_eth_price = crypto_prices [1]
            actual_mat_price = crypto_prices [2]
            
            try:
                with open('crypto_db.json') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = []


            btc_objects =[]
            eth_objects =[]
            mat_objects =[]
            
            for record in data:
                short_name = record["short_name"]
                puchase_usd = record["purchase_usd"]
                purchase_crypto = record["purchase_crypto"]
                year = record["year"]
                month = record["month"]
                day = record["day"]
            
                if short_name == "BTC":
                    btc_objects.append(record)
                elif short_name == "ETH":
                    eth_objects.append(record)
                elif short_name == "MAT":
                    mat_objects.append(record)

            
            for btc_purchase in btc_objects:
                
                float_crypto = float(btc_purchase['purchase_crypto'])
                float_usd = {btc_purchase['purchase_usd']}
                actual_crypto_in_usd = float_crypto * actual_btc_price
                y={btc_purchase['year']}
                m={btc_purchase['month']}
                d= {btc_purchase['day']}
                
                print(f"Crypto: {btc_purchase['short_name']} | Date: {d}/{m}/{y} | Amount BTC: {float_crypto} >> Buy Value: {float_usd} USD | Actual value: {actual_crypto_in_usd} USD | Profit: {(actual_crypto_in_usd-float_usd)}")

            for eth_purchase in eth_objects:
                
                float_crypto = float(eth_purchase['purchase_crypto'])
                float_usd = {eth_purchase['purchase_usd']}
                actual_crypto_in_usd = float_crypto * actual_btc_price
                y={eth_purchase['year']}
                m={eth_purchase['month']}
                d= {eth_purchase['day']}
                
                print(f"Crypto: {eth_purchase['short_name']} | Date: {d}/{m}/{y} | Amount BTC: {float_crypto} >> Buy Value: {float_usd} USD | Actual value: {actual_crypto_in_usd} USD ")
                

            for mat_purchase in mat_objects:

                float_crypto = float(mat_purchase['purchase_crypto'])
                float_usd = {mat_purchase['purchase_usd']}
                actual_crypto_in_usd = float_crypto * actual_btc_price
                y={mat_purchase['year']}
                m={mat_purchase['month']}
                d= {mat_purchase['day']}
                
                print(f"Crypto: {mat_purchase['short_name']} | Date: {d}/{m}/{y} | Amount BTC: {float_crypto} >> Buy Value: {float_usd} USD | Actual value: {actual_crypto_in_usd} USD ")


            contador_bucle += 1
            time.sleep(60)


    elif opcion == 2:
        print("What do you want to record?")
        print("AVAILABLE OPTIONS:")
        print("1- BTC - Bitcoin ")
        print("2- ETH - Ethereum ")
        print("3- MAT - Polygon-Matic ")

        crypto_option = int(input("Enter option number: "))

        if crypto_option == 1:
            crypto_register("BTC")
        elif crypto_option == 2:
            crypto_register("ETH")
        elif crypto_option == 3:
            crypto_register("MAT")
    
    
    elif opcion ==3:
        delete_crypto_register()
        
    elif opcion == 4:
        crypto_sold_register()
        
    elif opcion == 5:
        view_all_crypto_register()
        
    elif opcion == 6:
        view_all_sold_crypto_registers()
        
    elif opcion== 7:
        print("Program closed successfully.")
        exit()


