import pygame 

from pygame.sprite import Sprite 

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet at rect (0, 0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet's y position as a decimal Value
        self.y = float(self.rect.y)
    def update(self):
        """Move the bullet up the screen"""
        #update decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #update the rectangle's position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet onto the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


