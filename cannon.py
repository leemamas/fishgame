import pygame
from bullet import Bullet

class Cannon():
    def __init__(self):
        self.key=1
        self.image = pygame.image.load('images/cannon'+str(self.key)+'.png')
        self.org_image = self.image.copy()
        ##中心点
        self.pos = (555, 735)
        # self.rect=(520,690)
        # 旋转角度
        self.angle = 0
        self.rect = self.image.get_rect(center=self.pos)
        self.bulletlist=[]

    def display(self,screen):
        screen.blit(self.image,self.rect)

    ##旋转
    def rotate(self):
        ##1.通过键盘
        # keyboard=pygame.key.get_pressed()
        # if keyboard[pygame.K_a]:
        #     self.angle+=1
        # if keyboard[pygame.K_d]:
        #     self.angle-=1
        #

        ##2.根据鼠标位置转动
        # print(pygame.mouse.get_pos())
        radius, angle = (pygame.mouse.get_pos() - pygame.Vector2(self.pos)).as_polar()
        self.angle = -angle - 90

        self.image = pygame.transform.rotate(self.org_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

    def shot(self,enemtlist):
        bullet=Bullet(self.pos,self.angle,enemtlist,self.key)
        self.bulletlist.append(bullet)


    def switch(self,symbol):
        if symbol=='plus':
            if self.key==7:
                self.key=1
            else:
                self.key += 1
        if symbol=='minus':
            if self.key==1:
                self.key=7
            else:
                self.key-=1
        self.image = pygame.image.load('images/cannon' + str(self.key) + '.png')
        self.org_image = self.image.copy()