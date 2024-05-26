# Dylan Nelson
# May 10, 2024
# arbitrary_arguments.py

def pizza_toppings(*toppings):
    '''Creates a tuple of the item "toppings" '''
    print('\nCreate a pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

def make_pizza(size, *toppings):
    '''Makes a pizza with given parameters, positional and arbitrary'''
    print(f'\nCreate a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

pizza_toppings('pepperoni')
pizza_toppings('pineapple', 'olives', 'bacon')
make_pizza(12, 'cheese', 'jalapenos', 'pepperoni')
