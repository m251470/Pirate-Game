import pygame
from pygame.sprite import Sprite
from pygame import mixer
import math
from cannonballs2 import CannonBall2


class Ship2(Sprite):
    def __init__(self, ai_game):
        """Intitate Sprite"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #Load Music mix
        mixer.init()
        mixer.music.load('images/explosion.mp3')
        # Load the images
        self.original = pygame.image.load('images/Ships/ship (5).png')
        self.original = pygame.transform.scale(self.original, (64, 64))
        # Set original image to image
        self.image = self.original
        self.rect = self.image.get_rect()
        self.health = 3
        # #Set ship health
        if self.health == 3:
            self.image = pygame.image.load('images/Ships/ship (5).png')
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()



        #Ship intial position
        self.x = 1000
        self.y = 400


        #Rotating
        self.speed = 0
        self.theta = 0
        self.omega = 0
        self.theta_rads = 0


    def move_location(self, location):
        """Set the move the location of the ship to the center"""
        self.rect.center = location

    def change_speed(self, delta=1):
        """Function for ship speed"""
        self.omega = 0
        # Add ship speed after events
        self.speed += delta
        # Set limit for ship speed
        if self.speed > 5:
            self.speed = 5

    def change_omega(self, delta=1):
        """Function for rotating ship"""
        self.speed = 0
        self.omega += delta
    def shoot(self):
        """Fire cannonball"""
        return CannonBall2(self.x, self.y, self.theta)


    def update(self, islands, powerups, cannonballs1, ship_group2):
        """Update the ship's position based on movement flag."""
        # Equation for degrees to radians
        self.theta_rads = math.pi / 180 * self.theta
        # Equations for movement
        #TRICKY TRIG
        new_y = self.y + self.speed * math.cos(self.theta_rads)
        new_x = self.x + self.speed * math.sin(self.theta_rads)
        old_rect = self.rect
        self.rect.center = (new_x, new_y)
        self.theta -= self.omega
        if (not pygame.sprite.spritecollide(self, islands, False)):
            #If ship does not collide with islands nothing happens
            self.y = new_y
            self.x = new_x
        else:
            # go back to the old position
            self.rect = old_rect
            #WALLS ARE HARD IF YOU COLLIDE WITH WALL YOU DIE
            self.health -=3
            if self.health <= 0:
                self.health == 0
        # Check for death by collisions
        self.check_death2(cannonballs1, ship_group2)
        self.check_powerup(powerups, ship_group2)
        self.island_death(islands, ship_group2)
        # Process of rotating images
        intX = int(self.x)
        inty = int(self.y)
        self.rect.center = (intX, inty)
        #Rotate original image
        rotation = pygame.transform.rotate(self.original, self.theta)
        rot = rotation.get_rect(center=self.rect.center)
        #Set rotation to image
        self.image = rotation
        self.rect = rot
        # Set limit to health of ship
        if self.health >= 3:
            self.health == 3
        if self.health <=0:
            self.health ==0


    def check_death2(self, cannonballs1, ship_group2):
        #Function for cannonball ship collision
        #LOOKING WEAK, health changing by showing different images with damage.
        collisions = pygame.sprite.groupcollide(cannonballs1, ship_group2, True, False)
        if collisions:
            # Play music if collision
            mixer.music.play()
            # If Collision subtract from health
            self.health -= 1
        if self.health == 2:
            # Change image if hit
            self.original = pygame.image.load('images/Ships/ship (17).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 1:
            # Change image if hit
            self.original = pygame.image.load('images/Ships/ship (23).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            #Kill ship
            print("Ship is dying")
            self.kill()
    def check_powerup(self, powerups, ship_group2):
        """Function for powerups"""
        # HEALTHY EATER, images change depending on health
        healthup = pygame.sprite.groupcollide(powerups, ship_group2, True, False)
        if healthup:
            #If collision add to health
            self.health +=1
        if self.health == 3:
            # Change image
            self.original = pygame.image.load('images/Ships/ship (5).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        if self.health == 2:
            # Change image
            self.original = pygame.image.load('images/Ships/ship (17).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 1:
            # Change image
            self.original = pygame.image.load('images/Ships/ship (23).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            print("Ship is dying")
            self.kill()
    def island_death(self, islands, ship_group2):
        """Function if island ship collision"""
        #WALLS ARE HARD, if you collide with wall you are dead.
        death = pygame.sprite.groupcollide(islands, ship_group2, False, False)
        if death:
            #Subtract 2 health collision
            self.health -= 3
        if self.health == 3:
            #Change image
            self.original = pygame.image.load('images/Ships/ship (5).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        if self.health == 2:
            # Change image
            self.original = pygame.image.load('images/Ships/ship (17).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
            # Change image
        elif self.health == 1:
            # Change image
            self.original = pygame.image.load('images/Ships/ship (23).png')
            self.original = pygame.transform.scale(self.original, (64, 64))
            self.image = self.original
            self.rect = self.image.get_rect()
            self.rect.center = (int(self.x), int(self.y))
        elif self.health == 0:
            print("Ship is dying")
            self.kill()


