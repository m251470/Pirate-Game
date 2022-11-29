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
tile_size = 64
window_width = 18 * tile_size
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
        pygame.display.set_caption("Pirate Game")
        self.ship1 = Ship1(self)
        self.ship2 = Ship2(self)
        self.ship_group1 = pygame.sprite.Group()
        self.ship_group2 = pygame.sprite.Group()
        self.ship_group1.add(self.ship1)
        self.ship_group2.add(self.ship2)
        self.bg = self.draw_background((window_width,window_height))
        self.cannonballs1 = pygame.sprite.Group()
        self.cannonballs2 = pygame.sprite.Group()
        self.islands = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.clock = pygame.time.Clock()


    def run_game(self):
        """Main Loop"""
        while True:
            self._check_events()
            self.update_screen()



    def _check_events(self):
        #Responds to events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship2.change_omega(.1)
        elif event.key == pygame.K_LEFT:
            self.ship2.change_omega(-.1)
        elif event.key == pygame.K_UP:
            self.ship2.change_speed(-.4)
        elif event.key == pygame.K_DOWN:
            self.ship2.change_speed(.4)
        elif event.key == pygame.K_d:
            self.ship1.change_omega(.1)
        elif event.key == pygame.K_a:
            self.ship1.change_omega(-.1)
        elif event.key == pygame.K_w:
            self.ship1.change_speed(-.4)
        elif event.key == pygame.K_s:
            self.ship1.change_speed(.4)
        elif event.key == pygame.K_q:
            self.cannonballs1.add(self.ship1.shoot())
        elif event.key == pygame.K_RSHIFT:
            self.cannonballs2.add(self.ship2.shoot())
        elif event.key == pygame.K_SPACE:
            self.island_create()
            self.create_powerup()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()



    # Redraw the screen during each pass thorugh the loop
    def draw_background(self, bg_size):
        self.bg = pygame.Surface(bg_size)
        for r, gridlist in enumerate(grid):
            for c, gridpart in enumerate(gridlist):
                self.bg.blit(background[gridpart], (c * tile_size, r * tile_size))
        return self.bg
    def island_create(self):
        for x in range(0,window_width,tile_size):
            for y in (0,window_height+10):
                island = Island((x,y))
                self.islands.add(island)
        for y in range(0, window_height, tile_size):
            for x in (0, window_width+10):
                island = Island((x, y), 'vertical')
                # add the wall to our sprite group
                self.islands.add(island)
        Middleisland = Island((300,250))
        Bottomisland = Island((800, 500))
        self.islands.add(Bottomisland)
        self.islands.add(Middleisland)


    def random_position(self):
        """Creating Random Position for Powerup"""
        x_loc = randint(100, window_width - 100)
        y_loc = randint(100, window_height - 100)
        return (x_loc, y_loc)
    def create_powerup(self, num_powers=1):
        current_num = len(self.powerups.sprites())
        for i in range(current_num, num_powers):
            new_powerup = Powerup(*self.random_position())
            if not pygame.sprite.spritecollideany(new_powerup, self.islands):
                self.powerups.add(new_powerup)

    def update_screen(self):
        self.screen.blit(self.bg, self.bg.get_rect())
        self.islands.draw(self.screen)
        self.ship_group1.draw(self.screen)
        self.ship_group2.draw(self.screen)
        self.cannonballs1.draw(self.screen)
        self.cannonballs2.draw(self.screen)
        self.powerups.draw(self.screen)
        self.islands.update()
        self.cannonballs1.update()
        self.cannonballs2.update()
        self.ship_group1.update(self.islands, self.cannonballs2, self.ship_group1)
        self.ship_group2.update(self.islands, self.cannonballs1, self.ship_group2)
        self.powerups.update()




        # make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(1000)

if __name__ == '__main__':
    # run game
    ai = PirateGame()
    ai.run_game()