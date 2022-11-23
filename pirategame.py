#DJ's Pirate ship game
import sys
import pygame
from background import grid
from WASDpirateship import Ship1
from Arrowspirateship import Ship2
from cannonballs1 import CannonBall1
from cannonballs2 import CannonBall2
from island1 import Island
from time import sleep

#Grid
tile_size = 64
window_width = 18 * tile_size
window_height = 12 * tile_size
#Load in all images
water = pygame.image.load("images/rpgTile029.png")
TopLeftIslandCorner1  = pygame.image.load("images/island1/tile_01.png")
CenterTopIsland1 = pygame.image.load("images/island1/tile_02.png")
TopRightIslandCorner1 = pygame.image.load("images/island1/tile_03.png")
MiddleLeftIsland1 = pygame.image.load("images/island1/tile_17.png")
MiddleMiddleIsland1 = pygame.image.load("images/island1/tile_18.png")
MiddleRightIsland1 = pygame.image.load("images/island1/tile_19.png")
BottomLeftCornerIsland1 = pygame.image.load("images/island1/tile_33.png")
BottomCenterIsland1 = pygame.image.load("images/island1/tile_34.png")
BottomRightCornerIsland1 = pygame.image.load("images/island1/tile_35.png")
TopLeftIslandCorner2 = pygame.image.load("images/island2/tile_06.png")
Center1TopIsland2 = pygame.image.load("images/island2/tile_07.png")
Center2TopIsland2 = pygame.image.load("images/island2/tile_08.png")
TopRightIslandCorner2 = pygame.image.load("images/island2/tile_09.png")
TMiddleLeftIsland2 = pygame.image.load("images/island2/tile_22.png")
TMiddleMiddleIsland2 = pygame.image.load("images/island2/tile_23.png")
TMiddleMiddle2Island2 = pygame.image.load("images/island2/tile_24.png")
TMiddleRightIsland2 = pygame.image.load("images/island2/tile_25.png")
BMiddleLeftIsland2 = pygame.image.load("images/island2/tile_38.png")
BMiddleMiddleIsland2 = pygame.image.load("images/island2/tile_39.png")
BMiddleMiddle2Island2 = pygame.image.load("images/island2/tile_40.png")
BMiddleRightIsland2 = pygame.image.load("images/island2/tile_41.png")
BottomLeftCornerIsland2 = pygame.image.load("images/island2/tile_54.png")
BottomCenterIsland2 = pygame.image.load("images/island2/tile_55.png")
Bottom2CenterIsland2 = pygame.image.load("images/island2/tile_56.png")
BottomRightCornerIsland2 = pygame.image.load("images/island2/tile_57.png")
#Assign number values to images
background = [water, TopLeftIslandCorner1, CenterTopIsland1, TopRightIslandCorner1, MiddleLeftIsland1, MiddleMiddleIsland1, MiddleRightIsland1, BottomLeftCornerIsland1, BottomCenterIsland1, BottomRightCornerIsland1, TopLeftIslandCorner2, Center1TopIsland2, Center2TopIsland2, TopRightIslandCorner2, TMiddleLeftIsland2, TMiddleMiddleIsland2, TMiddleMiddle2Island2, TMiddleRightIsland2, BMiddleLeftIsland2, BMiddleMiddleIsland2, BMiddleMiddle2Island2, BMiddleRightIsland2, BottomLeftCornerIsland2, BottomCenterIsland2, Bottom2CenterIsland2, BottomRightCornerIsland2]
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

        self.bg = self.draw_background((window_width,window_height))
        self.cannonballs1 = pygame.sprite.Group()
        self.cannonballs2 = pygame.sprite.Group()
        self.islands = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.intro = (0,50,250)


    def run_game(self):
        """Main Loop"""
        while True:
            self._check_events()
            self.update_screen()

    def game_intro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.intro)
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = self.text_objects("Press Space to Start", largeText)
            TextRect.center = ((window_width / 2), (window_height / 2))
            self.screen.blit(TextSurf, TextRect)


    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.intro)
        return textSurface, textSurface.get_rect()
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
        Misland = Island((300,250))
        Bisland = Island((800, 500))
        self.islands.add(Bisland)
        self.islands.add(Misland)



    def _check_cannonball_ship_collisions(self):
        #Check for cannonballs that hit ships and get rid of cannonballs and change ship if so
        collisions1 = pygame.sprite.groupcollide(self.cannonballs1, self.ship2, True, True)
        collisions2 = pygame.sprite.groupcollide(self.cannonballs2, self.ship1, True, True)

        if not self.ship2:
            self.cannonballs1.empty()
        elif not self.ship1:
            self.cannonballs2.empty()

    def update_screen(self):
        self.game_intro()
        self.screen.blit(self.bg, self.bg.get_rect())
        self.ship1.update(self.islands)
        self.ship2.update(self.islands)
        self.ship1.update(self.islands)
        self.ship2.update(self.islands)
        pygame.sprite.Group.draw(self.islands, self.screen)
        self.ship2.blitme(self.screen)
        self.ship1.blitme(self.screen)
        self.cannonballs1.update()
        self.cannonballs2.update()
        pygame.sprite.Group.draw(self.cannonballs1,self.screen)
        pygame.sprite.Group.draw(self.cannonballs2, self.screen)

        # make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(1000)

if __name__ == '__main__':
    # run game
    ai = PirateGame()
    ai.run_game()