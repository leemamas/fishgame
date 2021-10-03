# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/10/4  0:32
import pygame
import math

class Coin():
    def __init__(self,rect):
        self.images = [pygame.image.load('images/coinAni1.png').subsurface(0, i*60, 60, 60) for i in range(0, 10)]
        self.key=0
        self.rect_x=rect[0]
        self.rect_y=rect[1]
        self.pos=(200,700)
        self.speed=3
        self.isDestroy=False


    def display(self, screen):
        if not self.isDestroy:
            screen.blit(self.images[self.key], (self.rect_x,self.rect_y))
            self.move()


    def move(self):
        radius,angle=(pygame.Vector2(self.pos)-pygame.Vector2((self.rect_x,self.rect_y))).as_polar()
        if angle<=90:
            x=math.sin(math.radians(90-angle))
            y=math.cos(math.radians(90-angle))
        else:
            x = -(math.sin(math.radians( angle-90)))
            y = math.cos(math.radians(angle-90))

        if self.key<9:
            # 图片变化
            self.key+=1
            self.rect_x+=x*self.speed
            self.rect_y+=y*self.speed
            if self.rect_y>self.pos[1]:
                self.isDestroy=True
        else:
            self.key=0


