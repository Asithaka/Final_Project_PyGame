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

 #is used to check for user inputs like keyboard or mouse events.

     for event in pygame.event.get():
       
         if event.type == pygame.QUIT:
# called to exit the game.    
            sys.exit()

 # Make the most recently drawn screen visible.

     pygame.display.flip()

if __name__ == '__main__':
 
 # Make a game instance, and run the game.

 ai = AlienInvasion()
 ai.run_game()