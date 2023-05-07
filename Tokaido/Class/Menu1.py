"""
Ce programme permet l'execution du menu principal du jeu, ou on l'on pourra choisir de jouer seul, a plusieurs sur un meme ordinateur, ou bien a plusieurs en reseau local
On pourra egalement consulter ses statistiques en cliquant sur le menu a cote de notre pseudo en haut a gauche, et une croix permet de fermer la fenetre en haut a droite

Pour l'instant il n'est pas tres propre, mais on le retravaillera plus tard si on arrive a trouver le temps
"""


from math import *
from turtle import bgcolor
import cv2
import pygame

class Menu():
    def __init__ (self, player) :
        self.player = player
        pygame.init()
        pygame.display.init()
        pygame.font.init()


        ##--Par mesure de simplicite, on met tout en global (necessaire pour passer de l'authenticator au menu et vice-versa)--##
        
        #on commence par l'horloge
        global clock
        clock = pygame.time.Clock()


        #puis les images avec leurs differentes caracteristiques
        global bg, title, account, back, croix
        global bg_width, bg_height, BG_COLOR
        global title_rect, title_width, title_height, hovered_title
        global account_and_back_rect, hovered_account, hovered_back
        global croix_rect, hovered_croix
        
        #puis les polices
        global player_font
        global stats_font
        global disconnect_font, disconnect_surface, hovered_disconnect_surface, disconnect_rect, disconnect_width, disconnect_height
        global play_font, play_solo_surface, hovered_play_solo_surface, play_solo_rect, play_split_surface, hovered_play_split_surface, play_split_rect

        #Apres avoir definit nos variables, on y met ce dont on a besoin (images, texte, dimensions...)

        #D'abord les images
        bg = pygame.image.load('Tokaido/class/images/menu/bg.png')
        bg_width, bg_height = bg.get_size()
        BG_COLOR = (251,253,248)

        croix = pygame.image.load('Tokaido/class/images/menu/croix.png')
        hovered_croix = pygame.image.load('Tokaido/class/images/menu/hovered_croix.png')
        croix_rect = croix.get_rect()

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

        #puis les polices

        #J'importe la police "Japon" que j'aie obtenue sur DaFont dans une variable pour la rappeler plus facilement
        JAPON = 'Tokaido/Fonts/Japon.ttf'

        player_font = pygame.font.Font(JAPON ,40)
        stats_font = pygame.font.Font(JAPON, 100)

        play_font = pygame.font.Font(JAPON, 30)
        PLAY_COLOR = (70,70,70)
        HOVERED_PLAY_COLOR = (150,150,150)

        play_solo_surface = play_font.render("Jouer seul", 1, PLAY_COLOR)
        hovered_play_solo_surface = play_font.render("Jouer seul", 1, HOVERED_PLAY_COLOR)
        play_solo_rect = play_solo_surface.get_rect()

        play_split_surface = play_font.render("Jouer ensemble sur le meme ecran", 1, PLAY_COLOR)
        hovered_play_split_surface = play_font.render("Jouer ensemble sur le meme ecran", 1, HOVERED_PLAY_COLOR)
        play_split_rect = play_split_surface.get_rect()


        disconnect_font = pygame.font.Font(JAPON, 25)
        disconnect_surface = disconnect_font.render("Changer de compte", 1, (70,70,70))
        hovered_disconnect_surface = disconnect_font.render("Changer de compte", 1, (0,0,0))
        disconnect_width, disconnect_height = disconnect_surface.get_size()
        disconnect_rect = disconnect_surface.get_rect()

    def account_menu(self): #ouvre le menu de compte avec une jolie petite animation qui comporte un resize et plusieurs translations
    
        #Ce sont les dimensions de l'image de depart (seule bg sera resized, donc j'ai pas fait d'effort sur la nomenclature)
        start_size = (1275,627)
        ratio = int(1275/627)

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        player_surface = player_font.render(str(self.player[0]), 1, (50,50,50))

        DISCONNECT_POS = screen_width - disconnect_width - 10, screen_height - disconnect_height - 10
        disconnect_rect.center = screen_width - disconnect_width - 10 + disconnect_width/2, screen_height - disconnect_height - 10 + disconnect_height/2

        stats_surface_victories = stats_font.render("Victoires : " + str(self.player[1]), 1, (50,50,50))
        stats_surface_victories_width = stats_surface_victories.get_width()

        stats_surface_defeats = stats_font.render("Defaites : " + str(self.player[2]), 1, (50,50,50))
        stats_surface_defeats_width = stats_surface_defeats.get_width()
        
        #Je voulais rescale l'image en utilisant les fonctions de pygame mais le resultat n'etait pas convaincant (interpolation inadaptee a une animation).
        #J'ai donc trouve ca sur Stack Overflow, sans explications evidemment mais je pense avoir compris (les explications seront precedee de "##") :

        ##On convertit l'image "bg" en caracteres alphanumeriques et on met tout ca dans une matrice
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

            ##On change les dimensions de la matrice correspondant a notre image
            scaled_size = (scaled_size[0]- int(ratio * rescale_animation_speed), scaled_size[1]-int(rescale_animation_speed))

            ##On cree une nouvelle matrice a l'aide de la librairie cv2
            ##Celle-ci utilisera la matrice faite a l'aide de l'image initiale,
            ##les dimensions de la nouvelle matrice,
            ##ainsi que le procede d'interpolation d'image utilise (une interpolation bicubique faisant la moyenne de groupes de 4x4 pixels)
            scaled_array = cv2.resize(array, scaled_size[::-1], interpolation = cv2.INTER_CUBIC)

            ##On transforme la matrice rescaled en une surface affichable par pygame
            scaled_bg = pygame.surfarray.make_surface(scaled_array)
            scaled_bg_width, scaled_bg_height = scaled_bg.get_size()       

            bg_diff_pos = (0,int(bg_diff_pos[1] + bg_animation_speed))
            title_diff_pos = (0,int(title_diff_pos[1] - title_animation_speed))

            screen.fill(BG_COLOR)
            screen.blit(scaled_bg, (CENTERW - scaled_bg_width / 2, (CENTERH - scaled_bg_height / 1.5)-(bg_diff_pos[1])))

            screen.blit(title, (CENTERW - title_width/2, (screen.get_height() - 2*title_height)-title_diff_pos[1]))
            screen.blit(player_surface, (30 + 75 + 10, 30+75/4))
            screen.blit(back, (45,45))
            screen.blit(croix, CROIX_POS)
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
            screen.blit(player_surface, (30 + 75 + 10, 30+75/4))


            screen.blit(stats_surface_victories, (3*screen_width/10-stats_surface_victories_width/2, current_stats_pos_y))
            screen.blit(stats_surface_defeats, (7*screen_width/10 - stats_surface_defeats_width/2, current_stats_pos_y))

            screen.blit(back, (45,45))
            screen.blit(croix, CROIX_POS)
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
                        screen.blit(player_surface, (30 + 75 + 10, 30+75/4))
                        screen.blit(account, (30,30))
                        screen.blit(croix, CROIX_POS)
                        pygame.display.flip()
                    return True

                if disconnect_rect.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(hovered_disconnect_surface, DISCONNECT_POS)
                else :
                    screen.blit(disconnect_surface, DISCONNECT_POS)

                if event.type == pygame.MOUSEBUTTONUP and disconnect_rect.collidepoint(pygame.mouse.get_pos()) :
                    return "deconnexion"

                if event.type == pygame.MOUSEBUTTONUP and croix_rect.collidepoint(pygame.mouse.get_pos()):
                    return "quit"

                if croix_rect.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(hovered_croix, CROIX_POS)
                else :
                    screen.blit(croix, CROIX_POS)

                if account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(hovered_back, (45,45))
                else :
                    screen.blit(back, (45,45))

            pygame.display.flip()


    def launch(self):
        global screen
        screen = pygame.display.set_mode((0,0))
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        global CENTERW, CENTERH
        CENTERW = screen_width/2
        CENTERH = screen_height/2

        BGCENTER = (CENTERW - bg_width/2 ,CENTERH - bg_height/1.5)
        TITLEPOS = (CENTERW - title_width/2, screen_height - 2*title_height)

        player_surface = player_font.render(str(self.player[0]), 1, (50,50,50))
        global player_width
        player_width = player_surface.get_width()

        while True :
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "quit"

                if event.type == pygame.MOUSEBUTTONUP and account_and_back_rect.collidepoint((pygame.mouse.get_pos())):
                    action = self.account_menu()
                    if action == "deconnexion" :
                        pygame.quit()
                        return"deconnexion"

                    elif action == "quit":
                        pygame.quit()
                        return "quit"

                if event.type == pygame.MOUSEBUTTONUP and croix_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    return "quit"

                else :
                    screen.fill(BG_COLOR)
                    screen.blit(bg, BGCENTER)
                    screen.blit(player_surface, (30+75+10, 30+75/4))
                    screen.blit(title, TITLEPOS)
                    title_rect.center = TITLEPOS[0] + title.get_width()/2, TITLEPOS[1] + title.get_height()/2

                    if account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(hovered_account, (30,30))
                    else :
                        screen.blit(account, (30,30))

                    if title_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(title, TITLEPOS)
                    else :
                        screen.blit(hovered_title, TITLEPOS)

                    global CROIX_POS

                    """Ca on pourrait choisir de ne le faire qu'une fois"""
                    CROIX_POS = (screen_width - 50 - 10, 10)
                    croix_rect.center = CROIX_POS[0] + 25, CROIX_POS[1]+25

                    if croix_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(hovered_croix, CROIX_POS)
                    else :
                        screen.blit(croix, CROIX_POS)

                    play_split_rect.center = 10, screen_height - 30
                    play_solo_rect.center = 10, screen_height - play_split_rect.y - 10

                    if play_split_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(hovered_play_split_surface, (10, screen_height-30))
                    else :
                        screen.blit(play_split_surface, (10, screen_height - 30))

                    

            pygame.display.flip()

menu = Menu(["Anateh", 8, 2])
menu.launch()