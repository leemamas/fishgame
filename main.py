import pygame,sys
from cannon import Cannon
from fish import Fish
from number import Number

pygame.init()

pygame.display.set_caption('fish')

bg=pygame.image.load('images/bg.jpg')
bar=pygame.image.load('images/bottom-bar.png')

screen=pygame.display.set_mode((1024,768))

cannon = Cannon()
number=Number()
fishlist=[]

def main():
    score=709394
    ##随机定时产生鱼，即设置一个事件定时器
    PRODUCT_FISH_EVENT=pygame.USEREVENT+1
    pygame.time.set_timer(PRODUCT_FISH_EVENT,3000)

    while 1:

        screen.blit(bg,(0,0))
        screen.blit(bar,((bg.get_width()-bar.get_width())/2,bg.get_height()-bar.get_height()))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==PRODUCT_FISH_EVENT:
                fish = Fish()
                fishlist.append(fish)
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pressed()
                if mouse[0]:
                    ###enemtlist就是fishlist
                    cannon.shot(fishlist)
                    score-=1


        cannon.display(screen)
        cannon.rotate()
        for bullet in cannon.bulletlist:
            bullet.display(screen)
            if bullet.isDestory:
                cannon.bulletlist.remove(bullet)


        for fish in fishlist:
            fish.display(screen)
            fish.move()
            if fish.isAttack:
                fish.net.display(screen)
            if fish.isDestory:
                fishlist.remove(fish)

        # print(fishlist)
        number.display(screen,score)

        pygame.display.update()

if __name__ == '__main__':
    main()