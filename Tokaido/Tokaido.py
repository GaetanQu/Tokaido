"""
Voici le code initial du programme.
On y lancera d'abord l'authentificateur, puis un menu permettant de jouer et d'afficher ses statistiques.
On pourra egalement comparer ces dernieres avec celles des autres utilisatteurs enregistres.
"""

"""
A la base on voulait faire un truc propre, digne de professionnels
Puis on s'est rappeles qu'on etait en prepa
C'est pas le cas de Jules et Martin apparemment
"""


###############################################################################
#                                                                             #
#                          IL FAUT JOUER EN 1080P !!!                         #
#                             (sinon c'est moche)                             #
#                                                                             #
###############################################################################




#Importation de tous les modules et classes nécessaires au bon fonctionnement du programme
import Class.Authenticator
import Class.menu
import Class.Game
import Class.Joueur
import PySimpleGUI as sg
import pygame

pygame.init()
pygame.display.init()
pygame.font.init()

#En premier lieu, l'utilisateur doit s'identifier
players_list = []

account = Class.Authenticator.auth()
players_list.append(account)
screen = pygame.display.set_mode((0,0))


menu_event = None

while menu_event != "Quit" :
    if account[0] != "Closed":
        menu = Class.menu.Menu(players_list, screen)
        menu_event = menu.launch()

    elif account[0] == "Closed":
        break

    if menu_event == "Deconnexion":
        account = Class.Authenticator.auth()
        players_list = []
        players_list.append(account)
        menu_event = None

    elif menu_event == "Solo":
        sg.Popup("Coming Soon")

    elif menu_event[0] == "Split":
        players_list = menu_event[1]
        liste_joueurs = []

        i = 0
        for player in players_list:
            i+=1
            joueur = Class.Joueur.Joueur(player[0], screen)
            liste_joueurs.append(joueur)
            joueur.choix_couleur(liste_joueurs)
            joueur.choix_perso(liste_joueurs)

        while i < 5:
            liste_joueurs.append(Class.Joueur.Joueur(None, screen))
            liste_joueurs[i].case = 99 #<- necessaire pour que les objets joueurs inexistants (joueur.nom = None) ne genent pas lors du tri de la liste pour l'ordre de passage
            i+=1

        Class.Game.launch(screen, liste_joueurs)