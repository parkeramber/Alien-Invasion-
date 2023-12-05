class Settings:

    def __init__(self):
        """ Initialize the game's static settings. """
        self.screen_width = 1200
        self.screen_height = 800  # Corrected line
        self.bg_color = (235, 196, 251)
        
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet settings - bullets that are 3 pixels wide and purple
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (128, 0, 128)  # Purple color
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1