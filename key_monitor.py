import pygame
import time

class KeyMonitor(object):
        def __init__(self):
    	    self.TIME_OUT = 1
            self.key_array = [False,False,False,False]
            self.key_array_timeout = [0,0,0,0]

        def key_down(self, evt):
            
            if evt.key == pygame.K_LEFT or evt.key == pygame.K_a:
                self.key_array[0] = True
                self.key_array_timeout[0] = time.time()
            elif evt.key == pygame.K_UP or evt.key == pygame.K_w:
                self.key_array[1] = True
                self.key_array_timeout[1] = time.time()
            elif evt.key == pygame.K_DOWN or evt.key == pygame.K_s:
                self.key_array[2] = True
                self.key_array_timeout[2] = time.time()
            elif evt.key == pygame.K_RIGHT or evt.key == pygame.K_d:
                self.key_array[3] = True
                self.key_array_timeout[3] = time.time()


        def key_up(self, evt):
            if evt.key == pygame.K_LEFT:
                self.key_array[0] = False
            elif evt.key == pygame.K_UP:
                self.key_array[1] = False
            elif evt.key == pygame.K_DOWN:
                self.key_array[2] = False
            elif evt.key == pygame.K_RIGHT:
                self.key_array[3] = False

        def get_key(self, index):
            return self.key_array[index]

        def tick(self):
            for index,kt in enumerate(self.key_array_timeout):
                if time.time()-kt>self.TIME_OUT:
                    self.key_array[index] = False
