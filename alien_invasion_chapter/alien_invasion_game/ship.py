# Dylan Nelson
# June 03, 2024
# ship.py

import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and its starting location."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship in the bottom center of the screen,
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float value for the ships exact horizontal position
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that is not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag."""
        # Update the ships x value, instead of the rect value.
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update the ship's rect value from the x value
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
