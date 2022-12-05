import pygame
from pygame.sprite import Sprite
import math

class CannonBall2(Sprite):
    def __init__(self,x,y,theta,):
        """Intitate cannonball"""
        Sprite.__init__(self)
        #Set image for cannonball
        self.image = pygame.image.load('images/cannonBall.png')
        self.image = pygame.transform.rotate(self.image,theta+180)

        #Create cannon
        self.rect = self.image.get_rect()
        self.rect.center = (int(x),int(y))

        #Store the cannon's position
        self.y = y
        self.x = x
        #Set speed for cannonabll
        self.speed = -4

        self.theta = theta
    def update(self, islands, cannonballs1):
        """Update cannonball's position"""
        #fucntions for cannonballs position
        self.y += self.speed * math.cos(self.theta_rads())
        self.x += self.speed * math.sin(self.theta_rads())
        self.rect.center = (int(self.x),int(self.y))
        #Check for collision
        self.island_cannon(islands, cannonballs1)
    def theta_rads(self):
        """Function for degrees into radians"""
        return math.pi/180 * self.theta
    def island_cannon(self, islands, cannonballs2):
        # Kill cannonball if collide into island
        collisions = pygame.sprite.groupcollide(islands, cannonballs2, False, True)
