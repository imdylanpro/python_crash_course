# Dylan Nelson
# May 25, 2024
# alice.py

'''Shows how to handle the error encountered when trying to read a file that 
does not exist in the supplied directory file path.'''

from pathlib import Path
# When using the Path class from pathlib, it starts in the directory you are 
# currently inside already.
path = Path('text_files/alice.txt')

# UTF-8 is a variable-length character encoding standard used for electronic 
# communication. It is typically used when the system encoding that the file 
# was written on does not match the encoding of the system you are using. 
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f'Sorry, the file {path} does not exist.')
else:
    # Count the number of words that are in "alice.py"
    words = contents.split()
    num_words = len(words)
    print(f'The file "{path}" has about {num_words} words.')