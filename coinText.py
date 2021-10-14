# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/9/28  0:30
import pygame

class Cointext():
    def __init__(self,rect,reward,bshape):
        self.images = [pygame.image.load('images/coinText.png').subsurface(i*36, 0, 36, 49) for i in range(0, 11)]
        self.rect=rect
        self.reward=reward
        self.bshape=bshape

    def display(self, screen):
        count=0
        for i in self.change((self.reward*self.bshape)):
            screen.blit(self.images[i], (self.rect[0]+count*36,self.rect[1]))
            count+=1

    def change(self, number):
        l = list(map(int, str(number)))
        ##每个数字前插入X
        l.insert(0,10)
        return l