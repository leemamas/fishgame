# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/9/26  11:07
import pygame

class Number():
    def __init__(self):
        self.images=[pygame.image.load('images/number_black.png').subsurface(0,i*24,20,24) for i in range(0,10)]

    def display(self,screen,number):
        count=0
        for i in self.change(number):
            screen.blit(self.images[i],(150+count*23,740))
            count+=1

    def change(self,number):
        l=list(map(int,str(number)))
        if len(l)<6:
            for i in range(0,6-len(l)):
                l.insert(0,0)

        result=[]
        for n in l:
            result.append(abs(n-9))
        # print(result)
        return result