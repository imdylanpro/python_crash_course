# Dylan Nelson
# August 08, 2024
# scatter_squares.py

import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# List by hand
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# Automatically generating list values,
#   y_values uses an in-line for loop to accomplish the auto generation.
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Plots the given coordinates,
#   coordinates or a list of coordinates can be supplied, s is the point size.
ax.scatter(500, 500_000, s = 200)
# The scatter method does not overwrite previous implementations of the method,
#   both will appear on the graph.
# The inclusion of c and cmap add a color map and assign it to the value of c.
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)

# Set chart title and label axis.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Define the axis range
ax.axis([0, 1100, 0 ,1_100_000])

# Customize the tick label based upon preference, default is scientific.
ax.ticklabel_format(style = 'sci')

# Set the size of tick lables
ax.tick_params(labelsize = 14)

# Saves the figure to a file
plt.savefig('squares_plot.png', bbox_inches = 'tight')
# Show the figure.
plt.show()