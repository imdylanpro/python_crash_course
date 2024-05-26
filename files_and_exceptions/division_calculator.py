# Dylan Nelson
# May 25, 2024
# division_calculator

'''Builds a calculator that will '''

try:
    print(5/0)
# Here we can anticipate the divide by zero error so we can handle it.
except ZeroDivisionError:
    print('You cannot divide by zero!')

print('Provide me with two numbers and I will divide them.')
print('Type "q" to quit.')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    # Because the divide by zero error might happen on this line we can place 
    # the try portion here, else can be combined with try-except to ensure that
    # only the portion where we expect an error to be raised is in the "try".
    try:
        # Python will automatically convert the quotient into a float, to 
        # display the trailing decimal places
        answer = int(first_number) / int(second_number)
    # Handles when the user tries to divide by zero
    except ZeroDivisionError:
        print('You cannot divide by zero!')
    # Handles when a user inputs a non-number value
    except ValueError:
        print('You must enter a number!')
    else:
        # print the type of object that the "answer" variable is. This is to 
        # show that the division in Python always converts the result into a
        # float type.
        print(type(answer))
        print(answer)