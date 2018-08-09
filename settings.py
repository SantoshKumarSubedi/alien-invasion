from random import randint
class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        self.ship_speed_factor = 1.5

        #Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255,0,0
        self.bullet_allowed = 4

        #Star Settings
        self.star_speed_factor = randint(20,30)/10
        self.star_width = 2
        self.star_height = 2
        self.star_color = 255,255,255
        self.star_allowed = 100

        #alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
