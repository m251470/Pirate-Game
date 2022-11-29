import pygame
from pygame.sprite import Sprite
import math
from cannonballs2 import CannonBall2


class Ship2(Sprite):
    def __init__(self, ai_game):
        pygame.sprite.Sprite.__init__(self)
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.health = 3
        # Pirate ship 2 image
        if self.health == 3:
            self.image = pygame.image.load('images/Ships/ship (5).png')
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()


        # Store values for ship's position
        self.x = 1000
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
        return CannonBall2(self.x, self.y, self.theta)


    def update(self,island_group,cannonballs1, ship_group2):
        """Update the ship's position based on movement flag."""
        self.theta_rads = math.pi/180*self.theta
        self.y + self.speed * math.cos(self.theta_rads)
        self.x + self.speed * math.sin(self.theta_rads)
        self.theta -= self.omega
        intX = int(self.x)
        inty = int(self.y)
        self.rect.center = (intX, inty)
        rotation = pygame.transform.rotate(self.image, self.theta)
        rot = rotation.get_rect(center=self.rect.center)
        self.screen.blit(rotation, rot)
        self.check_death2(cannonballs1, ship_group2)
    def check_death2(self, cannonballs1, ship_group2):
        collisions = pygame.sprite.groupcollide(cannonballs1, ship_group2, True, False)
        if collisions:
            self.health -= 1
            print(f"health: {self.health}")
        if self.health == 2:
            self.image = pygame.image.load('images/Ships/ship (17).png')
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 1:
            self.image = pygame.image.load('images/Ships/ship (23).png')
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            print("Ship is dying")
            self.kill()



    def draw(self,screen):
        screen.blit(self.image, self.rect)
