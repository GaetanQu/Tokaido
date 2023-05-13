import pygame

def launch(screen):
    pygame.display.set_caption("Tokaido")

def jouer_tour (liste_joueurs):
    joueur = au_tour_de(liste_joueurs)

def au_tour_de (liste_joueurs):
    dernier=liste_joueurs[0]
    for joueur in liste_joueurs:
        if joueur.case<dernier.case:
            dernier=joueur
    return dernier

def affichage_plateau():
    pass