# Dylan Nelson
# May 26, 2024
# addition_calculator.py

'''This script will add two numbers together while handling the common 
exceptions that can arise.'''

print('Enter two numbers and I will add them together.')
print('Type "q" to escape.')
while True:
    first_number = input('\nWhat is the first number? ')
    if first_number == 'q':
        break
    second_number = input('What is the second number? ')
    if second_number == 'q':
        break
    try:
        addition = int(first_number) + int(second_number)
    except ValueError:
        print(f'You need to enter a number!')
    else:
        print(f'Answer: {addition}')
