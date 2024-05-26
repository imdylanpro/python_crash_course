# Dylan Nelson
# April 21, 2024
# while_lists.py

unconfirmed_users = ['alice', 'mark', 'jeremy', 'nicholas']

confirmed_users = []

# move users from one list to another

while unconfirmed_users:
    # the pop command removes the default last item in an index from the list
    current_user = unconfirmed_users.pop()

    #place the popped user into the second list
    print(f'Confirming user: {current_user.title()}')
    confirmed_users.append(current_user)

# show that the users have been moved into a different list
for confirmed_user in confirmed_users:
    print(f'The verified users are: {confirmed_user.title()}')
