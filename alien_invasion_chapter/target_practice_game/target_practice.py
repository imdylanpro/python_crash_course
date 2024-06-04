# Dylan Nelson 
# June 03, 2024
# target_practice.py

import pygame
import sys

from settings import Settings
from archer import Archer

class TargetPractice():
    """Creates a blue background."""

    def __init__(self):
        """Initialize the background and create the neccessary resources."""
        # pygame.init() initializes all of the modules that are associated 
        # with pygame. This command is necessary to run to ensure that all of
        # the pygame features are ready to be used.
        pygame.init()
        # Sets the caption that appears at the top of the window.
        pygame.display.set_caption("Target Practice")
        # Creates a clock object that can be used to control framerate.
        self.clock = pygame.time.Clock()
        # import the settings as an attribute and make them available to use.
        self.settings = Settings()
        # Sets the screen size.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.archer = Archer(self)

    def run_game(self):
        """Creates the main loop for the game."""
        # This is a while loop to run the pygame screen in a loop.
        while True:
            # Call the helper methods to help declutter the run_game method
            self._check_events()
            self._update_screen()
            # Sets the frame rate to be 60 fps.
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse movements."""
        # Mouse and keyboard events are stored inside a queued list that can be
        # accessed in pygame.event 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Helper method that redraws the screen"""
        self.screen.fill(self.settings.bg_color)
        # Call the blitme function from Archer class which draws the archer at 
        # his current location.
        self.archer.blitme()
        # pygame.display.flip essentially refreshes the display. It draws 
        # in anything that was created on the last frame into the new 
        # frame. It does this by "flipping" the back buffer to the front.
        pygame.display.flip()

if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()
