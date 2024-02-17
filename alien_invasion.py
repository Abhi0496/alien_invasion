import sys #we will use to exit the game
import pygame #contains the functionality to we need to run the game
from ship import Ship

from settings import Settings

class AlienInvasion:
    """This class will manage game behavior and assets"""

    def __init__(self):
        """Initializing game and game resources"""
        pygame.init() #initializes the background settings that Pygame needs to work properly
        self.clock = pygame.time.Clock() #for frame rate, it will tick after each iteration of while loop
        self.settings = Settings()
        


        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        """pygame.display.set_mode()to create a display window.
           self.screen is called as surface where the game element will be displayed
           Each element in the game- like alien, ship  it its own surface
           Here the display.set_mode() represents the entire window which will be redrawn on every loop iteration, 
           so it can be updated with any changes triggered by the user input"""
        
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)



    """This game is controlled by run_game method"""
    def run_game(self):
        """Start main loop for the game"""
        """It contains an event(an action that user performs while playing the game) loop"""
        while True:
            """Watch for keyboard and mouse event"""
            """Below for loop is an event loop"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #redraw the screen during each pass through loop
            #fill() method is used to fill the backgroud color
            self.screen.fill(self.settings.bg_color)
            

            """Make the most recently drawn screen visible"""
            pygame.display.flip()
            self.clock.tick(60) #making loop run 60 times/sec
            self.ship.blitme()

if __name__ == '__main__':
    """Making game instance"""
    ai = AlienInvasion()
    ai.run_game()