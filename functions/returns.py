# Dylan Nelson
# May 01, 2024
# returns.py

# This program utilizes a function that takes an input for a name and returns 
# a properly formatted and capitalized output.

def format_name(first_name, last_name, middle_name = ''):
    if middle_name != '':
        formatted_name = f'{first_name} {middle_name} {last_name}'
    else:
        formatted_name = f'{first_name} {last_name}'
    return formatted_name.title()

# These three function calls accomplish the same task, just performed 
# differently it is dependant upon how the user how to implement.
print(format_name('dylan', 
                  'nelson'))
print(format_name('james', 
                  'morgan', 
                  middle_name='arthur'))
print(format_name(last_name='McKinley', 
                  first_name='Barriston', 
                  middle_name='Jocko'))
