import pygame
import math
from cannonballs1 import CannonBall1
from island1 import Island
from powerup import Powerup



class Ship1(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        pygame.sprite.Sprite.__init__(self)
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.original = pygame.image.load('images/Ships/ship (3).png')
        self.original = pygame.transform.scale(self.original, (64, 64))
        self.image = self.original
        self.rect = self.image.get_rect()
        self.health = 3
        #Pirate ship 1 image


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

    def update(self, islands, powerups, cannonballs2, ship_group1):
        """Update the ship's position based on movement flag."""
        self.theta_rads = math.pi / 180 * self.theta
        new_y = self.y + self.speed * math.cos(self.theta_rads)
        new_x = self.x + self.speed * math.sin(self.theta_rads)
        old_rect = self.rect
        self.rect.center = (new_x, new_y)
        self.theta -= self.omega
        if (not pygame.sprite.spritecollide(self, islands, False)):
            self.y = new_y
            self.x = new_x
        else:
            self.rect = old_rect
        self.check_death1(cannonballs2, ship_group1)
        self.check_powerup(powerups, ship_group1)
        self.island_death(islands, ship_group1)
        intX = int(self.x)
        inty = int(self.y)
        self.rect.center = (intX, inty)
        rotation = pygame.transform.rotate(self.original, self.theta)
        rot = rotation.get_rect(center=self.rect.center)
        self.image = rotation
        self.rect = rot
        if self.health >= 3:
            self.health == 3


    def check_death1(self, cannonballs2, ship_group1):
        collisions = pygame.sprite.groupcollide(cannonballs2, ship_group1, True, False)
        if collisions:
            self.health -= 1
            print(f"health: {self.health}")
        if self.health == 2:
            self.original = pygame.image.load('images/Ships/ship (15).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 1:
            self.original = pygame.image.load('images/Ships/ship (21).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            print("Ship is dying")
            self.kill()

    def check_powerup(self, powerups, ship_group1):
        healthup = pygame.sprite.groupcollide(powerups, ship_group1, True, False)
        if healthup:
            self.health +=1
        if self.health == 3:
            self.original = pygame.image.load('images/Ships/ship (3).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        if self.health == 2:
            self.original = pygame.image.load('images/Ships/ship (15).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 1:
            self.original = pygame.image.load('images/Ships/ship (21).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            print("Ship is dying")
            self.kill()
    def island_death(self, islands, ship_group1):
        death = pygame.sprite.groupcollide(islands, ship_group1, False, False)
        if death:
            self.health -= 2
        if self.health == 3:
            self.original = pygame.image.load('images/Ships/ship (3).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        if self.health == 2:
            self.original = pygame.image.load('images/Ships/ship (15).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 1:
            self.original = pygame.image.load('images/Ships/ship (21).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            print("Ship is dying")
            self.kill()





