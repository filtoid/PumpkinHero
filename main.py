import pygame
import time
from key_monitor import KeyMonitor
from screen_vars import ScreenVars

from game import Game
from witch import Witch
from zombie import Zombie
from monster import Monster
from skeleton import Skeleton

import pprint

pygame.init()

FRAME_TIME = 50 #50ms is 20 frames per second

if __name__ == '__main__':
    print("Starting Pumpkin Hero...")
    screen_vars = ScreenVars()
    screen = pygame.display.set_mode((screen_vars.get_width(), screen_vars.get_height()))

    black = (0,0,0)

    witch = Witch(50,0,100,200)
    zombie = Zombie(250,0,100,200)
    monster = Monster(450,0,100,200)
    skeleton = Skeleton(650,0,100,200)

    done = False
    last_time = time.time()*1000.0
    SPEED = 5
    game = Game()
    key_monitor = KeyMonitor()

    #Message pump
    while not done:
        for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            done = True
	        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
	            done = True
	        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and game.started()==False:
		        #print("starting new game")
			    game.start()
			    last_time = time.time()*1000
	        elif event.type == pygame.KEYDOWN:
	            #print(event.key)
	            key_monitor.key_down(event)
	        elif event.type == pygame.KEYUP:
	            key_monitor.key_up(event)

        # Game loop
        if game.started() and (time.time()*1000.0)-last_time > FRAME_TIME:
            last_time = time.time()*1000.0

            witch.update()
            zombie.update()
            monster.update()
            skeleton.update()

            witch.move(SPEED)
            zombie.move(SPEED)
            monster.move(SPEED)
            skeleton.move(SPEED)

            screen.fill(black)

            game.check_piece([witch,zombie,monster,skeleton], key_monitor)

            game.draw_background(screen)

            screen.blit(witch.get_image(), witch.get_rect())
            screen.blit(zombie.get_image(), zombie.get_rect())
            screen.blit(monster.get_image(), monster.get_rect())
            screen.blit(skeleton.get_image(), skeleton.get_rect())

            pygame.display.flip()
        elif not game.started():
			game.draw_score(screen)
