import os
from data import MENU, resources

end = False

money = 0


# clear console on windows
def clear_windows():
    lambda: os.system('cls')


# clear console on osx
def clear_osx():
    lambda: os.system('clear')


MENU['espresso']['ingredients']['milk'] = 0

while not end:
    # Prompt user, ask what they would like? Check user input, once drink is dispensed, this prompt should show
    #  again
    user_input: str = input('What would you like? (espresso/latte/cappuccino):\n').lower()
    # when 'off' is entered, the coffee machine turns off - code halts
    if user_input == 'off':
        print('closing for maintenance')
        end = True
        clear_windows()
        clear_osx()
    # When the user enters 'report' to the prompt,  a report should be generated that shows the current values of
    # resources
    elif user_input == 'report':
        print(f'water: {resources["water"]}\nmilk: {resources["milk"]}\ncoffee: {resources["coffee"]}\nmoney: ${money}')
    elif user_input in MENU:
        # calculate price of bev
        price = float(MENU[user_input]["cost"])
        # check if resources are greater than minimum amount needed to create a drink
        # check if resources are sufficient
        # if not
        for ingredient in resources:
            if resources[ingredient] - MENU[user_input]['ingredients'][ingredient] < 0:
                print(f'sorry, there is not enough {ingredient} to make your {user_input}')
                break
            # otherwise
            elif resources[ingredient] - MENU[user_input]['ingredients'][ingredient] >= 0:
                continue
        else:
            print(f'Price: ${price} ')
            print('please insert coins')
            money_in_quarters = float(input('how many quarters?')) * .25
            money_in_dimes = float(input('how many dimes?')) * .10
            money_in_nickels = float(input('how many nickels?')) * .05
            money_in_pennies = float(input('how many pennies?')) * .01
            payment_sum = money_in_quarters + money_in_dimes + money_in_nickels + money_in_pennies
            if payment_sum < price:
                print('Sorry, that\'s not enough money. Money refunded!')
            elif payment_sum >= price:
                change = round(payment_sum - float(MENU[user_input]['cost']), 2)
                print('...')
                print('...')
                print('...')
                print(f'Here is ${change} in change.')
                for bev in MENU:
                    if bev == user_input:
                        water_deduced = resources['water'] - (MENU[user_input]['ingredients']['water'])
                        resources['water'] = water_deduced
                        coffee_deduced = resources['coffee'] - (MENU[user_input]['ingredients']['coffee'])
                        resources['coffee'] = coffee_deduced
                        if user_input == 'espresso':
                            milk_deduced = resources['milk'] - 0
                        else:
                            milk_deduced = resources['milk'] - (MENU[user_input]['ingredients']['milk'])
                            resources['milk'] = milk_deduced
                        money += MENU[user_input]['cost']
                # then vend the bev
                print(f'Here is your {user_input}☕. Enjoy!')
