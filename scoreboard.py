
#To display the score on the screen, we first create a new class, Scoreboard. For now, this class will just display the current score, but eventually we’ll use
# it to report the high score, level, and number of ships remaining as well.

import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
 
 # A class to report scoring information.

 def __init__(self, ai_game):
  
 #Initialize scorekeeping attributes.
    self.ai_game = ai_game
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ai_game.settings
    self.stats = ai_game.stats

    # Font settings for scoring information.
    self.text_color = (30, 30, 30)
    self.font = pygame.font.SysFont(None, 48)

    # Prepare the initial score image.
    self.prep_score()
    self.prep_high_score()
    self.prep_level()
    self.prep_ships()


# To turn the text to be displayed into an image, we call prep_score() 

 def prep_score(self):
    
 # Turn the score into a rendered image.

    rounded_score = round(self.stats.score, -1)
    #score_str = str(self.stats.score)
    score_str = "{:,}".format(rounded_score)
    self.score_image = self.font.render(score_str, True,
            self.text_color, self.settings.bg_color)

    # Display the score at the top right of the screen.

    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20


# Then we create a show_score() method to display the rendered score image:

 def show_score(self):
   
 # Draw score to the screen.

    self.screen.blit(self.score_image, self.score_rect)
    self.screen.blit(self.high_score_image, self.high_score_rect)
    self.screen.blit(self.level_image, self.level_rect)
    self.ships.draw(self.screen)


# The high score will be displayed separately from the score, so we need a new method, prep_high_score(), to prepare the high score image

 def prep_high_score(self):
   
 # Turn the high score into a rendered image.

    high_score = round(self.stats.high_score, -1)

# Rounding the Score

    high_score_str = "{:,}".format(high_score)
    self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)

 # Center the high score at the top of the screen.

    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.centerx = self.screen_rect.centerx
    self.high_score_rect.top = self.score_rect.top

# The method check_high_score() checks the current score against the high score. If the current score is greater, 
# we update the value of high_score and call prep_high_score() to update the high score’s image.

 def check_high_score(self):

#  Check to see if there's a new high score.

    if self.stats.score > self.stats.high_score:
        self.stats.high_score = self.stats.score
        self.prep_high_score()

# To have Scoreboard display the current level, we call a new method, prep_level(),

 def prep_level(self):

 # Turn the level into a rendered image.

    level_str = str(self.stats.level)
    self.level_image = self.font.render(level_str, True,
            self.text_color, self.settings.bg_color)

 # Position the level below the score.
    self.level_rect = self.level_image.get_rect()
    self.level_rect.right = self.score_rect.right
    self.level_rect.top = self.score_rect.bottom + 10

 def prep_ships(self):

# Finally, let’s display the number of ships the player has left, but this time, let’s use a graphic.
# Show how many ships are left.

   self.ships = Group()
   for ship_number in range(self.stats.ships_left):
      ship = Ship(self.ai_game)
      ship.rect.x = 10 + ship_number * ship.rect.width
      ship.rect.y = 10
      self.ships.add(ship)