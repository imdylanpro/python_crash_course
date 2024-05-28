# Dylan Nelson
# May 27, 2024
# favorite_number_writer.py

from pathlib import Path
import json

path = Path('json_files/favorite_number.json')
number = input('What is your favorite number? ')
try:
    number = int(number)
except ValueError:
    print('Please enter a number.')
else:
    # Save in json file format
    contents = json.dumps(number)
    # write the number to the file path
    path.write_text(contents)
