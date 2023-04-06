import Random

class Cartes :
    def __init__(self):
        self.pano_cases=[[11,15,24,34,39,46,52],[6,12,19,23,32,50],[4,18,28,35,51]]    #mer, montagne, riziere
        self.pano_cartes=[[],[],[]]

        self.echoppe_cases=[1,8,25,29,40,45,53]
        self.echoppe_cartes[{},{},{},{}]

        self.source_cases=[5,13,22,33,42,48]
        self.source_cartes={emplacement[points_rapportes]}

        self.rencontre_cases=[3,10,20,30,38,44,49]
        self.rencontre_cartes={}

        self.relais_cases=[14,27,41]  
        self.relais_cartes={}  

        self.temple_cases=[2,9,16,21,36,43]

        self.ferme_cases=[7,17,26,31,37,47]
    
    def test_case(self, joueur):
        if joueur.case in pano_cases[1]:
            return self.pano_cartes[1]
        elif joueur.case in pano_cases[2]:
            return self.pano_cartes[2]
        elif joueur.case in pano_cases[3]:
            return self.pano_cartes[3]
        elif joueur.case in echoppe_cases:
            return echoppe_cartes[1].keys()+echoppe_cartes[2].keys()+echoppe_cartes[3].keys()+echoppe_cartes[4].keys()
        elif joueur.case in source_cases:
            return source_cartes.keys()
        elif joueur.case in rencontre_cases:
            return rencontre_cartes.keys()
        elif joueur.case in relais_cases:    
            return relais_cartes.keys()

    def tirage(self, nb_cartes_a_tirer, emplacement_cartes, joueur):  #pour ne pas avoir 2x la meme case        
        liste_cartes=emplacement_cartes.keys()
        if joueur.case in self.echoppe_cases :    #on ne doit pas proposer a un joueur une carte quil a deja dans lechoppe
            
            i=0
            for carte in liste_cartes:
                if carte==joueur.cartes_echoppe:
                    liste_cartes.del(i)
                i+=1

        cartes_a_proposer=[]
        for i in range (nb_cartes_a_tirer):
            carte=random.randint(1,len(liste_cartes))
            cartes_a_proposer.append(carte)
            
if joueur.case in self.echoppe_cases :