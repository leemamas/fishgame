import pygame,sys
from cannon import Cannon

pygame.init()

pygame.display.set_caption('fish')

bg=pygame.image.load('images/bg.jpg')
bar=pygame.image.load('images/bottom-bar.png')

screen=pygame.display.set_mode((1024,768))

cannon = Cannon()

def main():
    while 1:

        screen.blit(bg,(0,0))
        screen.blit(bar,((bg.get_width()-bar.get_width())/2,bg.get_height()-bar.get_height()))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pressed()
                if mouse[0]:
                    cannon.shot()


        cannon.display(screen)
        cannon.rotate()
        for bullet in cannon.bulletlist:
            bullet.display(screen)
            if bullet.isDestory:
                cannon.bulletlist.remove(bullet)

        print(cannon.bulletlist)

        pygame.display.update()

if __name__ == '__main__':
    main()