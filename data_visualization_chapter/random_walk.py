# Dylan Nelson
# August 21, 2024
# random_walk.py

from random import choice

class RandomWalk:
    """Create an instance of a random walk that chooses random x and y paths to
    follow."""

    def __init__(self, num_points=5000):
        """Initialize the attributes associated with the class"""

        self.num_points = num_points

        # Start the x, and the y values at 0.
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Fill in the values for the x_values and y_values for the graph."""

        while len(self.x_values) < (self.num_points):

            # Decide which direction to go and how far to go.
            x_step = self._step_creation()
            y_step = self._step_creation()
            # Reject steps that do not go anywhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
        
    def _step_creation(self):
        """Creates the steps for the graph using random values."""

        direction = choice([-1,1])
        distance = choice([0,1,2,3,4,5,6,7,8])
        step = direction * distance

        return step