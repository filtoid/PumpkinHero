import pygame
from screen_vars import ScreenVars

class Game(object):
    def __init__(self):
        self.section_1_y = 325
        self.section_2_y = 400
        self.section_3_y = 500

        self.screen_vars = ScreenVars()
        self.dark_yellow = (153,153,0)
        self.yellow = (255,255,0)
        self.dark_green = (0,153,0)
        self.green = (0,255,0)

        self.section_1 = False
        self.section_2 = False
        self.section_3 = False

        self.key_array = [False,False,False,False]
        self.points = 0
        self.started_game = False

    def draw_background(self, screen):
        if self.section_1:
            pygame.draw.rect(screen, self.yellow, (0,self.section_1_y,self.screen_vars.get_width(),75), 0)
        else:
            pygame.draw.rect(screen, self.dark_yellow, (0,self.section_1_y,self.screen_vars.get_width(),75), 0)

        if self.section_2:
            pygame.draw.rect(screen, self.green, (0,self.section_2_y,self.screen_vars.get_width(),100), 0)
        else:
            pygame.draw.rect(screen, self.dark_green, (0,self.section_2_y,self.screen_vars.get_width(),100), 0)

        if self.section_3:
            pygame.draw.rect(screen, self.yellow, (0,self.section_3_y,self.screen_vars.get_width(),75), 0)
        else:
            pygame.draw.rect(screen, self.dark_yellow, (0,self.section_3_y,self.screen_vars.get_width(),75), 0)

    def check_piece(self, pieceary, keymonitor):
        self.section_1 = False
        self.section_2 = False
        self.section_3 = False

        key_just_pressed = [False,False,False,False]

        if keymonitor.get_key(0)==True and self.key_array[0]==False:
            self.key_array[0] = True
            key_just_pressed[0] = True
        elif not keymonitor.get_key(0)==False:
            self.key_array[0] = False

        if keymonitor.get_key(1)==True and self.key_array[1]==False:
            self.key_array[1] = True
            key_just_pressed[1] = True
        elif not keymonitor.get_key(1)==False:
            self.key_array[1] = False

        if keymonitor.get_key(2)==True and self.key_array[2]==False:
            self.key_array[2] = True
            key_just_pressed[2] = True
        elif not keymonitor.get_key(2)==False:
            self.key_array[2] = False

        if keymonitor.get_key(3)==True and self.key_array[3]==False:
            self.key_array[3] = True
            key_just_pressed[3] = True
        elif not keymonitor.get_key(3)==False:
            self.key_array[3] = False


        for index,piece in enumerate(pieceary):
            y_pos = piece.get_y() + piece.get_height()
            if  y_pos > self.section_1_y and y_pos<self.section_1_y+75:
                self.section_1 = True
                if key_just_pressed[index]:
                    piece.kill()
                    self.points += 1

            if  y_pos > self.section_2_y and y_pos<self.section_2_y+100:
                self.section_2 = True
                if key_just_pressed[index]:
                    piece.kill()
                    self.points += 2

            if  y_pos > self.section_3_y and y_pos<self.section_3_y+75:
                self.section_3 = True
                if key_just_pressed[index]:
                    piece.kill()
                    self.points += 1

    def draw_score(self, screen):
    	pass

    def started(self):
	    return self.started_game

    def start(self):
        if self.started_game == False:
		    print("Game starting")
		    self.started_game = True
        else:
            print("Game has already started - can't restart")
