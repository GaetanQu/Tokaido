import pygame
pygame.init()
BG_COLOR = (251,253,248)

class Menu():
    def __init__ (self) :
        pass

    def launch(self):
        bg = pygame.image.load('Tokaido/class/images/menu/bg.jpg')

        bg_width, bg_height = bg.get_size()

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
            screen.fill(BG_COLOR)
            screen.blit(bg, ((screen_width - bg_width)/2 ,(screen_height - bg_height)/2))
            pygame.display.flip()
        pass

menu = Menu()
menu.launch()   