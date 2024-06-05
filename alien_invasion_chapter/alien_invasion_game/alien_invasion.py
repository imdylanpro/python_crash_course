# Dylan Nelson
# June 02, 2024
# alien_invasion.py

import sys 
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion():
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create the game resources.'''
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            # Set the frame rate to 60.
            self.clock.tick(60)
    
    # This is a helper method. It is used to only run code in the run_game 
    # method while also being a standalone method.
    def _check_events(self):
        """Respond to keypreses and mouse events."""
        # A keypress or mouse movement is considered an "event".
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right while holding down keyright.
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move the ship to the right while holding down keyright.
                    self.ship.moving_left = True                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Stop movement of the ship when keyright is released.
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    # Stop movement of the ship when keyright is released.
                    self.ship.moving_left = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screenduring each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
