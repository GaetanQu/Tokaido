"""
Voici le code initial du programme.
On y lancera d'abord l'authentificateur, puis un menu permettant de jouer et d'afficher ses statistiques.
On pourra egalement comparer ces dernieres avec celles des autres utilisatteurs enregistres.
"""

"""
A la base on voulait faire un truc propre, digne de professionnels
Puis on s'est rappeles qu'on etait en prepa
"""

#Importation de tous les modules et classes nécessaires au bon fonctionnement du programme
import Class.Authenticator
import Class.Menu #<- ca arrive que le fichier se renomme en "menu.py", sans doute a cause de Git, il faut le renommer en "Menu.py"
import Class.Play_split
import Class.Joueur
import PySimpleGUI as sg

#Creation du plateau
case = []
for i in range (54):
    case.append(i)

#En premier lieu, l'utilisateur doit s'identifier
players_list = []

account = Class.Authenticator.auth()
players_list.append(account)

menu_event = ""

while menu_event != "Quit" :

    if account[0] != "Closed":
        menu = Class.Menu.Menu(players_list)
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
        joueur = []
        for player in players_list:
            joueur.append(Class.Joueur.Joueur(player[0]))

            for element in joueur :
                element.choix_perso()