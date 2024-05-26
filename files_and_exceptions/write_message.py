# Dylan Nelson
# May 24, 2024
# write_message.py

'''This program will be used to write into a text file.'''

from pathlib import Path

# define a file path to use, if the file doesn't already exist Python will
# create it.
path = Path('/DN_Python/python_crash_course/files_and_exceptions'
            '/text_files/write_message.txt')
# Write a string into the file
path.write_text('Hello, my name is Dylan!')
contents = path.read_text()
print(contents)

# Whenever "".write_text" is used it will erase the contents of whatever is 
# currently in the file, so if there is previous data that is present you 
# can risk losing it. The previous string written above is replaced here.
path.write_text('Testing!')
print(path.read_text())

# Because we stored the original value that we wrote to the text file we can 
# combine the two strings into one
contents += '\n' + path.read_text()
print(contents)