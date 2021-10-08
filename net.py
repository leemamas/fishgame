# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/9/26  6:46
import pygame

class Net():
    def __init__(self,rect,shape):
        self.key=shape
        self.image=pygame.image.load('images/web'+str(self.key)+'.png')
        self.pos=rect
        self.rect=self.image.get_rect(center=self.pos)
        self.count=0
    def display(self,screen):
        # 根据图片大小缩放
        if self.count%10==0:
            self.image=pygame.transform.smoothscale(self.image,(self.image.get_width()+2,self.image.get_height()+2))
            self.rect = self.image.get_rect(center=self.pos)
        screen.blit(self.image,self.rect)
        self.count+=1