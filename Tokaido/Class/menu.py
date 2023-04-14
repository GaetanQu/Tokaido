from tkinter import CENTER
import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

BG_COLOR = (251,253,248)
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60
BUTTON_TEXT_COLOR = BLACK
BUTTON_BACKGROUND_COLOR = WHITE

bg = pygame.image.load('Tokaido/class/images/menu/bg.jpg')
bg_width, bg_height = bg.get_size()

title = pygame.image.load('Tokaido/class/images/menu/title.png')
title_width, title_height = title.get_size()

account = pygame.image.load('Tokaido/class/images/menu/account.png')
account = pygame.transform.scale(account, (75,75))

hovered_account = pygame.image.load('Tokaido/class/images/menu/hovered_account.png')

#play_button = pygame.Rect(100, 100, BUTTON_WIDTH, BUTTON_HEIGHT)

class Menu():
    def __init__ (self) :
        pass

    def launch(self):
        screen = pygame.display.set_mode((0,0))
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        CENTERW = screen_width/2
        CENTERH = screen_height/2

        BGCENTER = (CENTERW - bg_width/2 ,CENTERH - bg_height/1.5)
        TITLEPOS = (CENTERW - title_width/2, screen_height - 2*title_height)


        pygame.display.set_caption("Menu Tokaido")
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

            screen.fill(BG_COLOR)
            screen.blit(bg, BGCENTER)
            screen.blit(title, TITLEPOS)

            account_rect = account.get_rect()
            account_rect.center = 30+75/2, 30+75/2

            if account_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(hovered_account, (30,30))
            else :
                screen.blit(account, (30,30))

            pygame.display.flip()
        pass

menu = Menu()
menu.launch()