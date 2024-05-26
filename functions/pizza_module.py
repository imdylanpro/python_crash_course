# Dylan Nelson
# May 10, 2024
# pizza_module.py

# This script is demonstrating how to create a module, 
# this script is used in conjunction with "making_use_of_modules.py"
'''Include in same directory as "making_use_of_modules.py"'''

def make_pizza(size, *toppings):
    '''Makes a pizza with given parameters, positional and arbitrary'''
    print(f'\nCreate a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')
