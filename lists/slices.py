# Dylan Nelson
# February 6, 2024
# slices.py

cars = ["honda", "ford", "mazda", "toyota", "subaru"]

# Print the message "The first three items in the list are:", then use a slice to print the first three items from the list.
# Leaving the first number in the slice operator blank it will default to the first number in the list.
print(f"The first three items in the list are:", cars[:3])

# Print the message "The middle items in the list are:", then use a slice to print the 3 middle items in the list
print(f"The middle items in the list are: ", cars[1:4])

# Print the same as before but for the last 3 items in the list
# By leaving the second number on the slice operator blank it will use the last item in the list
print(f"The last three items in the list are: ", cars[2:])

# The three examples from above will actually print the list itself with the commas, apostrophes, and brackets included.

# Prints the item that is 3rd from the end of the list
print(f"The last three items in the list are: ", cars[-3])
