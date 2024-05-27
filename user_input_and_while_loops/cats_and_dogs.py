# Dylan Nelson
# May 26, 2024
# cats_and_dogs.py

'''Reads the contents of the files "cats.txt" and "dogs.txt" handles errors 
correctly in case the files do not exist.'''

from pathlib import Path

files = ['cats.txt', 'dogs.txt', 'cows.txt']

for file in files:
    path = Path(f'text_files/{file}')
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f'\nCould not find file {path}.')
    else:
        names = contents.split()
        print(f'\n{file}')
        for name in names:
            print(f'-{name.title()}')
