#DJ's Pirate ship game
import sys
import pygame
from background import grid
from WASDpirateship import Ship1
from Arrowspirateship import Ship2
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
            self.ship2.change_omega(1)
        elif event.key == pygame.K_LEFT:
            self.ship2.change_omega(-1)
        elif event.key == pygame.K_UP:
            self.ship2.change_speed(-.1)
        elif event.key == pygame.K_DOWN:
            self.ship2.change_speed(.1)
        elif event.key == pygame.K_d:
            self.ship1.change_omega(1)
        elif event.key == pygame.K_a:
            self.ship1.change_omega(-1)
        elif event.key == pygame.K_w:
            self.ship1.change_speed(-.1)
        elif event.key == pygame.K_s:
            self.ship1.change_speed(.1)
        elif event.key == pygame.K_ESCAPE:
            sys.exit()



    # Redraw the screen during each pass thorugh the loop
    def draw_background(self, bg_size):
        self.bg = pygame.Surface(bg_size)
        for r, gridlist in enumerate(grid):
            for c, gridpart in enumerate(gridlist):
                self.bg.blit(background[gridpart], (c * tile_size, r * tile_size))
        return self.bg
    def update_screen(self):
        self.screen.blit(self.bg, self.bg.get_rect())
        self.ship1.update()
        self.ship2.update()
        self.ship2.blitme()
        self.ship1.blitme()
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # run game
    ai = PirateGame()
    ai.run_game()