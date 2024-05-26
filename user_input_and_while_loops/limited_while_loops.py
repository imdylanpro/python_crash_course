# Dylan Nelson
# April 17, 2024
# limited_while_loops.py

# creates a variable that will iterate the while loop 10 times
loop_iterations = 10

# loop through the variable number and print out a message for each loop
while loop_iterations > 0:
    if loop_iterations != 1:
        print(f'There are {loop_iterations} iterations left before this is finished. ')
    else:
        print(f'There is {loop_iterations} iteration left before this is finished. ')
    loop_iterations -= 1
