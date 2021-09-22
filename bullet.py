# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/9/22  15:05

import pygame
import math
class Bullet():
    def __init__(self,pos,angle):

        self.image=pygame.image.load('images/bullet1.png')
        self.org_image=self.image.copy()
        self.angle=angle
        self.image=pygame.transform.rotate(self.org_image,self.angle)
        self.distance=50
        self.pos_x=math.sin(math.radians(-self.angle))*self.distance+pos[0]
        self.pos_y=pos[1]-math.cos(math.radians(math.fabs(self.angle)))*self.distance
        self.pos=(self.pos_x,self.pos_y)

        self.rect=self.image.get_rect(center=self.pos)

        self.speed=3
        self.isDestory=False

    def display(self, screen):
        screen.blit(self.image, self.rect)
        self.move()

    def move(self):
        self.pos_x+=math.sin(math.radians(-self.angle))*self.speed
        self.pos_y-=math.cos(math.radians(math.fabs(self.angle)))*self.speed

        self.pos = (self.pos_x, self.pos_y)
        self.rect = self.image.get_rect(center=self.pos)

        if self.pos_y<0 or self.pos_x<0 or self.pos_x>1024:
            self.isDestory=True

