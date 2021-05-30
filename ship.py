import pygame

# Class to manage the player's ship
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    # Draw the ship at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)