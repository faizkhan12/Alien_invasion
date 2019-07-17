#import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
#from alien import Alien
import game_functions as gf

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Turn on music
    pygame.mixer.music.load('sound/Savannah.wav')
    pygame.mixer.music.play(-1)

    #Make the play button
    play_button=Button(ai_settings,screen,"Play")
    

    #Create an instance to store game statistics and create a scoreboard
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    #Make a ship,a group of bullets and a group of aliens
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()

    #Make a group to store bullets in.
    #bullets=Group()

    #Make an alien
    #alien=Alien(ai_settings,screen)

    #Create the fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #set the background color.
    #bg_color=(230,230,230)

    #Start the main loop for the game.
    while True:
       #Watch for keyboard and mouse events.
        #for event in pygame.event.get():
         #   if event.type==pygame.QUIT:
          #      sys.exit()
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        #Redraw the screen during each pass through the loop.
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()

        #make the most recently drawn screen visible.
        #pygame.display.flip()
        
        if stats.game_active:
            ship.update()
        #bullets.update()

        #Deleting old bullets
        #for bullet in bullets.copy():
         #   if bullet.rect.bottom <= 0:
          #      bullets.remove(bullet)
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
            
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
