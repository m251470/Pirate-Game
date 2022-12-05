import pygame
from pygame.sprite import Sprite
import math

class Powerup(Sprite):
    """This Class if for powerups within the game"""
    def __init__(self,x,y):
        """Initliaze the powerup class"""
        Sprite.__init__(self)
        #Load Powerupimage
        self.image = pygame.image.load('images/element_red_diamond_glossy.png')

        #Create the powerup
        self.rect = self.image.get_rect()
        self.rect.midright = (int(x),int(y))

        #Store the powerups's position as a decimal value
        self.y = y
        self.x = x

    def update(self):
        """Update position of the powerup"""
        self.rect.center = (int(self.x),int(self.y))

