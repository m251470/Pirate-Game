import pygame
import math
from cannonballs1 import CannonBall1
from pygame import mixer
from island1 import Island
from powerup import Powerup



class Ship1(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        """Intitate Sprite"""
        pygame.sprite.Sprite.__init__(self)
        #Load Music mix
        mixer.init()
        mixer.music.load('images/explosion.mp3')
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #Load the images
        self.original = pygame.image.load('images/Ships/ship (3).png')
        self.original = pygame.transform.scale(self.original, (64, 64))
        #Set original image to image
        self.image = self.original
        self.rect = self.image.get_rect()
        #Set ship health
        self.health = 3


        #Ship intital position
        self.x = 100
        self.y = 400



        #Rotating
        self.speed = 0
        self.theta = 0
        self.omega = 0
        self.theta_rads = 0

    def move_location(self, location):
        """Set the move the location of the ship to the center"""
        self.rect.center = location

    def change_speed(self, delta = 1):
        """Function for ship speed"""
        self.omega = 0
        #Add ship speed after events
        self.speed += delta
        #Set limit for ship speed
        if self.speed > 5:
            self.speed = 5
    def change_omega(self, delta = 1):
        """Function for rotating ship"""
        self.speed = 0
        self.omega += delta

    def shoot(self):
        """Fire cannonball"""
        return CannonBall1(self.x, self.y, self.theta)

    def update(self, islands, powerups, cannonballs2, ship_group1):
        """Update the ship's position based on movement flag."""
        #Equation for degrees to radians
        self.theta_rads = math.pi / 180 * self.theta
        #Equations for movement
        new_y = self.y + self.speed * math.cos(self.theta_rads)
        new_x = self.x + self.speed * math.sin(self.theta_rads)
        old_rect = self.rect
        self.rect.center = (new_x, new_y)
        self.theta -= self.omega
        self.y = new_y
        self.x = new_x
        self.rect = old_rect
        #Check for death by collisions
        self.check_death1(cannonballs2, ship_group1)
        self.check_powerup(powerups, ship_group1)
        self.island_death(islands, ship_group1)
        #Process of rotating images
        intX = int(self.x)
        inty = int(self.y)
        self.rect.center = (intX, inty)
        # Rotate original image
        rotation = pygame.transform.rotate(self.original, self.theta)
        rot = rotation.get_rect(center=self.rect.center)
        # Set rotation to image
        self.image = rotation
        self.rect = rot
        #Set limit to health of ship
        if self.health >= 3:
            self.health == 3


    def check_death1(self, cannonballs2, ship_group1):
        #Fucntion to collision
        collisions = pygame.sprite.groupcollide(cannonballs2, ship_group1, True, False)
        if collisions:
            #Play music if collision
            mixer.music.play()
            #If Collision subtract from health
            self.health -= 1
            print(f"health: {self.health}")
        if self.health == 2:
            #Change image if hit
            self.original = pygame.image.load('images/Ships/ship (15).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 1:
            # Change image if hit
            self.original = pygame.image.load('images/Ships/ship (21).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            # Kill Ship
            print("Ship is dying")
            self.kill()

    def check_powerup(self, powerups, ship_group1):
        """Function for powerup"""
        healthup = pygame.sprite.groupcollide(powerups, ship_group1, True, False)
        if healthup:
            #If collision add to health
            self.health +=1
        if self.health == 3:
            # Change image
            self.original = pygame.image.load('images/Ships/ship (3).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        if self.health == 2:
            # Change image
            self.original = pygame.image.load('images/Ships/ship (15).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 1:
            #Change image
            self.original = pygame.image.load('images/Ships/ship (21).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            print("Ship is dying")
            self.kill()
    def island_death(self, islands, ship_group1):
        """Function for ship collision"""
        death = pygame.sprite.groupcollide(islands, ship_group1, False, False)
        if death:
            #If island collision subtract 2 from health
            self.health -= 2
        if self.health == 3:
            # Change image if hit
            self.original = pygame.image.load('images/Ships/ship (3).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        if self.health == 2:
            # Change image if hit
            self.original = pygame.image.load('images/Ships/ship (15).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 1:
            # Change image if hit
            self.original = pygame.image.load('images/Ships/ship (21).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            #Kill ship
            print("Ship is dying")
            self.kill()





