# Dylan Nelson
# February 07, 2024
# pizza_party.py

# Creates a list of mine and my friends favorite pizzas
mypizzas = ['pepperoni', 'pineapple', 'cheese']
friendpizzas = ['alfredo chicken', 'pepperoni', 'sausage']

# Prints the current lists before anything is added
print(f"Our favorite pizzas are:", "\n", mypizzas, "\n", friendpizzas)

# add another pizza type onto each of the lists
mypizzas.append("mushroom and olive")
friendpizzas.append("chocolate")

# Print the list again after the new pizza styles are added
print(f"Now our favorite pizzas are:", "\n", mypizzas, "\n", friendpizzas)

# Using a for loop the contents can be printed as well

print("My favorite pizzas are: ")
for pizza in mypizzas:
    print(pizza)
