# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/9/23  2:49
import pygame
import random
import pandas as pd

data=[
    (55,296,8,4,1),
    (78,512,8,4,3),
    (72,448,8,4,5),
    (77,472,8,4,8),
    (107,976,8,4,10),
    (105,948,12,8,20),
    (92,1510,10,6,30),
    (174,1512,12,8,40),
    (166,2196,12,8,50),
    (178,1870,10,6,100),
]
cols=['width','height','space','live','score']
idx=list(i for i in range(1,11))
fish=pd.DataFrame(data,columns=cols,index=idx)



class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self).__init__()

        ##随机形态
        self.type=random.randint(1,10)

        self.fish = fish
        self.fish_w = fish.loc[self.type]['width']
        self.fish_h=fish.loc[self.type]['height']/fish.loc[self.type]['space']
        self.fish_l=self.fish_h*fish.loc[self.type]['live']

        self.image_all=pygame.image.load('images/fish'+str(self.type)+'.png')
        self.y=0
        ###0,---》 1,<<---分别代表2个方向，随机旋转
        self.direction=random.randint(0,1)
        ##如果由左向右，X坐标为0 ，反之，即x=1024
        if self.direction==0:
            self.rect_x=0
        else:
            self.rect_x=1024
        self.rect_y=random.randint(0,768)
        ##这里宽高固定 设置动态的
        self.image = self.image_all.subsurface((0, self.y, self.fish_w, self.fish_h))
        self.rect=self.image.get_rect(center=(self.rect_x,self.rect_y))

        self.isDestory=False
        self.isAttack=False
        self.speed=0.3
        self.net=None
        ##设置鱼奖励分数
        self.reward= fish.loc[self.type]['score']
        self.bshape=1
        self.cointext=None
        self.coin=None
        self.count=0
        self.k=1

    def display(self,screen):
        if not self.isAttack:
            if self.y<self.fish_h*(self.fish.loc[self.type]['live']-1):
                if self.y%self.fish_h==0:

                    self.image=self.image_all.subsurface((0,self.y,self.fish_w, self.fish_h))
                    ##0的时候图片正常，1的时候即镜像
                    if self.direction==1:
                        self.image=pygame.transform.flip(self.image,True,False)
                self.y+=1
                # print(self.y)
            else:
                self.y=0
        else:
            if self.k<4:
                if self.count%40==0:
                    self.image=self.image_all.subsurface((0,self.y,self.fish_w, self.fish_h))
                    if self.direction==1:
                        self.image=pygame.transform.flip(self.image,True,False)
                    self.k+=1
                self.count+=1
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






