class Settings():
    """A class to store all settings for Alien Invasions"""
    def __init__(self):
        """Initialize the games's static settings."""
        #Screen settings
        self.screen_width=1360
        self.screen_height=760
        self.bg_color=(0,0,0)

        #Ship settings
        self.ship_speed_factor=1.5
        self.ship_limit=2

        #Bullet settings
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=0,0,180
        self.bullets_allowed = 6

        #Alien settings
        self.alien_speed_factor=2
        self.fleet_drop_speed=14
        #fleet_direction of 1 represents right; -1 represent left
        self.fleet_direction=1

        #How quickly the game speeds up
        self.speedup_scale= 1.1

        #How quickly the alien point values increase
        self.score_scale=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1

        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction=1

        #Scoring
        self.alien_points=10

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.alien_speed_factor *=self.speedup_scale
        self.alien_points=int(self.alien_points * self.score_scale)
        
