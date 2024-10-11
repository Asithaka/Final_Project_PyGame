#------------------------------------------------------  Creating a Pygame Window and Responding to User Input ---------------------------------------

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
 
# """Overall class to manage game assets and behavior."""

 def __init__(self):

 # """Initialize the game, and create game resources."""

    pygame.init()
    self.settings = Settings()
 
    self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")

    self.ship = Ship(self)

 def run_game(self):

    while True:
     
#  Isolating the event loop allows you to manage events separately from other aspects of the game, such as updating the screen

        self._check_events()
        self._update_screen()
        
 
 # Start the main loop for the game.



 # Watch for keyboard and mouse events.

#pygame.event.get() is used to check for user inputs like keyboard or mouse events.
#An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse
#This function returns a list of events that have taken place since the last time this function was called. Any keyboard or mouse event
#will cause this for loop to run. I

 def _check_events(self):
     
 #"""Respond to keypresses and mouse events."""

        for event in pygame.event.get():
       
            if event.type == pygame.QUIT:
# called to exit the game.   For example, when the player clicks the game window’s close button, a pygame.QUIT event is detected
# and we call sys.exit() to exit the gam  

                sys.exit()

 # Make the most recently drawn screen visible.

 # The call to pygame.display.flip() at z tells Pygame to make the most recently drawn screen visible. In this case, it simply draws an empty screen
# on each pass through the while loop, erasing the old screen so only the new screen is visible.

 def _update_screen(self):

    # Redraw the screen during each pass through the loop.

    self.screen.fill(self.settings.bg_color)

# which draws the image to the screen at the position specified by self.rect. 

    self.ship.blitme()
    
 # Make the most recently drawn screen visible.
    pygame.display.flip()


if __name__ == '__main__':
 
 # Make a game instance, and run the game.

 ai = AlienInvasion()
 ai.run_game()


    