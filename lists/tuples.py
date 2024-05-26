# Dylan Nelson
# February 07, 2024
# tuples.py

# Creates a tuple, which is an immutable list
coordinates = (200, 50, 75)

# Prints the contents of the coordinates tuple in the order they are requested
print(coordinates[2])
print(coordinates[0])
print(coordinates[1])

# Prints the contents of the coordinates tuple sequentially in a for loop
for item in coordinates:
    print(item)

# Creates a tuple of food items
foods = ('bagel', 'turnip', 'beef', 'carrot', 'radish')

print("Here is the original foods tuple:")
for food in foods:
    print(food)

# A tuple cannot be edited as it is immutable, however it can be rewritten like any variable
foods = ('bagel', 'bread', 'turnip', 'beef', 'carrot', 'turky' 'radish')

print("Here is the modified foods tuple:")
for food in foods:
    print(food)
