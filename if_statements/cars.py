# Dylan Nelson
# February 08, 2024
# cars.py

# Creates a list of different car brands
cars = ['audi', 'ford', 'mazda', 'gmc', 'bmw', 'mercedes', 'toyota', 'dodge']

# Prints each car brand with the correct capitalization rules
for car in cars:
    if car == 'bmw'or car == 'gmc':
        print(car.upper())
    elif car != 'bmw' or car != 'gmc':
        print(car.title())

# Creates a list of different car brands with random capitalization errors
cars = ['audI', 'Ford', 'mazDa', 'gmc', 'BMW', 'MercedEs', 'toYOta', 'doDGe']

# First this converts all of the strings into lower case, 
# then prints each car brand with the correct capitalization rules
for car in cars:
    if car.lower() == 'bmw'or car == 'gmc':
        print(car.upper())
    elif car.lower() != 'bmw' or car != 'gmc':
        print(car.title())
