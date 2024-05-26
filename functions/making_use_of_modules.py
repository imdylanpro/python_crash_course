# Dylan Nelson
# May 10, 2024
# making_use_of_modules.py

# This script demonstrates how to import modules and use their contents
'''This script requires "pizza_module.py" to be in the same directory to 
work'''

# import will search for the file named "pizza_module.py" and it will get ALL 
# of the functionality that is associated with the module when this method is 
# used it will need to be specified that we are taking "make_pizza" from 
# "pizza" module
import pizza_module
pizza_module.make_pizza(12, 'cheese', 'olives')

# The as keyword can be used to rename the module itself. Here 
# "pizza_module.py" is renamed to be just "p"
import pizza_module as p
p.make_pizza(13, 'steak', 'tacos', 'salsa')

# When we explicitly call out the module and function we can then call the 
# function solely by name
from pizza_module import make_pizza
make_pizza(16, 'cheese', 'jalapenos', 'chicken')

# If an imported function has an undesireable name it can be renamed using the 
# "as" keyword. Here "make_pizza" is renamed to be "n"
from pizza_module import make_pizza as n
n(19, 'cheese', 'olives', 'jalapenos', 'chicken', 'red sauce', 
  'banana peppers')

# This will import all functions from a module, the asterisk denotes all. It 
# will also allow for the functions to be called without calling out the 
# module. This method is not advised as it can import a lot of unnecessary data
# and cause errors if there are naming conflicts 
from pizza_module import *
