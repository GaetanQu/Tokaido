import pygame
import effets_cases
import Joueur
#import Game

PISTE = pygame.image.load('Tokaido/Class/images/piste_/piste.png')
POINTEUR=pygame.image.load ('Tokaido/Class/images/piste_/fleche.png')

relais_cases=[14,27,41]

#ecart entre les cases
#e et h sont a moduler en fonction de la resolution afin d'adapter a la taille de l'ecran
e=25
ecart_cases_x=[31/25*e,20/25*e,e,e,e,e,e,e,e,e,e*4/5,20/25*e,17/25*e,22/25*e, 30/25*e, 23/25*e,18/25*e,17/25*e,e,e,17/25*e,17/25*e,e,e*12/25,e*33/25,e,e,    35/25*e,e,e*20/25,e*20/25,e,e*17/25,e,e,e*15/25,e,19/25*e,16/25*e,19/25*e,     30/25*e, e,20/25*e,15/25*e,20/25*e,e,e,e,e,e,e,e,e,e]
h=1
ecart_cases_y=[-110*h, 30*h, 0, 0, -30*h, 80*h, 0, 0, -30*h, 8*h, -60*h, 30*h, 0, 30*h, -60*h,0,65*h,0,25*h,0,0,h*10,40*h,0,0,-40*h,0, h     ,30*h, 30*h,0,-10*h,-30*h,0,-30*h,h,-7*h,-30*h,0,0,-50*h,   -30*h,60*h,0,0,-30*h,-30*h,-30*h,-30*h,0,45*h,-35*h,0,35*h]
#ces valeurs doivent (en theorie) placer le premier pointeur en dessous de la case depart
x_pointeur=64/25*e
y_pointeur=550*h





def affichage_piste (screen):
    largeur_piste=screen.get_width()
    hauteur_piste=PISTE.get_height()/PISTE.get_width()*screen.get_width()
    scaled_piste=pygame.transform.smoothscale(PISTE, (largeur_piste, hauteur_piste))
    screen.blit(scaled_piste, (0, screen.get_height()/2-hauteur_piste/2))
    pygame.display.flip()


def launch (screen, joueur, list_players):
    scaled_pointeur=pygame.transform.smoothscale (POINTEUR, (20, 20))
    screen.fill((251,253,248))

    affichage_piste (screen)
    x_pointeur=64/25*e
    a=0
    while a!=joueur.case :
        x_pointeur+=ecart_cases_x[a]
        a+=1
    y_pointeur=550
    a=0
    while a!=joueur.case:
        y_pointeur+=ecart_cases_y[a]
        a+=1
    screen.blit(scaled_pointeur, (x_pointeur, y_pointeur))
    pygame.display.flip()
    no_entry_clic = True
    
    compteur=0
    compteur_relais=0
    while no_entry_clic:
        #Class.Game.affichage_HUD(screen, list_players)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                no_entry_clic = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN :
                    joueur.case+=compteur
                    if  effets_cases.can_stop_here(joueur, list_players)==True:
                        no_entry_clic = False
                    else : 
                        joueur.case-=compteur
                elif event.key == pygame.K_RIGHT:
                    #if joueur.case+compteur<relais_cases[compteur_relais]:
                        x_pointeur += ecart_cases_x[compteur+joueur.case]
                        y_pointeur += ecart_cases_y[compteur+joueur.case]
                        affichage_piste(screen)
                        screen.blit(scaled_pointeur, (x_pointeur, y_pointeur))
                        pygame.display.flip()
                        compteur+=1
                elif event.key == pygame.K_LEFT:
                    if compteur>0:
                        x_pointeur -= ecart_cases_x[compteur+joueur.case-1]
                        y_pointeur -= ecart_cases_y[compteur+joueur.case-1]
                        affichage_piste(screen)
                        screen.blit(scaled_pointeur, (x_pointeur, y_pointeur))
                        pygame.display.flip()
                        compteur-=1
                    
            


    
