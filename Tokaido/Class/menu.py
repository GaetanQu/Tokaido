import pygame
class Menu_():
    pygame.init()
    screen = pygame.display.set_mode((0,0))
    pygame.display.set_caption("Menu Tokaido")
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

    pass
