# Dylan Nelson
# May 27, 2024
# favorite_number_reader.py

'''Read the contents of a file containing a number.'''

from pathlib import Path
import json

# Define the filepath.
path = Path('json_files/favorite_number.json')
# Read the contents from the file.
contents = path.read_text(encoding='utf-8')
# Strip the json file type properties to make it a txt file equivalent.
number = json.loads(contents)
print(f'I remembered your favorite number, it is {number}!')
