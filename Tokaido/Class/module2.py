import pygame






















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
    return pos[0] + surface.get_size()[0]/2, pos[1] + surface.get_size()[1]/2