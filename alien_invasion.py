import pygame
from pygame.sprite import Group
from ship import Ship
from star import Star
from settings import Settings
import game_functions as gf


def run_game():
    #initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings,screen)

    #Make a group to store bullets in .
    bullets = Group()
    aliens = Group()
    stars = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #start the main loop for the run_game
    while True:
        #Watch for keyboard and mouse events .
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.create_star(ai_settings,screen,stars)
        gf.update_star(stars)
        gf.update_alien(ai_settings,aliens)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,stars)


run_game()
