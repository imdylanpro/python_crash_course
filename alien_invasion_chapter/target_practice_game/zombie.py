# Dylan Nelson
# June 18, 2024
# zombie.py

import pygame
from pygame.sprite import Sprite

class Zombie(Sprite):
    """A class to represent a single goblin."""

    def __init__(self, tp_game):
        """Initialize the goblin an set its starting position."""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings

        # Load the goblin image and set its rect attribute.
        self.image = pygame.image.load('images/zombie/zombie_s2.bmp')
        self.rect = self.image.get_rect()

        # Start each new zombie at the top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the zombies location as a float so that it is precise.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Store the archers location for the zombie pathfinding.
        self.archer = tp_game.archer

    def update(self):
        """Move the zombie toward the archer's location."""
        if self.x > self.archer.x:
            self.x -= self.settings.zombie_speed
        elif self.x < self.archer.x:
            self.x += self.settings.zombie_speed
        if self.y > self.archer.y:
            self.y -= self.settings.zombie_speed
        elif self.y < self.archer.y:
            self.y += self.settings.zombie_speed

        # Update the value for the rect.
        self.rect.x = self.x
        self.rect.y = self.y
        