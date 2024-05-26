# Dylan Nelson
# May 09, 2024
# preventing_modifying_lists.py

# This script is functionally similar to how the modifying_lists.py script
# The difference is that the list unprinted_models will not be modified

# This script will pass the contents of one list into another list. Permanently modifying both lists
unprinted_models = ['robot', 'snake', 'panda', 'skull']
printed_models = []
# Print out both lists
print(f'Unfinished designs: {unprinted_models}. \nFinished designs: {printed_models}.')

def print_designs(first, last):
    '''This function will print out the unprinted_models 
    list into the printed_models list'''
    while first:
        print(first)
        current_design = first.pop()
        print(f'Printing {current_design}...')
        last.append(current_design)
        print(f'Done.')

def state_prints(printed_models):
    '''Prints out each individual item within the printed_models list'''
    for model in printed_models:
        print(f'{model.title()} Has been printed.')

# Print out both lists again to show that they were actually switched over
# The list is in reverse order to how it was started, this is because the 'pop'
# method uses a last-in first-out method
# By adding a semicolon to 'unfinished_models' [:], we indicate that we want 
# to send a slice to the function rather than the list, and by default if we 
# include no indeces for the slice then we send a full copy of the list
print_designs(unprinted_models[:], printed_models)
state_prints(printed_models)
print(f'Original un-altered designs list: {unprinted_models}. \nFinished designs list: {printed_models}.')
