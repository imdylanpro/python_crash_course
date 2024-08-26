# Dylan Nelson
# August 25, 2024
# dice_visual.py

import plotly.express as px

from die import Die

# Create a D6 and D10 dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls and store the results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling a D6 and D10 Dice 50,000 times."
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize the chart / bar graph.
fig.update_layout(xaxis_dtick=1)

# Save the graph as an html file.
fig.write_html('d6_d10_50,000_rolls.html')

# Display the graph
fig.show()