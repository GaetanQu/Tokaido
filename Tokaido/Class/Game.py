import pygame
import Class.effets_cases
import random
import Class.affichage_plateau
import Class.Inventaire

JETON_SIZE = (150,150)
POINTS_WIDTH = 400

HUD_COLOR = (141, 147, 190)
BG_COLOR = (251, 253, 248)

pygame.font.init()

UIuprect = pygame.Rect((0,150), (1920, 1080 - 300))
UIdownrect = pygame.Rect((0,1080-150), (1920, 150))

JAPON = "Tokaido/Fonts/Japon.ttf"
MAIN_PLAYER_FONT = pygame.font.Font(JAPON, 50)
CURRENT_STATS_FONT = pygame.font.Font(JAPON, 60)
LITTLE_STATS_FONT = pygame.font.Font(JAPON, 30)

images_cases = {"mer":pygame.image.load("Tokaido/Class/images/cases/panorama_mer.png"),
                "relais":pygame.image.load("Tokaido/Class/images/cases/relais.png")}

jetons_persos = {"Chuubei" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/chuubei.png"), JETON_SIZE),
                 "Hiroshige" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/hiroshige.png"), JETON_SIZE),
                 "Hirotada" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/hirotada.png"), JETON_SIZE),
                 "Kinko" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/kinko.png"), JETON_SIZE),
                 "Mitsukuni" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/mitsukuni.png"), JETON_SIZE),
                 "Sasayakko" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/sasayakko.png"), JETON_SIZE),
                 "Satsuki" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/satsuki.png"), JETON_SIZE),
                 "Umegae" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/umegae.png"), JETON_SIZE),
                 "Yoshiyasu" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/yoshiyasu.png"), JETON_SIZE),
                 "Zen-Emon" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/jetons/zen-emon.png"), JETON_SIZE)}

piece = pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/HUD/piece.png"), (100,100))
little_piece = pygame.transform.smoothscale(piece, (30,30))


cards_viewer = pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/HUD/cards_viewer.png"), (100,100))
hovered_cards_viewer = pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/HUD/hovered_cards_viewer.png"), (100,100))

cards_viewers_rect = cards_viewer.get_rect()

def launch(screen, liste_joueurs):
    pygame.display.set_caption("Tokaido")
    for relais in range (4):
        liste_cartes_relais=[]
        while Class.effets_cases.everyone_in_relais (liste_joueurs)==False :
            liste_joueurs = ordre(liste_joueurs)
            current_player=liste_joueurs[0]
            Class.affichage_plateau.launch(screen, liste_joueurs[0], liste_joueurs)
            Class.effets_cases.effet (current_player, liste_joueurs, screen)
            if Class.effets_cases.someone_in_relais (current_player)==True : 
                liste_cartes_relais=Class.effets_cases.effet(current_player, liste_joueurs, liste_cartes_relais_restantes=liste_cartes_relais)
            else:
                Class.effets_cases.effet (current_player, liste_joueurs)



def jouer_tour (liste_joueurs):
    liste_joueurs = ordre(liste_joueurs)
    Class.effets_cases.effet(liste_joueurs[0], liste_joueurs)

def ordre (liste_joueurs):
    liste_joueurs.sort(key=lambda x: x.case)
    return liste_joueurs

def affichage_HUD(screen, liste_joueurs):
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

    if len(liste_pseudo_joueurs) < 5:
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

    

    if main_player_rect.collidepoint(pygame.mouse.get_pos()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        

    pygame.display.flip()

def centrage_rect(surface, pos):
    return pos[0] + surface.get_size()[0]/2, pos[1] + surface.get_size()[1]/2

def tour(screen, liste_joueurs, relais, is_generated = False):
    
    if is_generated == False :
        cases_liste = []
        for i in range(0,54):
            cases_liste.append(i)
        liste_cases_pos = []
        liste_cases_rect = []
    i = 0
    screen.fill(BG_COLOR)
    for case in cases_liste:
        if case <= relais:
            case_pos = (100*i + 100, 1080/2) #random.randint(250, screen.get_height()-250)
            liste_cases_pos.append(case_pos)
            screen.blit(images_cases["mer"], liste_cases_pos[i])
            liste_cases_rect.append(images_cases["mer"].get_rect())
            centrage_rect(images_cases["mer"], case_pos)
            for joueur in liste_joueurs:
                if joueur.case == case and joueur.pion != None:
                    screen.blit(pygame.transform.smoothscale(joueur.pion, (100,100)), (liste_cases_pos[i][0], liste_cases_pos[i][1] - 125))
            i+=1
    pygame.display.update((0,200),(screen.get_width(), screen.get_height()-200))
    case = choix_case(screen, liste_joueurs, cases_liste, liste_cases_rect, liste_cases_pos)
    return case

def choix_case(screen, liste_joueurs, liste_case, liste_cases_rect, liste_cases_pos):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            i = 0
            for case_rect in liste_cases_rect:
                if case_rect.collidpoint(pygame.mouse.get_pos()):
                    if liste_case[i] not in liste_joueurs.case:
                        return liste_case[i]
                else:
                    i+=1
    for case_rect in liste_cases_rect:
        if case_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(images_cases["relais"], liste_cases_pos[i])
    pygame.display.update((0,200),(screen.get_width(), screen.get_height()-200))
    return None