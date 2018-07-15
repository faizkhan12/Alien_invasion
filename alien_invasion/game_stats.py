class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_settings):
        """Initialise statistics"""
        self.ai_settings=ai_settings
        self.reset_stats()
        #High score shoud never be reset
        self.high_score=0

        #Start Alien Invasion in an inactive stat
        self.game_active=False

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ship_remaining=self.ai_settings.ship_limit
        self.score=0
        self.level=1
