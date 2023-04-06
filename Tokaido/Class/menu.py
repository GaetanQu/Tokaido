from codecs import backslashreplace_errors
import pygame
pygame.init()
WHITE = (255,255,255)

bg_width = 1920
bg_height = 1080

class Menu():
    def __init__ (self) :
        pass

    def launch(self):
        bg = pygame.image.load('Tokaido/class/images/menu/bg.jpg')

        screen = pygame.display.set_mode((0,0))

        pygame.transform.scale(bg, (bg_width,bg_height))

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        pygame.display.set_caption("Menu Tokaido")
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            screen.fill(WHITE)
            screen.blit(bg, ((screen_width - bg_width)/2 ,(screen_height - bg_height)/2))
            pygame.display.flip()
        pass

menu = Menu()
menu.launch()