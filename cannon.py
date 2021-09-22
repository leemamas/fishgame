import pygame
from bullet import Bullet

class Cannon():
    def __init__(self):
        self.image=pygame.image.load('images/cannon1.png')
        self.rect=(520,690)

    def display(self,screen):
        screen.blit(self.image,self.rect)


