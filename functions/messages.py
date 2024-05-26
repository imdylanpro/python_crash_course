# Dylan Nelson
# May 10, 2024
# messages.py

messages = ['hello', 'goodbye', 'good', 'bad']
sent_messages = []
print(f'List 1: {messages}.\nList 2: {sent_messages}')

def show_messages(my_list):
    '''Prints all of the contents of the list passed into the function'''
    for my_string in my_list:
        print(f'{my_string}')

def send_messages(my_list):
    '''Takes the contents from "messages" list, removes then and places them
    into "sent_messages"'''
    while my_list:
        message = my_list.pop()
        print(f'Printing message... {message}. ')
        print('Done.')
        sent_messages.append(message)

# show_messages(messages)
# By adding/removing the semicolon the original list is either left unaffected or it 
send_messages(messages[:])
print(f'List 1: {messages}.\nList 2: {sent_messages}')
