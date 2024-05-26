# Dylan Nelson
# May 24, 2024
# learning_python.py

'''This script will look through the contents of a file called: 
"learning_python.txt" it will then print the output once as a single string 
then store the items in a list and print the list.'''

# import the path module from the path library
from pathlib import Path

# establish the filepath to look into. I am going to just use the absolute 
# filepath for demonstrations sake.
path = Path('/DN_Python/python_crash_course/files_and_exceptions/text_files'
        '/learning_python.txt')

# Print the contents of the file.
contents = path.read_text().rstrip()
print(contents)

# store the lines into a list then print the list
my_list = []
for lines in contents.splitlines():
    # Due to the formatting used in the text file there are some lines that are
    # empty, we can eliminate them from our list to ensure that there are no 
    # empty strings stored in our list. 
    if lines == '':
        # "pass" is simply used as a placeholder since we don't acutally want 
        # any operations to happen when an empty stirng is found.
        pass
    else:
        my_list.append(lines)

print(my_list)
# .replace does not overwrite the contents of the variable
print(contents.replace('Python', 'C'))
