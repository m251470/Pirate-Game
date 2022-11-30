import pygame
from pygame.sprite import Sprite
import math

class Powerup(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.image = pygame.image.load('images/element_red_diamond_glossy.png')

        #Create cannon
        self.rect = self.image.get_rect()
        self.rect.midright = (int(x),int(y))

        #Store the bullet's position as a decimal value
        self.y = y
        self.x = x

    def update(self):
        """Move bullet up the screen"""
        self.rect.center = (int(self.x),int(self.y))

