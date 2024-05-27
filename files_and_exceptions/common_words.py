# Dylan Nelson
# May 26, 2024
# common_words.py

'''Reads how many times a word that the user defines is present inside a text 
file.'''

from pathlib import Path

path = Path("text_files/fiddler's_farewell.txt")

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('Could not find file.')
else:
    print('Type "q" to quit at any time.')
    while True:
        word = input('Which word do you want to search for? ')
        if word == 'q':
            break
        occurances = contents.lower().count(f'{word} ')
        print(f'"{word}" appears a total of {occurances} times.')
