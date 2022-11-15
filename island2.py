import pygame
from time import sleep
pygame.init()
tile_size2 = 64
window_width2 = 4 * tile_size2
window_height2 = 4 * tile_size2


grid2 = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15],
]
#Assign number values to images
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

island_parts2 = [TopLeftIslandCorner2, Center1TopIsland2, Center2TopIsland2, TopRightIslandCorner2, TMiddleLeftIsland2, TMiddleMiddleIsland2, TMiddleMiddle2Island2, TMiddleRightIsland2, BMiddleLeftIsland2, BMiddleMiddleIsland2, BMiddleMiddle2Island2, BMiddleRightIsland2, BottomLeftCornerIsland2, BottomCenterIsland2, Bottom2CenterIsland2, BottomRightCornerIsland2]

#Get dimensions of out tile
tile_rect2 = TopLeftIslandCorner2.get_rect()


#Draw our screen with the background
screen2 = pygame.display.set_mode((window_width2, window_height2))

w_loc2 = 0
h_loc2 = 0



for row in grid2:
    for i in row:
        screen2.blit(island_parts2[i],(w_loc2, h_loc2))
        w_loc2 += tile_size2
    h_loc2 += tile_size2
    w_loc2 = 0

pygame.display.flip()
sleep(5)

