# Dylan Nelson
# February 09, 2024
# ififif.py

# This program will show a use case where only if statements are allowed
# This situation comes up when all statements need to be checked
# This is different from an if | elif | else case

requested_toppings = ['pepperoni', 'sausage', 'anchovies', 'extra cheese',
                       'olives', 'chicken']

# Prints a message for each topping that is included in requested_toppings list
# if 'pepperoni' in requested_toppings:
#     print('Pepperoni will be added to your pizza!')
# if 'sausage' in requested_toppings:
#     print('Sausage will be added to your pizza!')
# if 'anchovies' in requested_toppings:
#     print('Anchovies will be added to your pizza!')
# if 'extra cheese' in requested_toppings:
#     print('Extra cheese will be added to your pizza!')
# if 'olives' in requested_toppings:
#     print('Olives will be added to your pizza!')s
# if 'chicken' in requested_toppings:
#     print('Chicken will be added to your pizza!')
# if 'pickles' in requested_toppings:
#     print('Pickles will be added to your pizza!')

for requested_topping in requested_toppings:
    if requested_topping in requested_toppings:
        print(f'{requested_topping.title()} will be added to your pizza!')
