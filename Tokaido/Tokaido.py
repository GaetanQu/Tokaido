"""
Voici le code initial du programme.
On y lancera d'abord l'authentificateur, puis un menu permettant de jouer et d'afficher ses statistiques.
On pourra egalement comparer ces dernieres avec celles des autres utilisatteurs enregistres.
"""

#Importation de tous les modules et classes nécessaires au bon fonctionnement du programme
import Class.Authenticator
import Class.menu

#Creation du plateau
case = []
for i in range (54):
    case.append(i)

#En premier lieu, l'utilisateur doit s'identifier
if Class.Authenticator.auth() :
    Class.menu.Menu_()