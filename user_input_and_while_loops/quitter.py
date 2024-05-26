# Dylan Nelson
# April 16, 2024
# quitter.py

# Define the prompt that the user will see
prompt = 'Go ahead and say something to me and I will repeat it back to you. Say "quit" to stop: '

#While loop that will have a quit condition that it tells the user
message =''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f'{message}')
