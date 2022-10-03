import coffee_menu
import time

# 1. Print Report
# 2. Check Resources
# 3. Process Coins
# 4. Verify Transaction
# 5. Make Beverage

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def run():
    menu = coffee_menu.MENU
    selected_item_name = ""
    credit = 0.0

    print(f"\nMENU")
    for item in menu:
        print(f"{item.title()} : ${menu[item]['cost']:.2f}")

    while selected_item_name not in menu:
        selected_item_name = input(f"\nEnter the item name: ").lower()
        if selected_item_name not in menu:
            print("\nInvalid item")

    selected_item = menu[selected_item_name]

    low_resources = check_resources(selected_item)
    if len(low_resources) > 0:
        print("")
        for res in low_resources:
            print(f"Low on {res.title()}!")
        input("\nPlease select a different beverage.")
        run()

    while credit < selected_item['cost']:
        print(f"Cost: ${float(selected_item['cost']) - credit}")
        payment = input(f"Please insert payment: (d)ollar (q)uarter (c)redit: ")
        if payment == 'd':
            credit += 1
        if payment == 'q':
            credit += 0.25
        if payment == 'c':
            credit = selected_item['cost']

    print(f"Thank You!\n")

    dispense(selected_item)


def print_report():
    print("Printing Report\n")
    for res in resources:
        print(f"{res}: {resources[res]}")


def check_resources(item):
    missing_resources = []
    for res in item['ingredients']:
        if item['ingredients'][res] > resources[res]:
            missing_resources.append(res)
    return missing_resources


def dispense(item):
    for ingredient in item['ingredients']:
        print(f"consuming {item['ingredients'][ingredient]} {ingredient}")
        resources[ingredient] -= item['ingredients'][ingredient]
    print("\nDispensing...")
    for i in range(1, 4):
        time.sleep(1)
        print("💧")
    print("Enjoy!")
    input("☕")
    run()


print_report()
run()

