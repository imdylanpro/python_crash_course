# Dylan Nelson
# June 04, 2024
# archer.py

import pygame

class Archer():
    """Creates an archer character that will be used as the player controlled 
    unit for the game."""

    def __init__(self, tp_game):
        """Defines the attributes for the archer character."""
        # Defines the characters screen as the same screen as the main canvas.
        self.screen = tp_game.screen
        # Sets the settings to be the same settings that in tp_game.
        self.settings = tp_game.settings

        # Sets the screen_rect to be the same screen rect as the main canvas, 
        # so the character model knows where they are on the game canvas.
        self.screen_rect = tp_game.screen.get_rect()

        # Load the archer image and get its rect.
        self.image = pygame.image.load(
            'images/archer/archer_facing_right_s2.bmp')
        self.rect = self.image.get_rect()
        

        # Start the archer in the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Create a float value that will be used to store the exact location of
        # the archer.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Create flags for monitoring the characters movement.
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

        # Create flags to monitor which direction the character is facing.
        # facing_right is True because that is the starting position.
        self.facing_right = True
        self.facing_left = False
        self.facing_down = False
        self.facing_up = False

    def update(self):
        """Updates the archers movement and image used based upon the movement 
        flag."""

        direction_change = False
        # Handles moving the character and ensures that they won't go beyond 
        # the limits of the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.facing_right != True:
                direction_change = True
                direction = 'right'
            self.x += self.settings.archer_speed
        if self.moving_left and self.rect.left > 0:
            if self.facing_left != True or direction_change == True:
                direction_change = True
                direction = 'left'
            self.x -= self.settings.archer_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            if self.facing_down != True or direction_change == True:
                direction_change = True
                direction = 'down'
            self.y += self.settings.archer_speed
        if self.moving_up and self.rect.top > 0:
            if self.facing_up != True or direction_change == True:
                direction_change = True
                direction = 'up'
            self.y -= self.settings.archer_speed

        if direction_change == True:
            self._set_character_direction(direction)
            direction_change = False

        # Here the exact value for the horizontal speed is applied to the rect.
        self.rect.x = self.x
        self.rect.y = self.y

    def _set_character_direction(self, direction):
        """Helper method to set the correct direction flag for the 
        character."""

        self.facing_right = False
        self.facing_left = False
        self.facing_down = False
        self.facing_up = False

        if direction == 'right':
            self.facing_right = True
            image = 'images/archer/archer_facing_right_s2.bmp'
            print(f'facing {direction}')
        if direction == 'left':
            self.facing_left = True
            image = 'images/archer/archer_facing_left_s2.bmp'
            print(f'facing {direction}')
        if direction == 'down':
            self.facing_down = True
            image = 'images/archer/archer_facing_down_s2.bmp'
            print(f'facing {direction}')
        if direction == 'up':
            self.facing_up = True
            image = 'images/archer/archer_facing_up_s2.bmp'
            print(f'facing {direction}')

        # Set the new image for the player character.
        self.image = pygame.image.load(image)
        # Set the new rect hitbox for the player character.
        self.rect = self.image.get_rect()

    def blitme(self):
        """Draw the archer at its current location."""
        self.screen.blit(self.image, self.rect)
