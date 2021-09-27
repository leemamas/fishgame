# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/9/23  2:49
import pygame
import random
class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self).__init__()
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
        self.image = self.image_all.subsurface((0, self.y, 55, 37))
        self.rect=self.image.get_rect(center=(self.rect_x,self.rect_y))

        self.isDestory=False
        self.isAttack=False
        self.speed=0.5
        self.net=None
        ##设置鱼奖励分数
        self.reward=5
        self.cointext=None

    def display(self,screen):
        if not self.isAttack:
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
        else:
            if self.y<296:
                if self.y%37==0:
                    self.image=self.image_all.subsurface((0,self.y,55,37))
                    if self.direction==1:
                        self.image=pygame.transform.flip(self.image,True,False)
                self.y+=1
            else:
                self.isDestory=True
        screen.blit(self.image,self.rect)

    def move(self):
        ##0:+ 1:-
        if not self.isAttack:
            if self.direction==0:
                self.rect_x+=self.speed
                if self.rect_x>1024:
                    self.isDestory=True
            else:
                self.rect_x-=self.speed
                if self.rect_x<0:
                    self.isDestory=True
        self.rect=self.image.get_rect(center=(self.rect_x,self.rect_y))






