import pygame
from pygame.sprite import Sprite
from random import randint
class Star(Sprite):
    """A class to manage start moving in the background"""
    def __init__(self,ai_settings,screen):
        """create a bullet object at a random position"""
        super(Star,self).__init__()
        self.screen = screen

        #Create a bullet star at(0,0) and then set correct position
        self.rect = pygame.Rect(0,0,ai_settings.star_width,ai_settings.star_height)
        self.rect.centerx=randint(0,ai_settings.screen_width)
        self.rect.top= randint(0,ai_settings.screen_height/4)

        self.y = float(self.rect.y)

        self.color = ai_settings.star_color
        self.speed_factor = ai_settings.star_speed_factor

    def update(self):

        self.y +=self.speed_factor

        self.rect.y= self.y

    def draw_star(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
