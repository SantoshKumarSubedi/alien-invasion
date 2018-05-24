import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Initialize the alien and set its starting position."""
    def __init__(self,ai_settings,screen):
        """Initialize the alien and set its starting position."""
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #Load the alien image and set rect attribute
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #start each new alien near the top left of the screenself.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
