import pygame
import random
from Settings import *

BG_COLOR = (251,253,248)
liste_perso = [("Chuubei", "Chuubei le messager pioche une carte Rencontre lorsqu'il arrive dans chacun des trois Relais intermediaires", 4),
                      ("Hiroshige", "Hiroshige l'artiste prend une carte Panorama de son choix lorsqu'il arrive dans chacun des trois Relais intermediaires", 3), 
                      ("Hirotada", "A chaque arret au temple, Hirotada le pretre se verra beni d'une piece offerte gratuitement au temple.", 8), 
                      ("Kinko", "Les cartes repas achetees par Kinko le ronin lui coutent une piece de moins", 7), 
                      ("Mitsukuni", "Chaque carte Source Chaude et chaque carte Accomplissement rapporte un point summplementaire a Mitsukuni le vieillard", 6), 
                      ("Sasayakko", "Dans les villages, si Sasayakko la geisha achete au moins deux Souvenirs, le moins cher des deux lui est offert", 5), 
                      ("Satsuki", "Lors de son arrivee au Relais, Satsuki l'orpheline recoit aleatoirement et gratuitement pour une carte repas", 2), 
                      ("Umegae", "Umegae la saltimbanque gagne un point et une piece lors de chaque rencontre", 5), 
                      ("Yoshiyasu", "Lors de chaque rencontre, Yoshiyasu le fonctionnaire choisi une carte Rencontre parmi deux au choix", 9), 
                      ("Zen-Emon", "Zen-Emon le marchand peur acheter l'un des Souvenirs pour une seule piece au lieu du prix indique, une fois par Echoppe", 6)]



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
        self.cartes_source=[]
        self.pieces_donnees_temple=0
        self.pieces_depensees_repas=0
        self.case=0
        self.points=0
        self.achievements=[0,0,0,0,0,0,0,0]     #pano_mer, pano_montagne, pano_riziere, temples, repas, source chaude, rencontre, souvenir 
                                                #on remplace pas 1 si le mec a l'achievment.
    

    def avancer (self):
        self.case+=int(input('Combien de cases?'))

    def choix_perso(self, liste_perso_joueur):
        FPS = int(settings.setting["FPS"])
        self.liste_perso_joueur = liste_perso_joueur
        
        pygame.init()
        pygame.display.init()
        pygame.font.init()

        clock = pygame.time.Clock()

        liste_choix_perso = []
        for i in range (3) :
            perso_envisageable = liste_perso[random.randint(len(liste_perso)-1)]
            while perso_envisageable in self.liste_perso_joueurs or perso_envisageable in liste_choix_perso:
                perso_envisageable = liste_perso[random.randint(len(liste_perso)-1)]
            liste_choix_perso.append()



        screen = pygame.display.set_mode((0,0))
        screen_width, screen_height = screen.get_size()
        CENTERX = screen_width / 2
        CENTERY =  screen_height/2


        #self.perso = perso_choisi