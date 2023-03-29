"""
Voici le code principal du programme. C'est ici que seront exécutées les fonctions créées dans les différents fichiers.
"""

#Importation de tous les modules et classes nécessaires au bon fonctionnement du programme
import Class.Authenticator
import pygame

#Creation du plateau
case = []
for i in range (54):
    case.append(i)

#En premier lieu, l'utilisateur doit s'identifier
Class.Authenticator.auth()

