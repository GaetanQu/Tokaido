import pygame
import effets_cases
import Joueur
import Game

PISTE = pygame.image.load('Tokaido/Class/images/piste_/piste.png')
POINTEUR=pygame.image.load ('Tokaido/Class/images/piste_/fleche.png')

relais_cases=[14,27,41]

#ecart entre les cases
e=25
ecart_cases_x=[31/25*e,20/25*e,e,e,e,e,e,e,e,e,e*4/5,20/25*e,17/25*e,22/25*e, e, e,e,e,e,e,e,e,e,e,e,e,e]
h=1
ecart_cases_y=[-110*h, 30*h, 0, 0, -30*h, 80*h, 0, 0, -30*h, 8*h, -60*h, 30*h, 0, 30*h, h,h,h,h,h,h,h,h,h,h,h,h,h]







def affichage_piste (screen):
    largeur_piste=screen.get_width()
    hauteur_piste=PISTE.get_height()/PISTE.get_width()*screen.get_width()
    scaled_piste=pygame.transform.smoothscale(PISTE, (largeur_piste, hauteur_piste))
    screen.blit(scaled_piste, (0, screen.get_height()/2-hauteur_piste/2))
    pygame.display.flip()


def launch (screen, joueur, list_players):
    scaled_pointeur=pygame.transform.smoothscale (POINTEUR, (20, 20))
    affichage_piste (screen)
    x_pointeur=63
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
                        #Game.affichage_HUD(screen,  list_players)
                        screen.blit(scaled_pointeur, (x_pointeur, y_pointeur))
                        pygame.display.flip()
                        compteur+=1
                elif event.key == pygame.K_LEFT:
                    if compteur>0:
                        x_pointeur -= ecart_cases_x[compteur+joueur.case-1]
                        y_pointeur -= ecart_cases_y[compteur+joueur.case-1]
                        affichage_piste(screen)
                        #Game.affichage_HUD(screen,  list_players)
                        screen.blit(scaled_pointeur, (x_pointeur, y_pointeur))
                        pygame.display.flip()
                        compteur-=1

                #else :
                    #Game.affichage_HUD(screen, list_players)
            


    

pygame.init()

screen = pygame.display.set_mode((0,0))
joueur = Joueur.Joueur("Test", screen)
joueur.case=0
joueur.personnage='Zen-Emon'

j2=Joueur.Joueur("Test2", screen)
j2.case=4
j2.personnage='Hiroshige'
lst=[joueur, j2]
launch(screen, joueur, lst)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break



'''def affichage_HUD(screen, liste_joueurs):
    PLAYER_SUFRACE_HEIGHT = 150
    MAIN_PLAYER_POS = (0,screen.get_size()[1] - PLAYER_SUFRACE_HEIGHT)
    
    JETON_POS = (int(0.5 * JETON_SIZE[0]),MAIN_PLAYER_POS[1] - 0.5 * JETON_SIZE[1]/2)

    MAIN_PLAYER_TEXT_POS = (JETON_POS[0] + JETON_SIZE[0] + 10, JETON_POS[1] + JETON_SIZE[1] - 30)
    OTHER_PLAYERS_POS = (0,0)

    CARDS_VIEWERS_POS = (screen.get_size()[0]/2 - cards_viewer.get_size()[0]/2, MAIN_PLAYER_POS[1] + cards_viewer.get_size()[1]/3)
    cards_viewers_rect.center = centrage_rect(cards_viewer, CARDS_VIEWERS_POS)

    points = CURRENT_STATS_FONT.render("Points : " + str(liste_joueurs[0].points), 1, (0,0,0))
    little_points = LITTLE_STATS_FONT.render(str(liste_joueurs[0].points), 1, (0,0,0))
    pieces = CURRENT_STATS_FONT.render(str(liste_joueurs[0].pieces), 1, (0,0,0))

    PIECE_POS = (screen.get_size()[0] - 100 -  POINTS_WIDTH, MAIN_PLAYER_POS[1] + PLAYER_SUFRACE_HEIGHT / 2 - 50)

    liste_pseudo_joueurs = []
    for joueur in liste_joueurs:
        liste_pseudo_joueurs.append(joueur.nom)

    while len(liste_pseudo_joueurs) < 5:
        liste_pseudo_joueurs.append("")

    main_player_text_surface = MAIN_PLAYER_FONT.render(liste_joueurs[0].nom, 1, (0,0,0))

    dico_perso_joueurs = {}
    for joueur in liste_joueurs:
        dico_perso_joueurs[joueur.nom] = joueur.personnage
    
    main_player_surface = pygame.Surface((screen.get_size()[0], PLAYER_SUFRACE_HEIGHT))
    main_player_rect = main_player_surface.get_rect()
    main_player_rect.topleft = MAIN_PLAYER_POS
    other_players_surface = pygame.Surface((screen.get_size()[0], PLAYER_SUFRACE_HEIGHT))

    main_player_surface.fill(HUD_COLOR)
    main_player_surface.set_alpha(100)

    other_players_surface.fill(HUD_COLOR)
    other_players_surface.set_alpha(150)    

    if main_player_rect.collidepoint(pygame.mouse.get_pos()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        screen.fill(BG_COLOR)

        if cards_viewers_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(hovered_cards_viewer, CARDS_VIEWERS_POS)
        else :
            screen.blit(cards_viewer, CARDS_VIEWERS_POS)

        screen.blit(main_player_surface, MAIN_PLAYER_POS)
        screen.blit(other_players_surface, OTHER_PLAYERS_POS)
        screen.blit(main_player_text_surface, MAIN_PLAYER_TEXT_POS)
        
        screen.blit(points, (screen.get_width() - points.get_width() - 50, screen.get_height() - PLAYER_SUFRACE_HEIGHT / 2 - points.get_height()/2))
        screen.blit(piece, PIECE_POS)
        screen.blit(pieces, (PIECE_POS[0] + piece.get_width() - 5, PIECE_POS[1] + piece.get_height() - 50))
        screen.blit(jetons_persos[liste_joueurs[0].personnage], JETON_POS)

        i = 1
        for joueur in liste_joueurs:
            if joueur.nom != None :
                OP_POS = (10 + (i-2) * (JETON_SIZE[0] + 100), 10)
                screen.blit(jetons_persos[liste_joueurs[i-1].personnage], OP_POS)
                screen.blit(little_piece, (OP_POS[0] + JETON_SIZE[0] - 30, OP_POS[1] + JETON_SIZE[1] - 30))

                little_pieces = LITTLE_STATS_FONT.render(str(liste_joueurs[i-1].pieces), 1, (0,0,0))
                little_points = LITTLE_STATS_FONT.render(str(liste_joueurs[i-1].points), 1, (0,0,0))

                screen.blit(little_pieces, (OP_POS[0] + JETON_SIZE[0], OP_POS[1] + JETON_SIZE[1] - 10))
                screen.blit(little_points, (OP_POS[0] + JETON_SIZE[0], OP_POS[1]))

            i+=1

        pygame.display.flip()

def centrage_rect(surface, pos):
    return pos[0] + surface.get_size()[0]/2, pos[1] + surface.get_size()[1]/2'''