
# The ship.py file contains the Ship class. The Ship class has an __init__() method, 
# an update() method to manage the ship’s position, and a blitme() method to draw the ship to the screen. 
# The image of the ship is stored inship.bmp, which is in the images folder.

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
 
# A class to manage the ship.

    def __init__(self, ai_game):
  
# Initialize the ship and set its starting position.

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

# Load the ship image and get its rect.

#To load the image, we call pygame.image.load() w and give it the location of our ship image. This function returns a surface representing the
# ship, which we assign to self.image

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

# Start each new ship at the bottom center of the screen.

        self.rect.midbottom = self.screen_rect.midbottom

# Store a decimal value for the ship's horizontal position.

        self.x = float(self.rect.x)

# Movement flag

        self.moving_right = False
        self.moving_left = False

    def update(self):

# Update the ship's position based on the movement flag.
# Update the ship's x value, not the rect.
# If this value is less than the value returned by self.screen_rect.right, the ship hasn’t reached the right edge of the screen

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

# Update rect object from self.x.

        self.rect.x = self.x

    def blitme(self):

# Draw the ship at its current location.

        self.screen.blit(self.image, self.rect)

    def center_ship(self):

# Center the ship on the screen.
# Start each new ship at the bottom center of the screen.

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
