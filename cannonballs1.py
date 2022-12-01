import pygame
from pygame.sprite import Sprite
import math

class CannonBall1(Sprite):
    def __init__(self,x,y,theta,):
        Sprite.__init__(self)
        self.image = pygame.image.load('images/cannonBall.png')
        self.image = pygame.transform.rotate(self.image,theta+90)

        #Create cannon
        self.rect = self.image.get_rect()
        self.rect.midright = (int(x),int(y))

        #Store the bullet's position as a decimal value
        self.y = y
        self.x = x
        self.speed = -2
        self.theta = theta
    def update(self, islands, cannonballs1):
        """Move bullet up the screen"""
        self.y += self.speed * math.cos(self.theta_rads())
        self.x += self.speed * math.sin(self.theta_rads())
        self.rect.center = (int(self.x),int(self.y))
        self.island_cannon(islands, cannonballs1)
    def theta_rads(self):
        return math.pi/180 * self.theta

    def island_cannon(self, islands, cannonballs1):
        collisions = pygame.sprite.groupcollide(islands, cannonballs1, False, True)
