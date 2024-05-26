# Dylan Nelson
# February 14, 2024
# list_in_a_dictionary.py

# This program will give an example of placing a list within a dictionary

# Creates a dictionary that has a list within
pizza = {
    'crust': 'thick',
    'toppings': ['pepperoni', 'mushrooms', 'olives',],
}

# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza."
      "\nYour toppings are:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
