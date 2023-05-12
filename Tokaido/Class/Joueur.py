import pygame
import random
import Class.Settings

BG_COLOR = (251,253,248)

#perso = [nom : [desc, image, pieces]]

dico_perso = { "Chuubei" : ["Chuubei le messager pioche une carte Rencontre lorsqu'il arrive dans chacun des trois Relais intermediaires", pygame.image.load("Tokaido/Class/images/personnages/chuubei.png"), 4],
               "Hiroshige" : ["Hiroshige l'artiste prend une carte Panorama de son choix lorsqu'il arrive dans chacun des trois Relais intermediaires", pygame.image.load("Tokaido/Class/images/personnages/hiroshige.png"), 3], 
               "Hirotada" : ["A chaque arret au temple, Hirotada le pretre se verra beni d'une piece offerte gratuitement au temple.", pygame.image.load("Tokaido/Class/images/personnages/hirotada.png"), 8], 
               "Kinko" : ["Les cartes repas achetees par Kinko le ronin lui coutent une piece de moins", pygame.image.load("Tokaido/Class/images/personnages/kinko.png"), 7], 
               "Mitsukuni" : ["Chaque carte Source Chaude et chaque carte Accomplissement rapporte un point summplementaire a Mitsukuni le vieillard", pygame.image.load("Tokaido/Class/images/personnages/mitsukuni.png"), 6], 
               "Sasayakko" : ["Dans les villages, si Sasayakko la geisha achete au moins deux Souvenirs, le moins cher des deux lui est offert", pygame.image.load("Tokaido/Class/images/personnages/sasayakko.png"), 5], 
               "Satsuki" : ["Lors de son arrivee au Relais, Satsuki l'orpheline recoit aleatoirement et gratuitement pour une carte repas", pygame.image.load("Tokaido/Class/images/personnages/satsuki.png"), 2], 
               "Umegae" : ["Umegae la saltimbanque gagne un point et une piece lors de chaque rencontre", pygame.image.load("Tokaido/Class/images/personnages/umegae.png"), 5], 
               "Yoshiyasu" : ["Lors de chaque rencontre, Yoshiyasu le fonctionnaire choisi une carte Rencontre parmi deux au choix", pygame.image.load("Tokaido/Class/images/personnages/yoshiyasu.png"), 9], 
               "Zen-Emon" : ["Zen-Emon le marchand peur acheter l'un des Souvenirs pour une seule piece au lieu du prix indique, une fois par Echoppe", pygame.image.load("Tokaido/Class/images/personnages/zen-emon.png"), 6]}

liste_perso = list(dico_perso.keys())

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.couleur=None
        self.personnage=None
        self.pieces=0
        self.cartes_pano=[[],[],[]]             #mer, montagne, riziere
        self.cartes_repas=[]
        self.cartes_echoppe=[[],[],[],[]]        #4 familles de cartes, faudrait les mettre dans l'ordre 
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

    def choix_perso(self, liste_joueurs):
        #FPS = int(Settings.settings.setting["FPS"])
        self.liste_joueurs = liste_joueurs
        
        liste_perso_joueurs = []
        for joueur in liste_joueurs :
            liste_perso_joueurs.append(joueur.personnage)

        pygame.init()
        pygame.display.init()
        pygame.font.init()

        clock = pygame.time.Clock()

        liste_choix_perso = []
        for i in range (3) :
            perso_envisageable = dico_perso[liste_perso[random.randint(0,len(liste_perso)-1)]]
            while perso_envisageable in liste_perso_joueurs or perso_envisageable in liste_choix_perso:
                perso_envisageable = dico_perso[liste_perso[random.randint(0,len(liste_perso)-1)]]
            liste_choix_perso.append(perso_envisageable)

        screen = pygame.display.set_mode((0,0))
        screen_width, screen_height = screen.get_size()
        CENTERX = screen_width / 2
        CENTERY =  screen_height/2
        card_1 = liste_choix_perso[0]
        card_2 = liste_choix_perso[1]
        card_3 = liste_choix_perso[2]

        perso_choisi = None
        while perso_choisi == None :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pass

    def choix_couleur(self) :



        couleur = input(print("Choisissez une couleur"))
        self.couleur == couleur