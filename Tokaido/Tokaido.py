"""
Voici le code initial du programme.
On y lancera d'abord l'authentificateur, puis un menu permettant de jouer et d'afficher ses statistiques.
On pourra egalement comparer ces dernieres avec celles des autres utilisatteurs enregistres.
"""

#Importation de tous les modules et classes nécessaires au bon fonctionnement du programme
import Class.Authenticator
import Class.Menu

#Creation du plateau
case = []
for i in range (54):
    case.append(i)
    0
#En premier lieu, l'utilisateur doit s'identifier

player = Class.Authenticator.auth()

if player != "Closed":
    menu = Class.Menu.Menu(player)
    menu.launch()