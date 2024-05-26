# Dylan Nelson
# February 08, 2024
# if_elif_els.py

# This program will demonstrate the if elif else statements and where they
# should be used. 

age = 6

# Prints custom admission cost message based upon the age variable
if age < 4:
    print("Your admission cost is 5$, because you are under 4 years old.")
elif age < 18:
    print("Your admission cost is 10$ because you are under 18 years old.")
else:
    print("Your admission cost is $12.")

# When one criteria is validated none of the other conditionals are checked
# Notice how the else: statement does not need a conditional
