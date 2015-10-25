import pygame
import random
from screen_vars import ScreenVars

class Monster(object):
    def __init__(self,x,y,w,h):
        self.screen_vars = ScreenVars()
        self.image = pygame.image.load("monster.jpeg")
        self.width = w
        self.height = h
        self.pos_x = x
        self.pos_y = y

        self.delay = random.randint(10,100)

        self.rect = (self.pos_x,self.pos_y,self.width,self.height)
        self.image = pygame.transform.scale(self.image, (self.width,self.height))

    def get_image(self):
        return self.image

    def get_rect(self):
        if self.delay > 0:
            return (-100,-100,self.width, self.height)
        return self.rect

    def move(self, speed):
        if self.delay>0:
            return

        self.pos_y += speed
        if self.pos_y > self.screen_vars.get_height():
            self.delay = random.randint(10,100)
            self.pos_y = 0
        self.rect = (self.pos_x,self.pos_y,self.width,self.height)

    def update(self):
        if self.delay > 0:
            self.delay -= 1