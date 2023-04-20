from math import *
import cv2
import pygame

clock = pygame.time.Clock()

bg = pygame.image.load('Tokaido/class/images/menu/bg.png')
bg_width, bg_height = bg.get_size()
bg_width, bg_height = bg.get_size()
title = pygame.image.load('Tokaido/class/images/menu/title.png')
title_width, title_height = title.get_size()
account = pygame.image.load('Tokaido/class/images/menu/account.png')
hovered_account = pygame.image.load('Tokaido/class/images/menu/hovered_account.png')
account_and_back_rect = account.get_rect()
account_and_back_rect.center = 30+75/2, 30+75/2
back = pygame.image.load('Tokaido/class/images/menu/back.png')
hovered_back = pygame.image.load('Tokaido/class/images/menu/hovered_back.png')

BG_COLOR = (251,253,248)


#ouvre le menu de compte avec une jolie petite animation qui comporte un resize et plusieurs translations
def account_menu(screen, CENTERW, CENTERH):
    
    #Ce sont les dimensions de l'image de depart (seule bg sera resized, donc j'ai pas fait d'effort sur la nomenclature)
    start_size = (1275,627)
    ratio = int(1275/627)


    #Je voulais rescale l'image en utilisant les fonctions de pygame mais le resultat n'etait pas convaincant (interpolation inadaptee a une animation).
    #J'ai donc trouve ca sur Stack Overflow, sans explications evidemment mais je pense avoir compris :
    #On convertit l'image "bg" en caracteres alphanumeriques (sans doute de l'hexadecimal), et on met tout ca dans une matrice
    array = pygame.surfarray.array3d(bg.convert_alpha())
    scaled_size = start_size

    animation_duration = 60
    bg_diff_pos = (0,0)
    title_diff_pos = (0,0)

    #Premiere animation durant laquelle on s'occupe du titre et de l'image
    for i in range (animation_duration) :
        clock.tick(60)


        rescale_animation_speed = 10*exp(-(4/animation_duration*i-0.5)**2)
        bg_animation_speed = 7*exp(-(4/animation_duration*i-2)**2)
        title_animation_speed = 50*exp(-(4/animation_duration*i))


        #On change les dimensions de l'image
        scaled_size = (scaled_size[0]- int(ratio * rescale_animation_speed), scaled_size[1]-int(rescale_animation_speed))

        #On cree une nouvelle matrice a l'aide de la librairie cv2
        #Celle-ci utilisera la matrice faite a l'aide de l'image initiale,
        #les dimensions de la nouvelle matrice,
        #ainsi que le procede d'interpolation d'image utilise (une interpolation bicubique faisant la moyenne de groupes de 4x4 pixels)
        scaled_array = cv2.resize(array, scaled_size[::-1], interpolation = cv2.INTER_CUBIC)

        #On retransforme la matrice en une surface affichable pas pygame
        scaled_image = pygame.surfarray.make_surface(scaled_array)
        scaled_bg_width, scaled_bg_height = scaled_image.get_size()       

        bg_diff_pos = (0,int(bg_diff_pos[1] + bg_animation_speed))
        title_diff_pos = (0,int(title_diff_pos[1] - title_animation_speed))

        screen.fill(BG_COLOR)
        screen.blit(scaled_image, (CENTERW - scaled_bg_width / 2, (CENTERH - scaled_bg_height / 1.5)-(bg_diff_pos[1])))
        screen.blit(title, (CENTERW - title_width/2, (screen.get_height() - 2*title_height)-title_diff_pos[1]))
        pygame.display.flip()

    
    #Seconde animation durant laquelle on se charge cette fois des statistiques et du bouton pour changer de compte
        


    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.MOUSEBUTTONUP and account_and_back_rect.collidepoint((pygame.mouse.get_pos())):
                #On refait l'animation à l'envers
                for i in range (animation_duration) :
                    clock.tick(60)

                    
                    #Il a fallu modifier les équations pour avoir une symétrie de la vitesse par rapport à la 30ième frame
                    rescale_animation_speed = -10*exp(-((4/animation_duration)*(i - 45)- 0.433)**(2))
                    bg_animation_speed = -(7*exp(-(4/animation_duration*(i-2)-0.2)**2))
                    title_animation_speed = -(50*exp(-(4/animation_duration*(-i+60+0.2))))

                    #On change les dimensions de l'image
                    scaled_size = (scaled_size[0]- int(ratio * rescale_animation_speed), scaled_size[1]-int(rescale_animation_speed))

                    #On cree une nouvelle matrice a l'aide de la librairie cv2
                    #Celle-ci utilisera la matrice faite a l'aide de l'image initiale,
                    #les dimensions de la nouvelle matrice,
                    #ainsi que le procede d'interpolation d'image utilise (une interpolation bicubique faisant la moyenne de groupes de 4x4 pixels)
                    scaled_array = cv2.resize(array, scaled_size[::-1], interpolation = cv2.INTER_CUBIC)

                    #On retransforme la matrice en une surface affichable pas pygame
                    scaled_image = pygame.surfarray.make_surface(scaled_array)
                    scaled_bg_width, scaled_bg_height = scaled_image.get_size()       

                    bg_diff_pos = (0,int(bg_diff_pos[1] + bg_animation_speed))
                    title_diff_pos = (0,int(title_diff_pos[1] - title_animation_speed))

                    screen.fill(BG_COLOR)
                    screen.blit(scaled_image, (CENTERW - scaled_bg_width / 2, (CENTERH - scaled_bg_height / 1.5)-(bg_diff_pos[1])))
                    screen.blit(title, (CENTERW - title_width/2, (screen.get_height() - 2*title_height)-title_diff_pos[1]))
                    pygame.display.flip()
                return True


            if account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(hovered_back, (30,30))
            else :
                screen.blit(back, (30,30))

        pygame.display.flip()

    return True


pygame.init()
pygame.display.init()
class Menu():
    def __init__ (self) :
        pass

    def launch(self):
        pygame.display.set_caption("Menu Tokaido")  
        screen = pygame.display.set_mode((0,0), pygame.HWSURFACE|pygame.DOUBLEBUF)
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        CENTERW = screen_width/2
        CENTERH = screen_height/2

        BGCENTER = (CENTERW - bg_width/2 ,CENTERH - bg_height/1.5)
        TITLEPOS = (CENTERW - title_width/2, screen_height - 2*title_height)

        while True :
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEBUTTONUP and account_and_back_rect.collidepoint((pygame.mouse.get_pos())):
                    if account_menu(screen, CENTERW, CENTERH) :
                        pass

                else :
                    screen.fill(BG_COLOR)
                    screen.blit(bg, BGCENTER)
                    screen.blit(title, TITLEPOS)

            if account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(hovered_account, (30,30))
            else :
                screen.blit(account, (30,30))

            pygame.display.flip()
        pass

menu = Menu()
menu.launch()