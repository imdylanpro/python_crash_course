# Dylan Nelson
# May 27, 2024
# remember_me.py

from pathlib import Path
import json

path = Path('json_files/name.json')

def greet_user(path):
    '''Greet the user by name.'''
    user = get_stored_name(path)
    if user:
        print(f'Welcome back {user['name']}. ' 
              f'You are {user['age']} and you live in {user['city']}.')
    else:
        name_creator()
    change_info()

def get_stored_name(path):
    '''Get stored name if available.'''
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        user = json.loads(contents)
        return user
    else:
        return None

def change_info():
    '''Allows the user to change the name stored in 
    "json_files/name.json".'''
    choice = input('Would you like to change your info? ')
    if (choice.lower() == 'yes' 
    or choice.lower() == 'y' 
    or choice.lower() == 'ya'
    or choice.lower() == 'ye'):
        name_creator()
    else:
        user = get_stored_name(path)
        print(f'Name not changed. You are still known as {user['name']}.')

def name_creator():
    '''Creates an initial name for the user.'''
    name = input('What is your name? ').title()
    while True:
        age = input('What is your age? ')
        try:
            age = int(age)
        except ValueError:
            print('You must enter a number.')
        else:
            break
    city = input('What city do you live in? ').title()
    user = {'name'  : f'{name}',
            'age'   : f'{age}',
            'city'  : f'{city}',}
    contents = json.dumps(user)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {name}!")

greet_user(path)
