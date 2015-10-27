import pygame

class KeyMonitor(object):
        def __init__(self):
            self.key_array = [False,False,False,False]

        def key_down(self, evt):
            if evt.key == pygame.K_LEFT:
                self.key_array[0] = True
            elif evt.key == pygame.K_UP:
                self.key_array[1] = True
            elif evt.key == pygame.K_DOWN:
                self.key_array[2] = True
            elif evt.key == pygame.K_RIGHT:
                self.key_array[3] = True

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
