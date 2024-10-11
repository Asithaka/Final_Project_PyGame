#------------------------------------------------------  Creating a Pygame Window and Responding to User Input ---------------------------------------

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
 
# """Overall class to manage game assets and behavior."""

 def __init__(self):

 # """Initialize the game, and create game resources."""

    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height
 
    self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")

    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()
    self._create_fleet()

 def _create_fleet(self):
 #"""Create the fleet of aliens."""
 # Create an alien and find the number of aliens in a row.
 # Spacing between each alien is equal to one alien width.
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size
    available_space_x = self.settings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x // (2 * alien_width)

 # Determine the number of rows of aliens that fit on the screen.

    ship_height = self.ship.rect.height
    available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = available_space_y // (2 * alien_height)

 # Create the full fleet of aliens.
    for row_number in range(number_rows):
      for alien_number in range(number_aliens_x):
        self._create_alien(alien_number, row_number)

 def _create_alien(self, alien_number, row_number):
     
 #"""Create an alien and place it in the row."""

    alien = Alien(self)
    alien_width, alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    self.aliens.add(alien)

 def _check_fleet_edges(self):

 #"""Respond appropriately if any aliens have reached an edge."""

    for alien in self.aliens.sprites():
        if alien.check_edges():
            self._change_fleet_direction()
            break

 def _change_fleet_direction(self):
 #"""Drop the entire fleet and change the fleet's direction."""
    for alien in self.aliens.sprites():
        alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1

 def run_game(self):

    while True:
     
#  Isolating the event loop allows you to manage events separately from other aspects of the game, such as updating the screen

        self._check_events()
        self.ship.update()
        #self.bullets.update()

        # Get rid of bullets that have disappeared.
        self._update_bullets()
        self._update_aliens()
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
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


 def _check_keydown_events(self, event):
 # """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
         self._fire_bullet()


 def _check_keyup_events(self, event):
 # """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False
 
 def _fire_bullet(self):
 # """Create a new bullet and add it to the bullets group."""
    if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

 def _update_bullets(self):
 # """Update position of bullets and get rid of old bullets."""
 # Update bullet positions.
    self.bullets.update()
 # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

# Check for any bullets that have hit aliens.
 # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
    
    if not self.aliens:
 # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()

 def _update_aliens(self):
     
 # """Update the positions of all aliens in the fleet."""
 # Check if the fleet is at an edge, then update the positions of all aliens in the fleet.
    self._check_fleet_edges()
    self.aliens.update()
                    
 # Move the ship to the right.
                    #self.ship.rect.x += 1

 # Make the most recently drawn screen visible.

 # The call to pygame.display.flip() at z tells Pygame to make the most recently drawn screen visible. In this case, it simply draws an empty screen
# on each pass through the while loop, erasing the old screen so only the new screen is visible.

 def _update_screen(self):

    # Redraw the screen during each pass through the loop.

    self.screen.fill(self.settings.bg_color)

# which draws the image to the screen at the position specified by self.rect. 

    self.ship.blitme()

    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    
    self.aliens.draw(self.screen)
    
 # Make the most recently drawn screen visible.
    pygame.display.flip()


if __name__ == '__main__':
 
 # Make a game instance, and run the game.

 ai = AlienInvasion()
 ai.run_game()


    