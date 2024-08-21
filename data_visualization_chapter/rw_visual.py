# Dylan Nelson
# August 21, 2024
# rw_visual.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap= s=15)
ax.set_aspect('equal')
plt.show()