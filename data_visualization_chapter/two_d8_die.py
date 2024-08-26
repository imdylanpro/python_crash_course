# Dylan Nelson
# August 25, 2024
# two_d8_die.py

# Import neccessary modules.
from die import Die
import plotly.express as px

# Create two D8 sided dice.
die_1 = Die(8)
die_2 = Die(8)

# Roll the die and store the data into a list
results = []
for rolls in range(100):
    die_1_result = die_1.roll()
    die_2_result = die_2.roll()
    result = die_1_result + die_2_result
    results.append(result)

# Sort the results of the rolls into a list according 
#   to the number of times a number was rolled.
frequencies = []
max_possible_num = die_1.num_sides + die_2.num_sides
poss_nums = range(2, max_possible_num)

for rolls in poss_nums:
    frequency = results.count(rolls)
    frequencies.append(frequency)

# Create the chart with the relevant data.
title = 'Results of Rolling Two D8 Dice 1000 Times'
labels = {'x': 'Value', 'y': 'Number of Times Rolled.'}
fig = px.bar(x=poss_nums, y=frequencies, title=title, labels=labels)

# Customize the chart
fig.update_layout(xaxis_dtick=1)

fig.write_html('two_D8_dice_rolls.html')

# Opent an html page in web browser and display the chart.
fig.show()