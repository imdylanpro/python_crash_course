# Dylan Nelson
# June 03, 2024
# settings.py

class Settings:
    """A class to store all of the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (192, 192, 192)

        # Archer settings
        self.archer_speed = 3

        # Arrow settings
        self.arrow_speed = 7.0
        self.arrow_width = 2
        self.arrow_length = 14
        self.arrow_color = (58, 6, 3)
        self.arrows_allowed = 10

        # Zombie settings
        self.zombie_speed = 2