# Dylan Nelson
# June 10, 2024
# arrow.py

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to handle the arrows that are fired by the archer."""

    def __init__(self, tp_game):
        """Create the arrow objects at the archers current location."""
        # Inheret the properties that are already present in the Sprite super class.
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.arrow_color

        # Create an arrow at the origin (0,0) then set the correct location.
        self.rect = pygame.rect(0,0, 
                                self.settings.bullet_width, 
                                self.settings.bullet_length)
        self.rect.midtop = tp_game.archer.rect.midtop

        # Store the bullets rect information as a float value
        self.y = float(self.rect.y)

    def update(self):
        """Move the arrow around the screen."""
        # Update the exact position of the arrow.
        self.y -= self.settings.arrow_speed
        # Update the rect position based upon the float value
        self.rect.y = self.y

    def draw_arrow(self):
        """Draw the arrow to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)