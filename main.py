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
money = 0

resources = {
    "water": 100,
    "milk": 200,
    "coffee": 100,
}


def check_resources(choice):
    if choice != 'report' or choice != 'off':
        for item in MENU[choice]['ingredients']:
            if MENU[choice]['ingredients'][item] > resources[item]:
                print(f"Sorry there's not enough {item}.")
                return False
            else:
                return True


def update_resource(choice):
    for item in MENU[choice]['ingredients']:
        resources[item] -= MENU[choice]['ingredients'][item]


def process_coins():
    total = int(input("Enter number of quarters: "))*0.25
    total += int(input("Enter number of dimes: "))*0.10
    total += int(input("Enter number of nickles: "))*0.05
    return round(total, 2)


def coffeemaker():
    global money
    choice = True
    while True:
        choice = input("What would you like? 'espresso, latte or cappuccino': ")
        if choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee {resources['coffee']}g")
            print(f"Money ${money}")
            coffeemaker()
            return

        elif choice == 'off':
            choice = False
            print("Goodbye")
            return

        elif check_resources(choice):
            deposit = process_coins()
            cost = MENU[choice]['cost']
            if cost > deposit:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += cost
                change = deposit - cost
                print(f"Here's ${change:.2f} dollars in change.")
                print(f"Here's your {choice} enjoy!")
                update_resource(choice)

        # elif choice == 'latte':
        #     pass
        # elif choice == 'cappuccino':
        #     pass


coffeemaker()

