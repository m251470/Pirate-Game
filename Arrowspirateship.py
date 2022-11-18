import pygame


class Ship2:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Pirate ship 2 image
        self.image = pygame.image.load('images/Ships/ship (5).png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        # Ship's starting positions on left side
        self.rect.midright = self.screen_rect.midright

        # Store values for ship's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False



    def update(self):
        """Update the ship's position based on movement flag."""
        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5
        if self.moving_up and self.rect.top > 0:
            self.y -= 1.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5

    def blitme(self):
        self.screen.blit(self.image, self.rect)