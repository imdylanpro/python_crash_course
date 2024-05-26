# Dylan Nelson
# April 30, 2024
# keywords.py

# Function that describes my pet type and their name
def my_pet(pet_type, pet_name):
    '''Assigns the species of pet and its' name and prints the result.'''
    print(f'I have a {pet_type}.')
    print(f'His name is {pet_name.title()}.')

#The variables are directly assigned when passing them into the function
my_pet(pet_type = 'crocodile', pet_name = 'cranky')
