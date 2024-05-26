# Dylan Nelson
# May 22, 2024
# lottery.py

'''This script simulates how many times you would need to play the lottery in 
order to win. In this lottery system there are 10 numbers and 5 letters. The 
ticket you create is any combination of the letters / numbers included in the 
"nums_letters" tuple.'''

from random import choice
nums_letters = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 'a', 'b', 'c', 'd', 'e')
number_of_cycles, total_cycles = 0, 0
selection = []
my_ticket = [1, 2, 3, 4]
winner = ''

while winner != 'true':
    selection.append(choice(nums_letters))
    number_of_cycles += 1
    total_cycles += 1 
    if my_ticket == selection:
        print(f'WINNER, it took a total of: {total_cycles} attempts.'
              f'Your ticket: {my_ticket}. Winning ticket: {selection}.')
        winner = 'true'
    if number_of_cycles == 4:
        selection = []
        number_of_cycles = 0
