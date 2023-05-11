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

    def choix_perso(self):
