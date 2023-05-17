import pygame
import Class.effets_cases
import Class.Joueur
import Class.Game

PISTE = pygame.image.load('Tokaido/Class/images/piste_/piste.png')
POINTEUR=pygame.image.load ('Tokaido/Class/images/piste_/fleche.png')

relais_cases=[14,27,41]

#ecart entre les cases
e=35.5
ecart_cases_x=[31/25*e,20/25*e,e,e,e,e,e,e,e,e,e*4/5,20/25*e,17/25*e,22/25*e]
ecart_cases_y=[-110, 30, 0, 0, -30, 80, 0, 0, -30, 8, -60, 30, 0, 30]







def affichage_piste (screen):
    screen.fill((251,253,248))
    largeur_piste=screen.get_width()
    hauteur_piste=PISTE.get_height()/PISTE.get_width()*screen.get_width()
    scaled_piste=pygame.transform.smoothscale(PISTE, (largeur_piste, hauteur_piste))
    screen.blit(scaled_piste, (0, screen.get_height()/2-hauteur_piste/2))


def launch (screen, joueur, list_players):
    scaled_pointeur=pygame.transform.smoothscale (POINTEUR, (20, 20))

    affichage_piste (screen)
    x_pointeur=90
    a=0
    while a!=joueur.case :
        x_pointeur+=ecart_cases_x[a]
        a+=1
    y_pointeur=800
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
        Class.Game.affichage_HUD(screen, list_players)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                no_entry_clic = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN :
                    joueur.case+=compteur
                    if  Class.effets_cases.can_stop_here(joueur, list_players)==True:
                        no_entry_clic = False
                    else : 
                        joueur.case-=compteur
                elif event.key == pygame.K_RIGHT:
                    if joueur.case+compteur<relais_cases[compteur_relais]:
                        x_pointeur += ecart_cases_x[compteur+joueur.case]
                        y_pointeur += ecart_cases_y[compteur+joueur.case]
                        affichage_piste(screen)
                        screen.blit(scaled_pointeur, (x_pointeur, y_pointeur))
                        compteur+=1
                elif event.key == pygame.K_LEFT:
                    if compteur>0:
                        x_pointeur -= ecart_cases_x[compteur+joueur.case-1]
                        y_pointeur -= ecart_cases_y[compteur+joueur.case-1]
                        affichage_piste(screen)
                        screen.blit(scaled_pointeur, (x_pointeur, y_pointeur))
                        compteur-=1
                    
            


    

"""pygame.init()

screen = pygame.display.set_mode((0,0))
joueur = Joueur.Joueur("Test", screen)
joueur.case=0
joueur.personnage='Zen-Emon'

j2=Joueur.Joueur("Test2", screen)
j2.case=4
j2.personnage='Hiroshige'
lst=[joueur, j2]
affichage_pointeur_case(PISTE,POINTEUR,  screen, joueur, lst)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        """