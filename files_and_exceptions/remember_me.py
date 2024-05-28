# Dylan Nelson
# May 27, 2024
# remember_me.py

from pathlib import Path
import json

path = Path('json_files/username.json')

def get_stored_username(path):
    '''Get stored username if available.'''
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        username = json.loads(contents)
        return username
    else:
        return None
    
def greet_user(path):
    '''Greet the user by name.'''
    username = get_stored_username(path)
    if username:
        print(f'Welcome back {username}.')
    else:
        name_creator()
    change_name(username)

def change_name(username):
    '''Allows the user to change the name stored in 
    "json_files/username.json".'''
    choice = input('Would you like to change your name? ')
    if choice.lower() == 'yes' or choice.lower() == 'y':
        name_creator()
    else:
        print(f'Name not changed. You are still known as {username}.')

def name_creator():
    '''Creates an initial username for the user.'''
    username = input('What is your name? ').title()
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

greet_user(path)
