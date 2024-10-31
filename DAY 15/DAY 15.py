MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

user = input("What would you like? (espresso/latte/cappuccino):").lower()
#how much money the machine made:
profit = 0

def show_resources():
    """prints a report"""
    for items in resources:
        print(items +': '+str(resources[items]))#prints the key plus the value
    print(f"Money: {profit}")
# if the user asks for report it will print this
if user == "report":
    print(show_resources())

def resource_check():
    if user == "espresso":
        if MENU[user]["ingredients"]["water"] > resources["water"]:
            print("not enougth water")
            return False
        elif MENU[user]["ingredients"]["coffee"] > resources["coffee"]:
            print("not enough coffee")
            return False
        else:
            return True
    elif user == "latte" or user == "cappuccino":
        if MENU[user]["ingredients"]["water"] > resources["water"]:
            print("not enough water")
            return False
        elif MENU[user]["ingredients"]["coffee"] > resources["coffee"]:
            print("not enough coffee")
            return False
        elif MENU[user]["ingredients"]["milk"] > resources["milk"]:
            print("not enough milk")
            return False
        else:
            return True

def calculate_change():
    """this will calculate the change the user will get """
    change = money_inserted - required_payment
    return change
# coin value
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
#drink prices
P_espresso = 1.50
P_latte = 2.50
P_cappuccino = 3.00
drink_prices = {
 "P_espresso": 1.50,
 "P_latte" : 2.50,
 "P_cappuccino" : 3.00,
}
#user choice of drink and required payment
def req_payment():
    if user == "espresso":
        value = drink_prices['P_espresso']
    elif user == "latte":
        value = drink_prices['P_latte']
    elif user == "P_cappuccino":
        value = drink_prices['P_cappuccino']
    else:
        value = 0
    return value

def process_coins():
    money = QUARTERS * quarters + DIMES * dimes + NICKLES * nickles + PENNIES * pennies
    return money

# ask for payment
run = True
while run:
    user = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user =="off":
        run = False
        if resource_check() == True:
            required_payment = req_payment()

            print("insert some coins")
            quarters = int(input("how many quarters"))
            dimes = int(input("how many dimes"))
            nickles = int(input("how many nickles"))
            pennies = int(input("how many pennies"))
            money_inserted = process_coins()
            print(f"amount paid: {money_inserted}")


            if money_inserted < required_payment:
                print(f"Sorry.Thats not enough money.Money refunded:{money_inserted}")
            elif money_inserted > required_payment:
                change = calculate_change()
                profit = profit + required_payment
                print(f"here is your change: {change}")
            elif money_inserted == required_payment:
                change = 0
                profit = profit + money_inserted

        # print(f"this is profit: {profit}")

            if user== "espresso":
                new_water =  resources["water"]-MENU[user]["ingredients"]["water"]
                new_coffee = resources["coffee"]-MENU[user]["ingredients"]["coffee"]
                resources["water"] = new_water
                resources["coffee"] = new_coffee
            elif user == "latte":
                new_water = resources["water"] - MENU[user]["ingredients"]["water"]
                new_milk =  resources["milk"] - MENU[user]["ingredients"]["milk"]
                new_coffee = resources["coffee"] - MENU[user]["ingredients"]["coffee"]
                resources["water"] = new_water
                resources["milk"] = new_milk
                resources["coffee"] = new_coffee
            elif user == "cappuccino":
                new_water = resources["water"] - MENU[user]["ingredients"]["water"]
                new_milk = resources["milk"] - MENU[user]["ingredients"]["milk"]
                new_coffee = resources["coffee"] - MENU[user]["ingredients"]["coffee"]
                resources["water"] = new_water
                resources["milk"] = new_milk
                resources["coffee"] = new_coffee


            print(resources)
