class Joueur:
    def __init__(self, couleur, personnage):
        self.couleur=couleur
        self.personnage=personnage
        self.pieces=personnage.pieces
        self.cartes_pano=[[],[],[]]    #mer, montagne, riziere
        self.cartes_repas=[]
        self.cartes_echoppe[[],[],[],[]]   #4 familles de cartes, faudrait les mettre dans l'ordre 
        self.pieces_donnees_temple=0
        self.pieces_depensees_repas=0
        self.case=0
        self.points=0
    

