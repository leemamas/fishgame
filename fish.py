# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/9/23  2:49
import pygame
import random
class Fish():
    def __init__(self):
        self.image_all=pygame.image.load('images/fish1.png')
        self.y=0
        ###0,---》 1,<<---分别代表2个方向，随机旋转
        self.direction=random.randint(0,1)
        ##如果由左向右，X坐标为0 ，反之，即x=1024
        if self.direction==0:
            self.rect_x=0
        else:
            self.rect_x=1024
        self.rect_y=random.randint(0,768)
        self.rect=(self.rect_x,self.rect_y)
        print(self.rect)
    def display(self,screen):
        if self.y<111:
            if self.y%37==0:

                self.image=self.image_all.subsurface((0,self.y,55,37))
                ##0的时候图片正常，1的时候即镜像
                if self.direction==1:
                    self.image=pygame.transform.flip(self.image,True,False)
            self.y+=0.5
            # print(self.y)
        else:
            self.y=0
        screen.blit(self.image,self.rect)

    def move(self):
        ##0:+ 1:-
        if self.direction==0:
            self.rect_x+=0.5
        else:
            self.rect_x-=0.5
        self.rect=(self.rect_x,self.rect_y)




