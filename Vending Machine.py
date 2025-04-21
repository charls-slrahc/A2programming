# dictionaries storing the key-value items
food_menu = {
    "A1": {"Item": "Lay's Chips", "Price": 1.50, "Stock": 5},
    "A2": {"Item": "Doritos Chips", "Price": 2.00, "Stock": 5},
    "A3": {"Item": "Takis Chips", "Price": 5.00, "Stock": 5},
    "B1": {"Item": "Snickers Chocolate", "Price": 3.00, "Stock": 5},
    "B2": {"Item": "Twix Chocolate", "Price": 2.50, "Stock": 5},
    "B3": {"Item": "M&Ms", "Price": 4.00, "Stock": 5},
    "C1": {"Item": "Oreos", "Price": 2.50, "Stock": 5},
    "C2": {"Item": "Parle G", "Price": 1.50, "Stock": 5},
    "C3": {"Item": "Ritz", "Price": 1.00, "Stock": 5}
}

drink_menu = {
    "D1": {"Item": "Fanta", "Price": 2.50, "Stock": 5},
    "D2": {"Item": "Sprite", "Price": 2.50, "Stock": 5},
    "D3": {"Item": "Coke", "Price": 2.50, "Stock": 5},
    "E1": {"Item": "Water", "Price": 1.00, "Stock": 5},
    "F1": {"Item": "Apple Juice", "Price": 1.50, "Stock": 5},
    "F2": {"Item": "Orange Juice", "Price": 1.50, "Stock": 5}
}
# dictionary combination
main_menu = {
    "Food": food_menu,
    "Drinks": drink_menu
}

#displays the main menu and its arrangements
def display_main_menu():
    print("=== Welcome to Charls' Vending Machine ===\n")
    for category, items in main_menu.items():
        print(f"--- {category} ---")
        for code, details in items.items(): #for loop to assign each key-value pair
            item = details['Item']
            price = details['Price']
            stock = details['Stock']
            print(f"{code}: {item} - ${price:.2f} (Stock: {stock})")
        print()

def item_code(code): # fetching the code once the user inputs the following code
    for category in main_menu: #for loop to fetch the code following the variable conversion
        if code in main_menu[category]:
            return main_menu[category][code]
    return None

def vending_machine(): #main vending machine code 
    while True: #while loop when the vending machine process
        display_main_menu()

        input_code = input("Please enter the item code (or type 'exit' to quit): ").upper() #input statement for the code

        if input_code == 'EXIT': #if else loop when the user exits the vending machine
            print("Thanks for visiting! Goodbye")
            break

        item_selected = item_code(input_code) #code conversion variable

        if not item_selected: #if loop for invalid code input
            print("Invalid code. Please try again.\n")
            continue

        if item_selected['Stock'] <= 0: #if loop for items that are out of stock
            print(f"Sorry, {item_selected['Item']} is out of stock.\n")
            continue

        price = item_selected['Price'] #if loop for the price items
        print(f"You selected: {item_selected['Item']} - ${price:.2f}")

        try: # try and except iterables for currency transaction
            money_inserted = float(input("Please insert money: $"))
        except ValueError:
            print("Invalid amount entered. Transaction cancelled.\n")
            continue

        if money_inserted < price: #if loop for transaction validation
            print("Not enough money inserted. Transaction cancelled.\n")
            continue

        change = round(money_inserted - price, 2)
        item_selected['Stock'] -= 1
        #print statements for the item selected for dispensing and the remaining change returned, following by the goodbye message. 
        print(f"\nDispensing {item_selected['Item']}...")
        print(f"Change returned: ${change:.2f}")
        print("Thank you for your purchase!\n")


vending_machine()