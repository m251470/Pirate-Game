import pygame

class Island(pygame.sprite.Sprite):
    def __init__(self,pos,orientation='horizontal'):
        # init our sprite:
        pygame.sprite.Sprite.__init__(self)
        #Load the Sprite island iamge
        self.image = pygame.image.load('images/tileStone.png')
        #Create the border of the islands on sides and top and bottom
        if orientation =='vertical':
            self.image = pygame.transform.rotate(self.image,90)
        #Make islands a sprite with get its rect and setting position
        self.rect = self.image.get_rect()
        self.rect.center = pos
    def update(self):
        """Do not need to update island"""
        pass
    def draw(self,screen):
        """Draw Island"""
        screen.blit(self.image,self.rect)