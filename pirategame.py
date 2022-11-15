#DJ's Pirate ship game
import sys
import pygame

class PirateGame:
    """The class for the Pirate Game"""
    def __init__(self):
        """Intialize Game"""
        pygame.init()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    def rungame(self):
        """Main Loop"""

    def _check_events(self):
        #Responds to events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_e:
            self._fire_cannon1()
        elif event.key == pygame.K_RSHIFT:
            self._fire_cannon2()
        elif event.key == pygame.K_q:
            self._rotate_ship1()
        elif event.key == pygame.K_SLASH:
            self._rotate_ship2()
        elif event.key == pygame.K_q:
            sys.exit()



   def _update_screen(self):
            # Redraw the screen during each pass thorugh the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            # make the most recently drawn screen visible
        self.stars.draw(self.screen)
        pygame.display.flip()



if __name__ == '__main__':
    # run game
    ai = PirateGame()
    ai.run_game()