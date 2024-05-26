# Dylan Nelson
# May 10, 2024
# sandwiches.py

def make_sandwich(*args):
    '''Creates a sandwich with as many arguments as the user provides'''
    print('Creating a sandwich with the following toppings: ')
    for items in args:
        print(f'- {items}')

# Call the function three different times with a different number of arguments 
# to prove it wokrs with multiple different values provided
make_sandwich('ham')
make_sandwich('cheese', 'bacon')
make_sandwich('roast beef', 'lettuce', 'swiss cheese', 'mayo')
