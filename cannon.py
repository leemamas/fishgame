import pygame
from bullet import Bullet

class Cannon():
    def __init__(self):
        self.image = pygame.image.load('images/cannon1.png')
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

    def shot(self):
        bullet=Bullet(self.pos,self.angle)
        self.bulletlist.append(bullet)
