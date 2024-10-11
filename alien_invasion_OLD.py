#------------------------------------------------------  Creating a Pygame Window and Responding to User Input ---------------------------------------

import sys
import pygame  

class AlienInvasion:
 
 # Overall class to manage game assets and behavior.

 def __init__(self):
  
 # Initialize the game, and create game resources.
    pygame.init()

#Sets up the display window (game screen) with dimensions 1200x800 pixels.

    self.screen = pygame.display.set_mode((1200, 800))

#Sets the title of the game window to "Alien Invasion".

    pygame.display.set_caption("Alien Invasion")

 def run_game(self):
 
 # Start the main loop for the game.

    while True:
     
 # Watch for keyboard and mouse events.

#pygame.event.get() is used to check for user inputs like keyboard or mouse events.
#An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse
#This function returns a list of events that have taken place since the last time this function was called. Any keyboard or mouse event
#will cause this for loop to run. I

     for event in pygame.event.get():
       
         if event.type == pygame.QUIT:
# called to exit the game.   For example, when the player clicks the game window’s close button, a pygame.QUIT event is detected
# and we call sys.exit() to exit the gam  

            sys.exit()

 # Make the most recently drawn screen visible.

 # The call to pygame.display.flip() at z tells Pygame to make the most recently drawn screen visible. In this case, it simply draws an empty screen
# on each pass through the while loop, erasing the old screen so only the new screen is visible.

     pygame.display.flip()

if __name__ == '__main__':
 
 # Make a game instance, and run the game.

 ai = AlienInvasion()
 ai.run_game()

#------------------------------------------------------  Setting the Background Color ---------------------------------------------------------------------

def __init__(self):
 # --snip--
    pygame.display.set_caption("Alien Invasion")
# Set the background color. Colors in Pygame are specified as RGB colors: a mix of red, green, and blue. Each color value can range from 0 to 255.
    self.bg_color = (230, 230, 230)

    def run_game(self):
    # --snip--
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

# To make an instance of Settings in the project and use it to access our settings

# --snip--

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

 # --snip--
 # Redraw the screen during each pass through the loop.

    self.screen.fill(self.settings.bg_color)
    
 # Make the most recently drawn screen visible.
    pygame.display.flip()

#--snip--

    