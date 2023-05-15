import pygame
import Class.effets_cases
JETON_SIZE = (150,150)
HUD_COLOR = (141, 147, 190)


jetons_persos = {"Chuubei" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/chuubei.png"), JETON_SIZE),
                 "Hiroshige" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/hiroshige.png"), JETON_SIZE),
                 "Hirotada" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/hirotada.png"), JETON_SIZE),
                 "Kinko" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/kinko.png"), JETON_SIZE),
                 "Mitsukuni" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/mitsukuni.png"), JETON_SIZE),
                 "Sasayakko" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/sasayakko.png"), JETON_SIZE),
                 "Satsuki" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/satsuki.png"), JETON_SIZE),
                 "Umegae" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/umegae.png"), JETON_SIZE),
                 "Yoshiyasu" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/yoshiyasu.png"), JETON_SIZE),
                 "Zen-emon" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/zen-emon.png"), JETON_SIZE)}

def launch(screen, liste_joueurs):
    pygame.display.set_caption("Tokaido")
    #affichage_HUD(screen, liste_joueurs)

    for relais in range (4):
        #while a modif car la le dernier joueur qui arrive ne prend pas sa carte, en gros tous les joueurs qui arrivent au relais mangent sauf le dernier car on sort du while
         while Class.effets_cases.everyone_in_relais (liste_joueurs)==False :
             liste_joueurs=ordre(liste_joueurs)
            #etape du choix de la case a caler
             Class.effets_cases.effet(liste_joueurs[0], liste_joueurs)
         liste_cartes_relais=Class.effet_cases.effet(liste_joueurs[0])
         for joueur in liste_joueurs : 
             liste


def jouer_tour (liste_joueurs):
    liste_joueurs = ordre(liste_joueurs)
    Class.effets_cases.effet(liste_joueurs[0], liste_joueurs)

def ordre (liste_joueurs):
    liste_joueurs.sort(key=lambda x: x.case)
    return liste_joueurs

def affichage_plateau():
    pass

def affichage_HUD(screen, liste_joueurs):
    PLAYER_SUFRACE_HEIGHT = 150
    MAIN_PLAYER_TEXT = liste_joueurs[0].nom
    NEXT_PLAYER_TEXT = liste_joueurs[1].nom

    dico_perso_joueurs = {}
    for joueur in liste_joueurs:
        dico_perso_joueurs[joueur.nom] = joueur.personnage

    MAIN_PLAYER_POS = (0,screen.get_size()[1] - PLAYER_SUFRACE_HEIGHT)
    OTHER_PLAYERS_POS = (0,0)
    
    main_player_surface = pygame.Surface((screen.get_size()[0], PLAYER_SUFRACE_HEIGHT))
    other_players_surface = pygame.Surface((screen.get_size()[0], PLAYER_SUFRACE_HEIGHT))

    main_player_surface.fill(HUD_COLOR)
    main_player_surface.set_alpha(100)

    other_players_surface.fill(HUD_COLOR)
    other_players_surface.set_alpha(150)

    screen.blit(main_player_surface, MAIN_PLAYER_POS)
    screen.blit(other_players_surface, OTHER_PLAYERS_POS)
    screen.blit(jetons_persos[liste_joueurs[0].personnage], (int(0.5 * JETON_SIZE[0]),MAIN_PLAYER_POS[1] - 0.5 * JETON_SIZE[1]/2))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()