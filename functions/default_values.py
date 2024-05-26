# Dylan Nelson
# May 01, 2024
# default_values.py

# This program will describe the use of default values when calling functions

# function that describes a type of pet and its name with a default species dog
# default values must be listed after the non-defualt values
def my_pet(pet_name, pet_age, pet_type = 'dog', ):
    print(f'''
          My pet is a {pet_type}. 
          His name is {pet_name}. 
          He is {pet_age} years old.
    ''')
my_pet('Tim', 12)
