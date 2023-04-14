class Joueur:
    def __init__(self, couleur, personnage):
        self.couleur=couleur
        self.personnage=personnage
        self.pieces=personnage.pieces
        self.cartes_pano=[[],[],[]]             #mer, montagne, riziere
        self.cartes_repas=[]
        self.cartes_echoppe[[],[],[],[]]        #4 familles de cartes, faudrait les mettre dans l'ordre 
        self.pieces_donnees_temple=0
        self.pieces_depensees_repas=0
        self.case=0
        self.points=0
        self.achievements=[0,0,0,0,0,0,0,0]     #pano_montagne, pano_rizière, temples, repas, source chaude, rencontre, souvenir 
                                                #on remplace pas 1 si le mec a l'achievment.
    

