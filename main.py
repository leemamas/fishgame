import pygame,sys
from cannon import Cannon
from fish import Fish
from number import Number
from switchButton import SwitchButton


pygame.init()

pygame.display.set_caption('fish')

bg=pygame.image.load('images/bg.jpg')
bar=pygame.image.load('images/bottom-bar.png')
start_bg=pygame.image.load('images/start.jpg')
pause=pygame.image.load('images/pause.png')


screen=pygame.display.set_mode((1024,768))

cannon = Cannon()
number=Number()
fishlist=[]
switchButton=SwitchButton()
score=709394

def main():
    PAUSE=False
    global score
    ##随机定时产生鱼，即设置一个事件定时器
    PRODUCT_FISH_EVENT=pygame.USEREVENT+1
    pygame.time.set_timer(PRODUCT_FISH_EVENT,3000)

    fps=120
    tClock=pygame.time.Clock()

    while 1:


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==PRODUCT_FISH_EVENT:
                fish = Fish()
                fishlist.append(fish)
            if event.type==pygame.KEYDOWN:
                if event.key==27:
                    PAUSE=not PAUSE
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pressed()
                if mouse[0]:
                    ###enemtlist就是fishlist
                    switchButton.hit(cannon)
                    if not switchButton.isHit:
                        cannon.shot(fishlist)
                        ##射击扣减根据炮弹不同。
                        score-=cannon.key
                    if PAUSE:
                        x,y=pygame.mouse.get_pos()
                        if x >= 460 and x <= 757 and y >= 253 and y <= 340:
                            PAUSE=not PAUSE
                        if x >= 460 and x <= 757 and y >= 395 and y <= 484:
                            start()
                        if x >= 460 and x <= 757 and y >= 536 and y <= 619:
                            quit()

            if event.type==pygame.MOUSEBUTTONUP:
                switchButton.back()


        if not PAUSE:
            screen.blit(bg, (0, 0))
            screen.blit(bar, ((bg.get_width() - bar.get_width()) / 2, bg.get_height() - bar.get_height()))

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
                    fish.cointext.display(screen)
                    fish.coin.display(screen)
                if fish.isDestory:
                    fishlist.remove(fish)
                ##捕获鱼增加分数
                if fish.isAttack and fish.isDestory:
                    score+=(fish.reward*fish.bshape)

            # print(fishlist)
            number.display(screen,score)
            switchButton.display(screen)

            tClock.tick(fps)
        else:
            screen.blit(pause, (0, 0))
        pygame.display.update()

def start():
    while 1:
        screen.blit(start_bg,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pressed()
                x,y=pygame.mouse.get_pos()
                if mouse[0]:
                    if x>=360 and x<=658 and y>=353 and  y<=427:
                        main()

        pygame.display.flip()


if __name__ == '__main__':
    start()
