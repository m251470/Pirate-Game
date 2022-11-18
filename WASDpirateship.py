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

        #Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #Rotating
        self.speed = 0
        self.theta = 0
        self.delta = 0

    def change_speed(self, omega = 1):
        self.delta = 0
        self.speed += omega
    def change_delta(self, omega = 1):
        self.speed = 0
        self.delta += omega


    def update(self):
        """Update the ship's position based on movement flag."""
        self.rect.x = self.x
        self.rect.y = self.y
        theta_rads = math.pi/180*self.theta
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed * math.cos(theta_rads)
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed * math.cos(theta_rads)
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed * math.cos(theta_rads)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed * math.cos(theta_rads)
        self.theta -= self.delta



    def blitme(self):
        self.update()
        intX = int(self.x)
        inty = int(self.y)
        self.rect.center = (self.x,self.y)
        center = self.rect.center
        rotating = pygame.transform.rotate(self.image, self.theta)
        rot = rotating.get_rect(center)
        self.screen.blit(rotating, rot)
