
# Responding to Alien and Ship Collisions
# Tracking statistics

class GameStats:
 
 # Track statistics for Alien Invasion.

 def __init__(self, ai_game):
  
 # Initialize statistics.

    self.settings = ai_game.settings
    self.reset_stats()

    # Start game in an inactive state.
    # Let’s add a game_active flag as an attribute to GameStats to end the game when the player runs out of ships.

    self.game_active = False

    # High score should never be reset.

    self.high_score = 0

   # To display the player’s level in the game, we first need an attribute in GameStats representing the current level.
   
    self.level = 1

 def reset_stats(self):
  
 # Initialize statistics that can change during the game.

    self.ships_left = self.settings.ship_limit
    self.score = 0