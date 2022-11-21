import pygame
from pygame.sprite import Sprite
import math

class Ship1(Sprite):
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Pirate ship 1 image
        self.image = pygame.image.load('images/Ships/ship (3).png')
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()

        #Ship's starting positions on left side
        self.rect.midleft = self.screen_rect.midleft

        #Store values for ship's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)



        #Rotating
        self.speed = 0
        self.theta = 0
        self.omega = 0
        self.theta_rads = 0
    def move_location(self, location):
        self.rect.center = location

    def change_speed(self, delta = 1):
        self.omega = 0
        self.speed += delta
    def change_omega(self, delta = 1):
        self.speed = 0
        self.omega += delta


    def update(self):
        """Update the ship's position based on movement flag."""
        self.theta_rads = math.pi/180*self.theta
        self.y += self.speed * math.cos(self.theta_rads)
        self.x += self.speed * math.sin(self.theta_rads)




    def blitme(self):
        self.update()
        intX = int(self.x)
        inty = int(self.y)
        self.rect.center = (intX, inty)
        rotation = pygame.transform.rotate(self.image, self.theta)
        rot = rotation.get_rect(center=self.rect.center)
        self.screen.blit(rotation, rot)

