from math import *
import cv2
import pygame
pygame.font.init()

clock = pygame.time.Clock()

bg = pygame.image.load('Tokaido/class/images/menu/bg.png')
bg_width, bg_height = bg.get_size()

title = pygame.image.load('Tokaido/class/images/menu/title.png')
hovered_title = pygame.image.load('Tokaido/class/images/menu/hovered_title.png')
title_rect = title.get_rect()
title_width, title_height = title.get_size()

account = pygame.image.load('Tokaido/class/images/menu/account.png')
hovered_account = pygame.image.load('Tokaido/class/images/menu/hovered_account.png')
back = pygame.image.load('Tokaido/class/images/menu/back.png')
hovered_back = pygame.image.load('Tokaido/class/images/menu/hovered_back.png')
account_and_back_rect = account.get_rect()
account_and_back_rect.center = 30+75/2, 30+75/2

player_police = pygame.font.SysFont("Arial" ,40)
stats_police = pygame.font.SysFont("Arial", 60)

BG_COLOR = (251,253,248)




pygame.init()
pygame.display.init()
class Menu():
    def __init__ (self, player) :
        self.player = player
        pass

    def account_menu(self, screen, CENTERW, CENTERH):     #ouvre le menu de compte avec une jolie petite animation qui comporte un resize et plusieurs translations
    
        #Ce sont les dimensions de l'image de depart (seule bg sera resized, donc j'ai pas fait d'effort sur la nomenclature)
        start_size = (1275,627)
        ratio = int(1275/627)

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        player_surface = player_police.render(str(self.player[0]), 1, (20,20,20))
        player_width = player_surface.get_width()

        stats_surface_victories = stats_police.render("Victoires : " + str(self.player[1]), 1, (20,20,20))
        stats_surface_victories_width, stats_surface_victories_height = stats_surface_victories.get_size()

        stats_surface_defeats = stats_police.render("Défaites : " + str(self.player[2]), 1, (20, 20, 20))
        stats_surface_defeats_width, stats_surface_defeats_height = stats_surface_defeats.get_size()
        
        #Je voulais rescale l'image en utilisant les fonctions de pygame mais le resultat n'etait pas convaincant (interpolation inadaptee a une animation).
        #J'ai donc trouve ca sur Stack Overflow, sans explications evidemment mais je pense avoir compris :
        #On convertit l'image "bg" en caracteres alphanumeriques et on met tout ca dans une matrice
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

            #On change les dimensions de la matrice correspondant a notre image
            scaled_size = (scaled_size[0]- int(ratio * rescale_animation_speed), scaled_size[1]-int(rescale_animation_speed))

            #On cree une nouvelle matrice a l'aide de la librairie cv2
            #Celle-ci utilisera la matrice faite a l'aide de l'image initiale,
            #les dimensions de la nouvelle matrice,
            #ainsi que le procede d'interpolation d'image utilise (une interpolation bicubique faisant la moyenne de groupes de 4x4 pixels)
            scaled_array = cv2.resize(array, scaled_size[::-1], interpolation = cv2.INTER_CUBIC)

            #On transforme la matrice rescaled en une surface affichable par pygame
            scaled_bg = pygame.surfarray.make_surface(scaled_array)
            scaled_bg_width, scaled_bg_height = scaled_bg.get_size()       

            bg_diff_pos = (0,int(bg_diff_pos[1] + bg_animation_speed))
            title_diff_pos = (0,int(title_diff_pos[1] - title_animation_speed))

            screen.fill(BG_COLOR)
            screen.blit(scaled_bg, (CENTERW - scaled_bg_width / 2, (CENTERH - scaled_bg_height / 1.5)-(bg_diff_pos[1])))

            screen.blit(title, (CENTERW - title_width/2, (screen.get_height() - 2*title_height)-title_diff_pos[1]))
            screen.blit(player_surface, (screen_width - player_width - 30, 30))
            pygame.display.flip()

        
        #Seconde animation durant laquelle on se charge cette fois des statistiques et du bouton pour changer de compte
        lim_stats_pos_y = screen_height/2 + screen_height/8
        current_stats_pos_y = screen_height
        i=0
        while current_stats_pos_y > lim_stats_pos_y:
            clock.tick(60)
            i+=1
            stats_animation_speed = 30*exp(-(4/animation_duration*i)**2)
            #stats_diff_pos = (0, int(stats_diff_pos[1]-stats_animation_speed))

            current_stats_pos_y = int(current_stats_pos_y-stats_animation_speed)

            screen.fill(BG_COLOR)
            screen.blit(scaled_bg, (CENTERW - scaled_bg_width / 2, (CENTERH - scaled_bg_height / 1.5)-(bg_diff_pos[1])))

            screen.blit(title, (CENTERW - title_width/2, (screen.get_height() - 2*title_height)-title_diff_pos[1]))
            screen.blit(player_surface, (screen_width - player_width - 30, 30))


            screen.blit(stats_surface_victories, (3*screen_width/10-stats_surface_victories_width/2, current_stats_pos_y))
            screen.blit(stats_surface_defeats, (7*screen_width/10 - stats_surface_defeats_width/2, current_stats_pos_y))

            pygame.display.flip()
            
            

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

                        #C'est litteralement un copier/coller de ce qui a ete fait au dessus
                        scaled_size = (scaled_size[0]- int(ratio * rescale_animation_speed), scaled_size[1]-int(rescale_animation_speed))
                        scaled_array = cv2.resize(array, scaled_size[::-1], interpolation = cv2.INTER_CUBIC)
                        scaled_bg = pygame.surfarray.make_surface(scaled_array)
                        scaled_bg_width, scaled_bg_height = scaled_bg.get_size()       

                        bg_diff_pos = (0,int(bg_diff_pos[1] + bg_animation_speed))
                        title_diff_pos = (0,int(title_diff_pos[1] - title_animation_speed))

                        screen.fill(BG_COLOR)
                        screen.blit(scaled_bg, (CENTERW - scaled_bg_width / 2, (CENTERH - scaled_bg_height / 1.5)-(bg_diff_pos[1])))
                        screen.blit(title, (CENTERW - title_width/2, (screen.get_height() - 2*title_height)-title_diff_pos[1]))
                        title_rect.center = CENTERW - title_width/2, (screen.get_height() - 2*title_height)-title_diff_pos[1]
                        screen.blit(player_surface, (screen_width - player_width - 30, 30))
                        pygame.display.flip()
                    return True


                if account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(hovered_back, (30,30))
                else :
                    screen.blit(back, (30,30))

            pygame.display.flip()

        return True


    def launch(self):
        pygame.display.set_caption("Menu Tokaido")  
        screen = pygame.display.set_mode((0,0), pygame.HWSURFACE|pygame.DOUBLEBUF)
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        CENTERW = screen_width/2
        CENTERH = screen_height/2

        BGCENTER = (CENTERW - bg_width/2 ,CENTERH - bg_height/1.5)
        TITLEPOS = (CENTERW - title_width/2, screen_height - 2*title_height)

        player_surface = player_police.render(str(self.player[0]), 1, (20,20,20))
        player_width = player_surface.get_width()

        while True :
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEBUTTONUP and account_and_back_rect.collidepoint((pygame.mouse.get_pos())):
                    if self.account_menu(screen, CENTERW, CENTERH) :
                        pass

                else :
                    screen.fill(BG_COLOR)
                    screen.blit(bg, BGCENTER)
                    screen.blit(player_surface, (screen_width - player_width - 30, 30))
                    screen.blit(title, TITLEPOS)
                    title_rect.center = TITLEPOS[0] + title.get_width()/2, TITLEPOS[1] + title.get_height()/2

            if account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(hovered_account, (30,30))
            else :
                screen.blit(account, (30,30))

            if title_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(hovered_title, TITLEPOS)
            else :
                screen.blit(title, TITLEPOS)
            
            pygame.display.flip()
        pass