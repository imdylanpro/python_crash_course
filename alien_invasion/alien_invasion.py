# Dylan Nelson
# June 02, 2024
# alien_invasion.py

import sys 
import pygame

class AlienInvasion():
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create the game resources.'''
        pygame.init()

        self.clock = pygame.time.clock()

        self.screen = pygame.display.set_mode(1200, 800)
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            # Watch for keyboard and mouse events

            # This specifically watches for if the user clicks the exit button.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screenduring each pass through the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            # Set the frame rate to 60.
            self.clock.tick(60)
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
