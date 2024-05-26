# Dylan Nelson
# May 26, 2024
# word_count.py

'''Returns the approximate number of words in a file'''

from pathlib import Path

def count_words(path):
    '''Splits strings by the whitespace then counts the length of the text 
    file supplied.'''

    try:
        contents = path.read_text()
    except FileNotFoundError:
        # You can choose whether or not to inform the user if the file is not 
        # found the "pass" statement tells Python to do nothing.
        pass
        # print(f'Unable to find file: {path}.'),    
    else:
        words = contents.split()
        word_count = len(words)
        print(f'The file path: {path} approximate word count is: '
              f'{word_count}.')

files = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for file in files:
    path = Path(f'text_files/{file}')
    count_words(path)
