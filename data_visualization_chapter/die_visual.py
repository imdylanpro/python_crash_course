# Dylan Nelson
# August 23, 2024
# die_visual.py

from die import Die
import plotly.express as px

# Create a D6
die = Die()

# Make some rolls then include the rolls into a list.
results = []
for i in range(1000):
    results.append(die.roll())

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of Rolling One D6 1,000 Times."
labels = {'x': 'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()