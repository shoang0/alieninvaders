class Settings:
    # A class to store all settings for alien Invasion
    def __init__(self):
        # Initialize the game's static settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Declare attributes in __init__ but initialize in other methods
        self.ship_speed_factor = None
        self.bullet_speed_factor = None
        self.alien_speed_factor = None
        self.fleet_direction = None
        self.alien_points = None
        self.pink_points = None
        self.teal_points = None
        self.green_points = None
        self.ufo_points = None

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.25

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 6
        self.alien_speed_factor = 3

        # fleet_direction of 1 represents right; -1 left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
        self.pink_points = 10
        self.teal_points = 20
        self.green_points = 40
        self.ufo_points = "???"

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
