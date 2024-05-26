#Dylan Nelson
#april 15, 2024
#user_input.py

# Demonstrates the input function
message = input("Tell me something and I will repeat it back to you. ")
print(f"{message}")

# Including more text with the input function
name = input("What is your name? ")
print(f"Hello {name}!")

# Using a prompt that is more than 1 line
prompt = "Hello there, in this example we will have 2 lines. "
prompt += "\nHere is the second line. How does that sound? "
response = input(prompt)
print(f"{response}")

# Using numbers in input function, user input is always interpreted as a string
# unless it is then converted using the int() class, however a case handler
# will need to be added to account for the situations when the user inputs
#  something that is not a number.
age = input("How old are you? ")
try:
    age = int(age)
    print(f"You are {age} years old.")
except Exception as e:
    print(f"Error: {age} is not a number.")
