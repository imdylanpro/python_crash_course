# Dylan Nelson 
# April 22, 2024
# responses.py

# create a dictonary for store cars that people like
cars = {}
polling_active = True

# Start the while loop

while polling_active:
    # Ask the user for their name and what car they like
    name = input('What is your name? ')
    car = input('What kind of car do you have? ')

    # Store the users name and the car that they have in a dictionary
    cars[name] = car

    # Ask if another user wants to take the poll
    repeat = input('Would anyone else like to take the poll? (Yes/No) ')
    if repeat == 'no':
        polling_active = False

print('Poll Results')
for name, car in cars.items():
    print(f'{name} has a {car}.')
