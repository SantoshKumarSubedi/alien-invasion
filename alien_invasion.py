import sys

import pygame
from ship import Ship
from settings import Settings


def run_game():
    #initialize game and create a screen object
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")
    #set the background color
    bg_color=(230,230,230)
    ship = Ship(screen)
    #start the main loop for the run_game
    while True:
        #Watch for keyboard and mouse events .
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    #Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
    #make the most recently drown screen visible
        pygame.display.flip()
run_game()
