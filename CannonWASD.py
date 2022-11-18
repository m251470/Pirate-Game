import pygame
from pygame.sprite import Sprite

class CannonBall(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen


        #Create cannon
        self.rect = pygame.Rect(0,0, 5, 5)
        self.rect.midright = ai_game.ship.rect.midright

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
    def update(self):
        """Move bullet up the screen"""
        #Update decimal position
        self.y += 10
        #Update the rect
        self.rect.y = self.y
    def draw_bullet(self):
        """Draw bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)