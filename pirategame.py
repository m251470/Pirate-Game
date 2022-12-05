#DJ's Pirate ship game
import sys
import pygame
from background import grid
from WASDpirateship import Ship1
from Arrowspirateship import Ship2
from cannonballs1 import CannonBall1
from cannonballs2 import CannonBall2
from island1 import Island
from powerup import Powerup
from time import sleep
from random import randint, choice

#Grid size
#Using sprites to create a background
tile_size = 64
#Get the window width
window_width = 18 * tile_size
#Get the window height
window_height = 12 * tile_size
#Load in water image
water = pygame.image.load("images/rpgTile029.png")

#Add iamge to list to assign number value
background = [water]
tile_rect = water.get_rect()



class PirateGame:
    """The class for the Pirate Game"""
    def __init__(self):
        """Intialize Game"""
        pygame.init()
        self.screen = pygame.display.set_mode((window_width,window_height))
        #Caption for game
        pygame.display.set_caption("Pirate Game")
        #Intialize ships
        self.ship1 = Ship1(self)
        self.ship2 = Ship2(self)
        #Set ships as sprites
        #Multiplier feature
        self.ship_group1 = pygame.sprite.Group()
        self.ship_group2 = pygame.sprite.Group()
        #Put ships into sprite groups
        self.ship_group1.add(self.ship1)
        self.ship_group2.add(self.ship2)
        #Draw background
        self.bg = self.draw_background((window_width,window_height))
        #Set cannonballs into sprite groups
        self.cannonballs1 = pygame.sprite.Group()
        self.cannonballs2 = pygame.sprite.Group()
        #Set the island groups
        self.islands = pygame.sprite.Group()
        #Set powerups groups
        self.powerups = pygame.sprite.Group()
        self.clock = pygame.time.Clock()




    def run_game(self):
        """Main Loop"""
        while True:
            #End Screen if ship2 wins
            if not self.ship1.alive():
                self.end_screen()
            #End screen if ship1 wins
            if not self.ship2.alive():
                self.end_screen()
            #Constantly check for events
            self._check_events()
            #Constantly check for screen updates
            self.update_screen()



    def _check_events(self):
        #Responds to events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        #Keyboard events to control 2 ships for multiplayer
        #Keyboard events for rotating
        if event.key == pygame.K_RIGHT:
            self.ship2.change_omega(.1)
        elif event.key == pygame.K_LEFT:
            self.ship2.change_omega(-.1)
        elif event.key == pygame.K_d:
            self.ship1.change_omega(.1)
        elif event.key == pygame.K_a:
            self.ship1.change_omega(-.1)
        #Keyboard events for speed
        elif event.key == pygame.K_UP:
            self.ship2.change_speed(-.4)
        elif event.key == pygame.K_DOWN:
            self.ship2.change_speed(.4)
        elif event.key == pygame.K_w:
            self.ship1.change_speed(-.4)
        elif event.key == pygame.K_s:
            self.ship1.change_speed(.4)
        #Keybaord events for cannons
        #SHOOTER
        elif event.key == pygame.K_q:
            self.cannonballs1.add(self.ship1.shoot())
        elif event.key == pygame.K_RSHIFT:
            self.cannonballs2.add(self.ship2.shoot())
        #Start game
        elif event.key == pygame.K_SPACE:
            self.island_create()
            self.create_powerup()
        #Exit game
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def draw_background(self, bg_size):
        #Draw the surface with spirtes
        self.bg = pygame.Surface(bg_size)
        #for every part in the grid blit the background in the screen
        for r, gridlist in enumerate(grid):
            for c, gridpart in enumerate(gridlist):
                self.bg.blit(background[gridpart], (c * tile_size, r * tile_size))
        return self.bg
    def island_create(self):
        #for every part of the window width create an island
        #Set upper and bottom borders
        for x in range(0,window_width,tile_size):
            for y in (0,window_height+10):
                island = Island((x,y))
                #Add them to sprite group
                self.islands.add(island)
        # for every part of the window hieght create an island
        #Set left and right island borders
        for y in range(0, window_height, tile_size):
            for x in (0, window_width+10):
                island = Island((x, y), 'vertical')
                # add the wall to our sprite group
                self.islands.add(island)
        #Create serperate
        Middleisland = Island((300,250))
        Bottomisland = Island((800, 500))
        #Add items to groups
        self.islands.add(Bottomisland)
        self.islands.add(Middleisland)


    def random_position(self):
        """Creating Random Position for Powerup"""
        x_loc = randint(100, window_width - 100)
        y_loc = randint(100, window_height - 100)
        return (x_loc, y_loc)
    def create_powerup(self, num_powers=1):
        """Fucntion to create powerups"""
        current_num = len(self.powerups.sprites())
        #If power up collides with island, do not put the powerup there
        for i in range(current_num, num_powers):
            #Powerup at random positions
            new_powerup = Powerup(*self.random_position())
            if not pygame.sprite.spritecollideany(new_powerup, self.islands):
                self.powerups.add(new_powerup)


    def end_screen(self):
        '''Ends the game and displays score / reset info'''
        while True:
            #If ship2 not alive
            if not self.ship2.alive():
                #Fill the screen red
                self.screen.fill((200, 100, 100))
                #Use special font
                #Kam Summers helped me use the special font
                #FANCY FONT
                final_screen_font = pygame.font.Font("images/Bruce-Forever.ttf", 26)
                #Font on screen
                final_screen_text = final_screen_font.render(
                    f"RED SHIP WINS!!! GAME OVER - Click Down To Exit", False, (230, 230, 230))
                #Set position of text
                final_rect = final_screen_text.get_rect()
                final_rect.center = self.screen.get_rect().center
                # draw text on screen
                self.screen.blit(final_screen_text, final_rect)
                final_rect = final_screen_text.get_rect()
                final_rect.midbottom = self.screen.get_rect().midbottom
                pygame.display.flip()
                self.clock.tick()
                #Set ability to exit screen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                        #MOUSE EVENT
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            sys.exit()
            elif not self.ship1.alive():
                #Exit screen is Ship2 wins
                #Blue Background
                self.screen.fill((35, 60, 186))
                #Kam Summers helped me with special font
                # FANCY FONT
                final_screen_font = pygame.font.Font("images/Bruce-Forever.ttf", 26)
                final_screen_text = final_screen_font.render(
                    f"BLUE SHIP WINS!! GAME OVER - Click Down TO Exit", False, (230, 230, 230))
                # Set position of text
                final_screen_rect = final_screen_text.get_rect()
                final_screen_rect.center = self.screen.get_rect().center
                #Draw text on screen
                self.screen.blit(final_screen_text, final_screen_rect)
                final_screen_rect = final_screen_text.get_rect()
                final_screen_rect.midbottom = self.screen.get_rect().midbottom
                pygame.display.flip()
                self.clock.tick()
                #Set ability to exit screen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                        # MOUSE EVENT
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            sys.exit()


    def update_screen(self):
        """Update all the different functions"""
        self.screen.blit(self.bg, self.bg.get_rect())
        # Draw the sprites
        self.islands.draw(self.screen)
        self.ship_group1.draw(self.screen)
        self.ship_group2.draw(self.screen)
        self.cannonballs1.draw(self.screen)
        self.cannonballs2.draw(self.screen)
        self.powerups.draw(self.screen)
        #Update the sprites
        #Duncan Ayles helped me with updating my sprites.
        self.islands.update()
        self.cannonballs1.update(self.islands, self.cannonballs1)
        self.cannonballs2.update(self.islands, self.cannonballs2)
        self.ship_group1.update(self.islands, self.powerups, self.cannonballs2, self.ship_group1)
        self.ship_group2.update(self.islands, self.powerups, self.cannonballs1, self.ship_group2)
        self.powerups.update()





        # make the most recently drawn screen visible
        pygame.display.flip()
        #Set fps for game
        self.clock.tick(2000)

if __name__ == '__main__':
    # run game
    ai = PirateGame()
    ai.run_game()