import Joueurs
import Cases


def au_tour_de (liste_des_joueurs):
    dernier=liste_des_joueurs[0]
    for joueur in liste_des_joueurs:
        if joueur.case<dernier.case:
            dernier=joueur
    return dernier


cases=Cases()

def jeu (liste_des_joueurs):
    #chaque tour de boucle rpz le tour d'1 joueur
    while True:
        joueur=au_tour_de(liste_des_joueurs)



