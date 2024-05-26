# Dylan Nelson
# April 22, 2024
# deli.py

# create a list for finished an unfinished sandwich orders
finished_sandwiches = []
unfinished_sandwiches = ['tuna sandwich', 'pastrami sandwich', 'ham sandwich', 'pastrami sandwich', 'turkey sandwich', 'pastrami sandwich', ]

# loop through the unfinished sandwich list and remove all mention of 'pastrami sandwich'

print(f'Here is the list of unfinished sandwiches: {unfinished_sandwiches}.')
print(f'We do not have any more pastrami, we are unable to make pastrami sandwiches.')

while 'pastrami sandwich' in unfinished_sandwiches:
    unfinished_sandwiches.remove('pastrami sandwich')

print(f'Here is the NEW list of unfinished sandwiches: {unfinished_sandwiches}.')

while unfinished_sandwiches:

    # create a variable to hold the sandwich order that is being list swapped
    swappa = unfinished_sandwiches.pop()

    # add the item to the other list
    print(f'Finishing order: {swappa}.')
    finished_sandwiches.append(swappa)

print(f'Orders all done: {finished_sandwiches}.')
