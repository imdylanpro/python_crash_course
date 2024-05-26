# Dylan Nelson
# May 22, 2024
# die.py

from random import randint

class Die():
    '''attempts to model the behavior of a die.'''

    def __init__(self, sides):
        '''Initializes an instance of a die.'''
        self.sides = sides

    def roll_die(self):
        '''Rolls the die using the number of sides given, returning a random 
        value.'''
        rand_number = randint(1, self.sides)
        print(f'You have rolled the {self.sides} sided die, '
              f'the number is {rand_number}.')

def die_functions():
    my_sixi_side_die = Die(6)
    my_20_side_die = Die(20)

    my_dies = [my_sixi_side_die, my_20_side_die]

    for die in my_dies:
        for i in range(10):
            die.roll_die()

die_functions()
