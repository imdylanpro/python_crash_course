# Dylan Nelson
# August 21, 2024
# rw_visual.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the user wants to make more.
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    # build the figure and axes of the graph.
    fig, ax = plt.subplots(figsize=(15,8), dpi = 100)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, 
               s=1, edgecolors='none')
    ax.set_aspect('equal')

    # Highlight the start and the finish of the graph.
    ax.scatter(0,0, c='blue', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
               edgecolors='None', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Generate another walk? (y/n): ")
    if keep_running == 'n':
        break