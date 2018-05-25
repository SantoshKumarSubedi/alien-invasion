import sys
from bullet import Bullet
from alien import Alien
from star import Star
import pygame

def check_keydown_event(event, ai_settings, screen, ship,bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True;
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """respond to  keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullets(bullets):
    """update position of bullets and get rid of old bullets."""
    bullets.update()

    #Get rid of bullets that have disappeared .
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_star(stars):
    stars.update()

    for star in stars.copy():
        if star.rect.bottom >= 700:
            stars.remove(star)

def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet if limit not reached yet."""
    #create a new bullet if limit not reached yet.
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_star(ai_settings,screen,stars):
    if len(stars) < ai_settings.star_allowed:
        new_star = Star(ai_settings,screen)
        stars.add(new_star)

def get_number_aliens_x(ai_settings,alien_width):
    """determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x/(2*alien_width))
    return number_alien_x
def get_number_rows(ai_settings,ship_height,alien_height):
    """Determine then number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien=Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien=Alien(ai_settings,screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
    """create a full fleet of aliens."""
    #Create an alien and find the number of aliens in a row .
    alien = Alien(ai_settings,screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #create the first row of aliens .
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)


def update_screen(ai_settings,screen, ship,aliens, bullets,stars):
    """Update images on the screen and flip to the new screens."""
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    for star in stars.sprites():
        star.draw_star()
    #Redraw all bullets behind ship and aliens .
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #Make the most recently drawn screen visible
    pygame.display.flip()
