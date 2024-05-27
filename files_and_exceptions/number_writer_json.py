# Dylan Nelson
# May 26, 2024
# number_writer_json.py

'''Write values into a .json file format.'''

from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('json_files/numbers.json')
# json.dumps will store the contents in .json file format
contents = json.dumps(numbers)
path.write_text(contents)
