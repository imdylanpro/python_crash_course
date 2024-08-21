# Dylan_Nelson
# August 13, 2024
# cubes.py

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# Set the style for the graph.
plt.style.use('Solarize_Light2')

# Assigns the figure and an array of axis.
fig, ax = plt.subplots()

# Plot the values, add a colormap.
ax.scatter(x_values, y_values, c = y_values,cmap = plt.cm.Reds, s = 10)

# Configure table.
ax.set_title("Cubed Numbers", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Cubed Values", fontsize = 14)

# Customize the tick label to show standard numbers.
ax.ticklabel_format(style='plain')

# Display the graph.
plt.show()