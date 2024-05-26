# Dylan Nelson
# April 16, 2024
# user_input_numbers.py

# This will use the Modulo operator to determine the remainder
# This will tell the user if the number they input is even or odd

# Ask user for number
number = input("What number? ")

# Use Modulo operator to determine if there is a remainder
# Modulo gives back the remainder of a divison operation
try: 
    number = int(number)
    if int(number) % 2 == 0:
        print(f"Your number: {number} is even.")
    else: 
        print(f"Your number: {number} is odd.")
except Exception as e:
    print(f"You did not supply a number, {number} is not a number.\nError : {e}")

# Ask the user what kind of vehicle would they like
vehicle = input("What vehicle would you like to own? ")
# Repeat the vehicle the user said back to them
print(f"I will see if I can get a {vehicle} for you.")
