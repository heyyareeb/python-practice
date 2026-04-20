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
profit = 0   # stores total money earned
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        break   # turn off machine

    elif choice == "report":
        print(resources)   # show current resources

    elif choice in MENU:
        # get selected drink data
        drink = MENU[choice]
        ingredients = drink["ingredients"]

        # check if resources are enough
        is_enough = True
        for item in ingredients:
            if ingredients[item] > resources[item]:
                print(f"Sorry, there is not enough {item}")
                is_enough = False

        # if resources are enough → continue
        if is_enough:
            print("Please insert coins.")

            # take coin input
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))

            # calculate total money inserted
            total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

            # check if money is enough
            if total_money < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                # calculate and return change
                change = total_money - drink["cost"]
                print(f"Here is ${round(change, 2)} in change.")

                # deduct resources AFTER successful payment
                for item in ingredients:
                    resources[item] -= ingredients[item]

                # add profit ONCE
                profit += drink["cost"]

                # serve coffee
                print(f"Here is your {choice}. Enjoy!")

    else:
        # runs only if input is invalid
        print("Invalid choice, please try again.")
