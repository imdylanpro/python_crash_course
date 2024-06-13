# Dylan Nelson
# June 10, 2024
# arrow.py

import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
    """A class to handle the arrows that are fired by the archer."""

    def __init__(self, tp_game):
        """Create the arrow objects at the archers current location."""
        # Inheret the properties that are already present in the Sprite super class.
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.arrow_color
        self.archer = tp_game.archer

        # Create an arrow at the origin (0,0) then set the correct location.
        if self.archer.facing_up or self.archer.facing_down:
            self.rect = pygame.Rect(0,0, 
                                    self.settings.arrow_width, 
                                    self.settings.arrow_length)
        elif self.archer.facing_left or self.archer.facing_right:
            self.rect = pygame.Rect(0,0, 
                                    self.settings.arrow_length,
                                    self.settings.arrow_width)
        self.rect.midtop = tp_game.archer.rect.midtop

        # Store the bullets rect information as a float value
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        # Set the direction for the arrow so that it can be modified later
        self.firing_right = False
        self.firing_left = False
        self.firing_down = False
        self.firing_up = False

        # Gets the direction the archer is facing, and uses that to determine 
        # the direction the arrow should travel.
        if self.archer.facing_right:
            self.firing_right = True
        elif self.archer.facing_left:
            self.firing_left = True
        elif self.archer.facing_down:
            self.firing_down = True
        elif self.archer.facing_up:
            self.firing_up = True

    def update(self):
        """Move the arrow around the screen."""
        # Update the exact position of the arrow.
        if self.firing_right:
            self.x += self.settings.arrow_speed
        elif self.firing_left:
            self.x -= self.settings.arrow_speed
        elif self.firing_down:
            self.y += self.settings.arrow_speed
        elif self.firing_up:
            self.y -= self.settings.arrow_speed
        
        # Update the rect position based upon the float value
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_arrow(self):
        """Draw the arrow to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)