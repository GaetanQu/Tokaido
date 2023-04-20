import pygame
pygame.init()

BG_COLOR = (251,253,248)

bg = pygame.image.load('Tokaido/class/images/account/bg.png')
bg_width, bg_height = bg.get_size()

back = pygame.image.load('Tokaido/class/images/account/back.png')
hovered_back = pygame.image.load('Tokaido/class/images/account/hovered_back.png')
back_rect = back.get_rect()
back_rect.center = 75,75

class Account():
    def __init__(self):
        pass
    def launch(self):
        screen = pygame.display.set_mode((0,0))
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        CENTERW = screen_width/2
        CENTERH = screen_height/2

        BGPOS = (CENTERW - bg_width/2 ,CENTERH - bg_height)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    pygame.quit()
                    break

            screen.fill(BG_COLOR)
            screen.blit(bg, BGPOS)

            if back_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(hovered_back, (30,30))
            else :
                screen.blit(back, (30,30))
            pygame.display.flip()

    pass

account = Account()
#account.launch()


