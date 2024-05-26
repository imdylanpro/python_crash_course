# Dylan Nelson
# April 29, 2024
# greeting.py

# Create a simple function which does one thing: Say hello to the user
def greet_user():
    print('Hello user!')
greet_user()

# Creates a function that passes in a variable to be used.
# Variables are not global by default, meaning they must be passed into a function to be used
name = 'Charles'
def user_name(user):
    print(f'Hello, {user}')
user_name(name)