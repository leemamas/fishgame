# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/10/4  6:53

import pygame

class SwitchButton():
    def __init__(self):
        self.plus=pygame.image.load('images/cannon_plus.png')
        self.minus=pygame.image.load('images/cannon_minus.png')
        self.plus_bk=self.plus.copy()
        self.minus_bk=self.minus.copy()
        self.plus_rect=(590,730)
        self.minus_rect=(480,730)
        self.isHit=False

    def display(self,screen):
        screen.blit(self.plus,self.plus_rect)
        screen.blit(self.minus,self.minus_rect)

    def hit(self,cannon):
        x,y=pygame.mouse.get_pos()
        plus_x=self.plus_rect[0]
        plus_y=self.plus_rect[1]
        minus_x=self.minus_rect[0]
        minus_y=self.minus_rect[1]

        if x>=plus_x and x<=self.plus.get_width()+plus_x and y>=plus_y and y<self.plus.get_height()+plus_y:
            self.plus = pygame.image.load('images/cannon_plus_down.png')
            self.isHit = True
            cannon.switch('plus')

        if x>=minus_x and x<=self.minus.get_width()+minus_x and y>=minus_y and y<self.minus.get_height()+minus_y:
            self.minus = pygame.image.load('images/cannon_minus_down.png')
            self.isHit = True
            cannon.switch('minus')


    def back(self):
        self.plus = self.plus_bk
        self.minus = self.minus_bk
        self.isHit = False