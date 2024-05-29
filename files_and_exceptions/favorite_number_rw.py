# Dylan Nelson
# May 28, 2024
# favorite_number_rw.py

from pathlib import Path
import json

path = Path('json_files/favorite_number.json')

def greet_user(path):
    '''Greet the user with their favorite number'''
    number = read_number(path)
    if number:
        print(f'Your favorite number is {number}.')
    else:
        write_number(path)
    change_number(number)

def write_number(path):
    '''Write a number into memory.'''
    number = input("What is your favorite number? ")
    try:
        number = int(number)
    except ValueError:
        print('Please enter a number.')
    else:
        # Save in json file format
        contents = json.dumps(number)
        # write the number to the file path
        path.write_text(contents)
        return number

def read_number(path):
    '''Read the number that is stored in the filepath.'''
    if path.exists():
        # Read the contents from the file.
        contents = path.read_text(encoding='utf-8')
        # Strip the json file type properties to make it a txt file equivalent.
        number = json.loads(contents)
        return number
    else:
        return None

def change_number(number):
    '''Allows the user to change their favorite number if they want to.'''

    choice = input('Would you like to change your favorite number? ').lower()
    if choice == 'yes' or choice == "y":
        write_number(path)
        number = read_number(path)
        print(f'Got it. We changed your favorite number to {number}.')
    else:
        print(f'Your favorite number did not change. It is still {number}.')

greet_user(path)
