
#          Cryptocurrency Manager         #


![Example Image](images/crypto_manager_image.png)

This is a console program designed to keep track of your cryptocurrency purchases and profits. The program uses the CoinGecko API to retrieve the current value of the cryptocurrencies. However, the purchase values are entered manually.

Available Cryptocurrencies: BTC, ETH, MAT

## JSON Files
The program creates two JSON files to store the data:
- crypto_db.json: Stores all the cryptocurrency purchases.
- crypto_sales.json: Stores all the sales made with their corresponding profits.

## Functions

```python
def clear_console():
    """Clears the console output."""
    

def main_menu_exit_key(event):
    """Detects if the 'f4' key is pressed and sets the salir variable to True, which will exit the program."""
    

def crypto_register(crypto):
    """Allows the user to register a new cryptocurrency purchase. 
    The function prompts the user to input the purchase amount in USD, purchase amount in the cryptocurrency, 
    and the purchase date (year, month, and day). The data is then appended to the crypto_db.json file."""
    

def crypto_delete_register():
    """Displays all the current records in crypto_db.json and prompts the user to input the ID of the record they wish to delete. 
    The selected record is then removed from the JSON file."""
    

def crypto_sold_register():
    """Allows the user to register a sale of a previously purchased cryptocurrency. The function prompts the user to input the ID of the cryptocurrency that was sold, 
    the sale value in USD, and calculates the profit from the sale. The record is then removed from crypto_db.json and added to crypto_sales.json."""
    

def view_all_sold_crypto_registers():
    """Displays all the records in crypto_sales.json. If a sale has been made, the profit from the sale is displayed. 
    At the end, the function displays the total profit from all the sales in the file."""
    
