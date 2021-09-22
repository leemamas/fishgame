# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/9/23  2:49
import pygame

class Fish():
    def __init__(self):
        self.image_all=pygame.image.load('images/fish1.png')
        self.y=0
        self.rect_x=0
        self.rect_y=300
        self.rect=(self.rect_x,self.rect_y)
    def display(self,screen):
        if self.y<111:
            if self.y%37==0:
                self.image=self.image_all.subsurface((0,self.y,55,37))
            self.y+=0.5
            print(self.y)
        else:
            self.y=0
        screen.blit(self.image,self.rect)

    def move(self):
        self.rect_x+=0.5
        self.rect=(self.rect_x,self.rect_y)



