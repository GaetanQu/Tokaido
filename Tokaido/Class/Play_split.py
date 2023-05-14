import pygame

jetons_persos = {"Chuubei" : pygame.image.load("Tokaido/Class/images/personnages/jetons/chuubei.png"),
                 "Hiroshige" : pygame.image.load("Tokaido/Class/images/personnages/jetons/hiroshige.png"),
                 "Hirotada" : pygame.image.load("Tokaido/Class/images/personnages/jetons/hirotada.png"),
                 "Kinko" : pygame.image.load("Tokaido/Class/images/personnages/jetons/kinko.png"),
                 "Mitsukuni" : pygame.image.load("Tokaido/Class/images/personnages/jetons/mitsukuni.png"),
                 "Sasayakko" : pygame.image.load("Tokaido/Class/images/personnages/jetons/sasayakko.png"),
                 "Satsuki" : pygame.image.load("Tokaido/Class/images/personnages/jetons/satsuki.png"),
                 "Umegae" : pygame.image.load("Tokaido/Class/images/personnages/jetons/umegae.png"),
                 "Yoshiyasu" : pygame.image.load("Tokaido/Class/images/personnages/jetons/yoshiyasu.png"),
                 "Zen-emon" : pygame.image.load("Tokaido/Class/images/personnages/jetons/zen-emon.png"),}

def launch(screen, liste_joueurs):
    pygame.display.set_caption("Tokaido")
    affichage_HUD(screen, liste_joueurs)

def jouer_tour (liste_joueurs):
    liste_joueurs = ordre(liste_joueurs)
    pass

def ordre (liste_joueurs):
    liste_joueurs.sort(key=lambda x: x.case)
    return liste_joueurs

def affichage_plateau():
    pass

def affichage_HUD(screen, liste_joueurs):
    PLAYER_SUFRACE_HEIGHT = 75
    MAIN_PLAYER_TEXT = liste_joueurs[0].nom
    NEXT_PLAYER_TEXT = liste_joueurs[1].nom

    main_player_surface = pygame.Rect((0,screen.get_size()[1] - PLAYER_SUFRACE_HEIGHT),(screen.get_size()[0], PLAYER_SUFRACE_HEIGHT))
    other_players_surface = pygame.Rect((0,0), (screen.get_size()[0], PLAYER_SUFRACE_HEIGHT))

    screen.blit(jetons_persos[liste_joueurs[0].personnage], (0,0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()