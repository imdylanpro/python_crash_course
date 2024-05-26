# Dylan Nelson
# May 05, 2024
# modifying_lists.py

# This script will pass the contents of one list into another list. Permanently modifying both lists
unprinted_models = ['robot', 'snake', 'panda', 'skull']
printed_models = []
# Print out both lists
print(f'Unfinished designs: {unprinted_models}. \nFinished designs: {printed_models}.')

def print_designs(first, last):
    '''This function will print out the unprinted_models 
    list into the printed_models list'''
    while unprinted_models:
        current_design = first.pop()
        print(f'Printing {current_design}...')
        last.append(current_design)
        print(f'Done.')

def state_prints(printed_models):
    '''Prints out each individual item within the printed_models list'''
    for model in printed_models:
        print(f'{model.title()} Has been printed.')

# Print out both lists again to show that they were actually switched over
# The list is in reverse order to how it was started, this is because the 'pop' method uses a 
# last-in first-out method
print_designs(unprinted_models, printed_models)
state_prints(printed_models)
# print(f'Unfinished designs: {unprinted_models}. \nFinished designs: {printed_models}.')