import pygame
import time
from screen_vars import ScreenVars

from witch import Witch
import pprint

pygame.init()

FRAME_TIME = 50 #50ms is 20 frames per second

if __name__ == '__main__':
    print("Starting Pumpkin Hero...")
    screen_vars = ScreenVars()
    screen = pygame.display.set_mode((screen_vars.get_width(), screen_vars.get_height()))

    black = (0,0,0)

    witch = Witch(25,0,50,100)

    done = False
    last_time = time.time()*1000.0
    SPEED = 5

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

        if (time.time()*1000.0)-last_time > FRAME_TIME:
            last_time = time.time()*1000.0

            witch.update()
            witch.move(SPEED)

            screen.fill(black)
            screen.blit(witch.get_image(), witch.get_rect())

            pygame.display.flip()
