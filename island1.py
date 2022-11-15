import pygame
from time import sleep
pygame.init()
tile_size = 64
window_width = 3 * tile_size
window_height = 3 * tile_size


grid = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
#Assign number values to images
TopLeftIslandCorner1  = pygame.image.load("images/island1/tile_01.png")
CenterTopIsland1 = pygame.image.load("images/island1/tile_02.png")
TopRightIslandCorner1 = pygame.image.load("images/island1/tile_03.png")
MiddleLeftIsland1 = pygame.image.load("images/island1/tile_17.png")
MiddleMiddleIsland1 = pygame.image.load("images/island1/tile_18.png")
MiddleRightIsland1 = pygame.image.load("images/island1/tile_19.png")
BottomLeftCornerIsland1 = pygame.image.load("images/island1/tile_33.png")
BottomCenterIsland1 = pygame.image.load("images/island1/tile_34.png")
BottomRightCornerIsland1 = pygame.image.load("images/island1/tile_35.png")

island_parts = [TopLeftIslandCorner1,CenterTopIsland1, TopRightIslandCorner1, MiddleLeftIsland1, MiddleMiddleIsland1, MiddleRightIsland1, BottomLeftCornerIsland1, BottomCenterIsland1, BottomRightCornerIsland1]

#Get dimensions of out tile
tile_rect = TopLeftIslandCorner1.get_rect()


#Draw our screen with the background
screen = pygame.display.set_mode((window_width, window_height))

w_loc = 0
h_loc = 0


for row in grid:
    for i in row:
        screen.blit(island_parts[i],(w_loc, h_loc))
        w_loc += tile_size
    h_loc += tile_size
    w_loc = 0
pygame.display.flip()
sleep(5)
