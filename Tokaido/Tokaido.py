"""
Voici le code initial du programme.
On y lancera d'abord l'authentificateur, puis un menu permettant de jouer et d'afficher ses statistiques.
On pourra egalement comparer ces dernieres avec celles des autres utilisatteurs enregistres.
"""

#Importation de tous les modules et classes nécessaires au bon fonctionnement du programme
import Class.Authenticator
import Class.Menu1

#Creation du plateau
case = []
for i in range (54):
    case.append(i)
    0
#En premier lieu, l'utilisateur doit s'identifier
player = []

account = Class.Authenticator.auth()
player.append(account)

menu_event = ""

while menu_event != "quit" :

    if account[0] != "Closed":
        menu = Class.Menu1.Menu(account)
        menu_event = menu.launch()

    elif account[0] == "Closed":
        break

    if menu_event == "deconnexion":
        account = Class.Authenticator.auth()

