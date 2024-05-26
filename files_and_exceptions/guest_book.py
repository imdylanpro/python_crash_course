# Dylan Nelson
# May 25, 2024
# guest_book.py

'''Asks the user for their name and stores the information into a text file.'''

# import path library.
from pathlib import Path

# Define the file path.
path = Path('/DN_Python/python_crash_course/files_and_exceptions'
            '/guest_book.txt')

# while loop to ask people for their name.
print('Gathering names for guest book. Enter "q" to quit.')
while True:
    contents = path.read_text()
    name = input('What is your name? ').title()
    if name != 'Q':
        # store into a text file, combining the original contents with the new 
        # message.
        stored_message = f'{contents}\n{name}'
        path.write_text(stored_message)  
    else:
        break

# Print a message so the user knows that they are no longer in the while loop.
print(f'Thanks everyone! I have stored your names in the location: {path}')
