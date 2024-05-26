# Dylan Nelson
# February 12, 2024
# dictionary_intro.py

# A dictionary is created using the curly brackets {},
# dictionaries are great for storing multiple different, 
# parameters to a variable

aliens = {'alien_0', 'alien_1', 'alien_2'}
alien_0 = {'color': 'green', 'points': 5, 'speed': 'fast'}
alien_1 = {'color': 'purple', 'points': 15, 'speed': 'medium'}
alien_2 = {'color': 'yellow', 'points': 25, 'speed': 'fast'}

new_points = alien_0['points']
# print(f'You just earned {new_points} points!')

# adds new key-value points to the dictionary, these are the coordinates
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# prints out the value of speed, but using the get command if speed is not,
# found then print the second string
# print(alien_0.get('speed', 'we could not find that value!'))

# Assigns the position modifier to a variable
if alien_0['speed'] == 'slow':
    x_increment = 1
if alien_0['speed'] == 'medium':
    x_increment = 2
if alien_0['speed'] == 'fast':
    x_increment = 3

# Prints the original value and then prints the newly modified x position
print(f"{alien_0['x_position']}")
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"{alien_0['x_position']}")

# Prints the associated key-value pairs for the dictionary alien_0
print(alien_0)

#  Deletes the color key-value pair associated with the alien_0 dictionary
del alien_0['color']

# Prints the associated key-value pairs for the dictionary alien_0
print(alien_0)
