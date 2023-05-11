import pygame
import random

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.couleur=None
        self.personnage=None
        self.pieces=0
        self.cartes_pano=[[],[],[]]             #mer, montagne, riziere
        self.cartes_repas=[]
        self.cartes_echoppe[[],[],[],[]]        #4 familles de cartes, faudrait les mettre dans l'ordre 
        self.ordre_famille_echoppe=[]           #car l'ordre dans lequel le joueur prend les cartes est important. liste prendra en paramètre sushi, kimono, statue, eventail.
        self.pieces_donnees_temple=0
        self.pieces_depensees_repas=0
        self.case=0
        self.points=0
        self.achievements=[0,0,0,0,0,0,0,0]     #pano_mer, pano_montagne, pano_rizi�re, temples, repas, source chaude, rencontre, souvenir 
                                                #on remplace pas 1 si le mec a l'achievment.
    

    def avancer (self):
        self.case+=int(input('Combien de cases?'))

    def choix_perso(self, liste_perso_joueur):
        self.liste_perso_joueur = liste_perso_joueur
        pygame.init()

        liste_choix_perso = []
        liste_perso = [("Chuubei", 4), ("Hiroshige", 3), ("Hirotada", 8), ("Kinko", 7), ("Mitsukuni", 6), ("Sasayakko", 5), ("Satsuki", 2), ("Umegae", 5), ("Yoshiyasu", 9), ("Zen-Emon", 6)]

        for i in range (3) :
            perso_envisageable = liste_perso[random.randint(len(liste_perso)-1)]
            while perso_envisageable in self.liste_perso_joueurs:
                perso_envisageable = liste_perso[random.randint(len(liste_perso)-1)]

            liste_choix_perso.append()



        #self.perso = perso_choisi