from Class.Auth import Auth
import pygame

"""Creation du plateau"""
case = []
for i in range (54):
    case.append(i)

id_mdp = {}
id_mdp["anateg"] = "20020417"
id_mdp[" rzejnkqfn bjidlsb qkchjsgqvjklhfkjgvns"] = "eusihferiduvqhfiuogdsohnijolbhns"


"""Authentification en mode console (retirer les input pour adapter en pygame)"""

userid = input("id : ").lower()
while userid not in id_mdp :
    userid = input("Cet utilisateur n'est pas enregistre\nSaisissez-en un autre : ").lower()

mdp = input("mdp : ")
while Auth.verif(userid, mdp, id_mdp) != 0 :
    mdp = input("Mot de passe incorrect\nSaissiez un autre mot de passe : ")