import pygame
from pygame.sprite import Sprite
import math
from cannonballs2 import CannonBall2


class Ship2(Sprite):
    def __init__(self, ai_game):
        pygame.sprite.Sprite.__init__(self)
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Pirate ship 2 image
        self.image = pygame.image.load('images/Ships/ship (5).png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        # Ship's starting positions on left side
        self.rect.midright = self.screen_rect.midright

        # Store values for ship's position
        self.x = 1000
        self.y = 400


        #Rotating
        self.speed = 0
        self.theta = 0
        self.omega = 0
        self.theta_rads = 0

        self.health = 3
    def move_location(self, location):
        self.rect.center = location

    def change_speed(self, delta = 1):
        self.omega = 0
        self.speed += delta
        if self.speed > 5:
            self.speed = 5
    def change_omega(self, delta = 1):
        self.speed = 0
        self.omega += delta
    def shoot(self):
        return CannonBall2(self.x, self.y, self.theta)


    def update(self,island_group,cannonballs1, ship_group2):
        """Update the ship's position based on movement flag."""
        self.theta_rads = math.pi/180*self.theta
        new_y= self.y + self.speed * math.cos(self.theta_rads)
        new_x = self.x + self.speed * math.sin(self.theta_rads)
        self.theta -= self.omega
        old_rect = self.rect
        if(not pygame.sprite.spritecollide(self,island_group,False)):
            self.y = new_y
            self.x = new_x
        else:
            self.rect = old_rect
        self.check_death2(cannonballs1, ship_group2)
    def check_death2(self, cannonballs1, ship_group2):
        collisions = pygame.sprite.groupcollide(cannonballs1, ship_group2, False, True)
        if collisions:
            for collision in collisions:
                self.health -= 1
                if self.health == 2:
                    self.image = pygame.image.load('images/Ships/ship (17).png')
                if self.health == 1:
                    self.image = pygame.image.load('images/Ships/ship (23).png')



    def blitme(self,screen):
        intX = int(self.x)
        inty = int(self.y)
        self.rect.center = (intX,inty)
        rotation = pygame.transform.rotate(self.image, self.theta)
        rot = rotation.get_rect(center = self.rect.center)
        self.screen.blit(rotation, rot)
