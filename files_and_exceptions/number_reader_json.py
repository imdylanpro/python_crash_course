# Dylan Nelson
# May 27, 2024
# number_reader_json.py

'''This file reads the contents of json files.'''

from pathlib import Path
import json
path = Path('json_files/numbers.json')
# the .json file is just a text file with different formatting which is why we 
# can use .read_text on it.
contents = path.read_text()
# json.loads will interpret "contents" in a json file format.
numbers = json.loads(contents)
print(numbers)
