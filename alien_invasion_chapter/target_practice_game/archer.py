# Dylan Nelson
# June 04, 2024
# archer.py

import pygame

class Archer():
    """Creates an archer character that will be used as the player controlled 
    unit for the game."""

    def __init__(self, tp_game):
        """Defines the attributes for the archer character."""
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen.get_rect()

        # Load the archer image and get its rect
        self.image = pygame.image.load('images/archer_no_helmet_larger.bmp')
        self.rect = self.image.get_rect()

        # Start the archer in the bottom center of the screen,
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the archer at its current location."""
        self.screen.blit(self.image, self.rect)