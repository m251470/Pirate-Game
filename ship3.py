import pygame
import math
from cannonballs1 import CannonBall1
from island1 import Island


class Ship3(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        pygame.sprite.Sprite.__init__(self)
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.health = 2
        #Pirate ship 1 image
        if self.health == 2:
            self.image = pygame.image.load('images/Ships/ship (15).png')
            self.image = pygame.transform.scale(self.image,(64,64))
            self.rect = self.image.get_rect()

        #Ship's starting positions on left side
        self.rect.center = self.screen_rect.center

        #Store values for ship's position
        self.x = 100
        self.y = 400



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
        if self.speed > 5:
            self.speed = 5
    def change_omega(self, delta = 1):
        self.speed = 0
        self.omega += delta
    def shoot(self):
        return CannonBall1(self.x, self.y, self.theta)

    def update(self, island_group, cannonballs2, ship_group1):
        """Update the ship's position based on movement flag."""
        self.theta_rads = math.pi/180*self.theta
        new_y= self.y + self.speed * math.cos(self.theta_rads)
        new_x = self.x + self.speed * math.sin(self.theta_rads)
        self.theta -= self.omega
        old_rect = self.rect
        if(not pygame.sprite.spritecollide(self, island_group, False)):
            self.y = new_y
            self.x = new_x
        else:
            self.rect = old_rect
        self.check_death1(cannonballs2, ship_group1)
    def check_death1(self, cannonballs2, ship_group1):
        collisions = pygame.sprite.groupcollide(cannonballs2, ship_group1, False, True)
        if collisions:
            self.health -= 1
        if self.health == 1:
            self.image = pygame.image.load('images/Ships/ship (22).png')
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))





    def blitme(self,screen):
        intX = int(self.x)
        inty = int(self.y)
        self.rect.center = (intX, inty)
        rotation = pygame.transform.rotate(self.image, self.theta)
        rot = rotation.get_rect(center=self.rect.center)
        self.screen.blit(rotation, rot)
