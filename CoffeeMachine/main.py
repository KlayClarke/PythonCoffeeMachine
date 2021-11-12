import os
from data import MENU, resources

money = 0


# clear console on windows
def clear_windows():
    lambda: os.system('cls')


# clear console on osx
def clear_osx():
    lambda: os.system('clear')


print(MENU)
# while resources are greater than minimum amount needed to create a drink, run below..
# money_in_quarters = int(input('how many quarters?')) * .25
# money_in_dimes = int(input('how many dimes?')) * .10
# money_in_nickels = int(input('how many nickels?')) * .05
# money_in_pennies = int(input('how many pennies?')) * .01
# payment_sum = money_in_quarters + money_in_dimes + money_in_nickels + money_in_pennies


# TODO: Prompt user, ask what they would like? Check user input, once drink is dispensed, this prompt should show again
user_input: str = input('What would you like? (espresso/latte/cappuccino):\n')
# TODO: Make it so when 'off' is entered, the coffee machine turns off - code halts
if user_input == 'off':
    clear_windows()
    clear_osx()
# TODO: When the user enters 'report' to the prompt,  a report should be generated that shows the current values
elif user_input == 'report':
    print(f'water: {resources["water"]}\nmilk: {resources["milk"]}\ncoffee: {resources["coffee"]}')
    print(f'money = {money}')
elif user_input in MENU:
    print('getting there')

# TODO: When user selects a drink, program should check whether there are sufficient resources to make said drink
# TODO: If there are sufficient resources, prompt user to enter coins AND calculate the monetary value of coins
# TODO: check if user has inserted sufficient amount of money - if so, add cost of drink to machine as profit
# TODO: if user gives too much money, offer change - rounded to two decimal places
# TODO: if transaction is successful and there are enough resources to make drink, deduct said ingredients from machine
# TODO: once all resources are deducted, tell the user 'Here is your {drink}. Enjoy!'
