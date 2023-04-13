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

#play_button = pygame.Rect(100, 100, BUTTON_WIDTH, BUTTON_HEIGHT)

class Menu():
    def __init__ (self) :
        pass

    def launch(self):
        screen = pygame.display.set_mode((1500, 720))
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        CENTER = (screen_width/2 ,screen_height/2)
        CENTERW = screen_width/2
        CENTERH = screen_height/2

        bg = pygame.image.load('Tokaido/class/images/menu/bg.jpg')
        bg_width, bg_height = bg.get_size()
        BGCENTER = (CENTERW - bg_width/2 ,CENTERH - bg_height/2)


        pygame.display.set_caption("Menu Tokaido")
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            screen.fill(BG_COLOR)
            screen.blit(bg, BGCENTER)
            #screen.blit(play_button, (CENTERW, (screen_height + CENTERH)/2))
            pygame.display.flip()
        pass

menu = Menu()
menu.launch()