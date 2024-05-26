# Dylan Nelson
# May 22, 2024
# file_reader.py

'''This script reads the contents of a file path using the pathlib library.
Note: "pi_digits.txt" will need to be in the same directory or within one of 
the example filepaths in order to function properly.'''

from pathlib import Path
# This line searches for a filepath called "pi_digits.txt" in the current 
# directory.
path = Path('pi_digits.txt')

# This line searches for a filepath called "pi_digits.txt" by starting in the 
# current directory and going into "text_files" folder.
path = Path('text_files/pi_digits.txt')

# The full system path can also be used. Although Windows uses backslash \ in
# its filepaths, it is more appropriate to use forward slash /. Python will 
# automatically use the correct interpretation.
path =Path('/DN_Python/python_crash_course/'
           'files_and_exceptions/text_files/pi_digits.txt')

# rstrip is used to remove the blank line that .read_text causes when gathering
# the string from "pi_digits.txt". This is an example of *method chaining*.
contents = path.read_text().rstrip()
# Print the contents of "pi_digits.py" as a single string.
print(contents)

# Change the path to look for another file.
path =Path('/DN_Python/python_crash_course/'
           'files_and_exceptions/text_files/pi_million_digits.txt')

contents = path.read_text().rstrip()
# Splits the variable "contents" into a list, where each item of the list is a 
# line from the string. The carriage returns or newlines is the delimiter.
lines = contents.splitlines()

# creates a string that is uninterrupted with the first million digits of pi, 
# this is accomplished by stripping the left side of the lines using lstrip().
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

# Create a tuple using slice to have the first 52 chars in "pi_string".
print(f'{pi_string[:52]}')
# Print the length of "pi_string" to show that it is 1 million
print(len(pi_string))

# Asks the user to enter their birthday, then checks if it is in the first 
# million digits of pi.
birthday = input("What is your birthday? Enter in mmddyy format: ")
if birthday in pi_string:
    print("Your birthday is in the first million digits of pi!")
else:
    print("Your birthday is not in the first million digits of pi.")
