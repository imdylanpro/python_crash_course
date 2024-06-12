# Dylan Nelson 
# June 03, 2024
# target_practice.py

import pygame
import sys

from settings import Settings
from archer import Archer
from arrow import Arrow

class TargetPractice():
    """Overall class to manage the game assets and behavior."""

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
        # Creates the archer model and allows for it to be used.
        self.archer = Archer(self)
        # Create the arrows as a group.
        self.arrows = pygame.sprite.Group()

    def run_game(self):
        """Creates the main loop for the game."""
        # This is a while loop to run the pygame screen in a loop.
        while True:
            # Call the helper methods to help declutter the run_game method
            self._check_events()
            self.archer.update()
            self._update_arrows()
            self._update_screen()
            # Sets the frame rate to be 60 fps.
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse movements."""
        # Mouse and keyboard events are stored inside a queued list that can be
        # accessed in pygame.event 
        # System quit is given highest priority.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Helper method to check the pressing of keys."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.archer.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.archer.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.archer.moving_down = True
        elif event.key == pygame.K_UP:
            self.archer.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_arrows() 
         
    def _check_keyup_events(self, event):
        """Helper method to press the releasing of keys."""
        if event.key == pygame.K_RIGHT:
            self.archer.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.archer.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.archer.moving_down = False
        elif event.key == pygame.K_UP:
            self.archer.moving_up = False        

    def _fire_arrows(self):
        """Create a new arrow and add it to the arrows group."""
        if len(self.arrows) < self.settings.arrows_allowed:
            new_arrow = Arrow(self)
            self.arrows.add(new_arrow)

    def _update_arrows(self):
        """Check if the arrow is out of bounds and delete it if it is."""
        self.arrows.update()
        for arrow in self.arrows.copy():
            if (arrow.rect.bottom <= 0 
                or arrow.rect.top > self.settings.screen_height):
                self.arrows.remove(arrow)

    def _update_screen(self):
        """Helper method that redraws the screen"""
        # Set the background color for the screen
        self.screen.fill(self.settings.bg_color)
        # draw each arrow that is in the arrows group
        for arrow in self.arrows.sprites():
            arrow.draw_arrow()
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