# Dylan Nelson
# February 12, 2024
# nested_dictionaries.py

# This program will give an example of using a dictionary within a dictionary

alien_0 = {'color': 'green', 'points': 5, 'speed': 'fast'}
alien_1 = {'color': 'purple', 'points': 15, 'speed': 'medium'}
alien_2 = {'color': 'yellow', 'points': 25, 'speed': 'fast'}
aliens = ['alien_0', 'alien_1', 'alien_2']

for alien in aliens:
    print(f'Dictionary: {alien}.')

# Makes an empty list for storing aliens
aliens = []

# Makes a list of 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 10, 'speed': 'slow',}
    aliens.append(new_alien)

# Using a slice the first 3 aliens are modified to be different
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Using a slice to change the aliens from 15-20, the slice uses the first 
#number to indicate the first index location to work with and the second number
# to indicate the second number to work with.
for alien in aliens[10:20]:
    alien['color'] = 'purple'
    alien['points'] = 3
    alien['speed'] = 'slow'

# Use a slice to change the last three aliens to be different
for alien in aliens[(len(aliens)-3):]:
    if alien['color'] == 'green':
        alien['color'] = 'blue'
        alien['points'] = 30
        alien['speed'] = 'very fast'

# The len function reports back the number of items in the list
print(f'The total number of aliens created is {len(aliens)}')
print(aliens)

# Accesses each of the keyword, value pairs within the "aliens" list
for a in aliens:
    # .items will allow us to work with the dictionary contents
    for k, v in a.items():
        print(f'{k} is the keyword, {v} is the value.')
