import Random

class Cartes :
    def __init__(self):
        self.pano_cases=[[11,15,24,34,39,46,52],[6,12,19,23,32,50],[4,18,28,35,51]]    #mer, montagne, riziere
        self.pano_cartes=[{},{},{}]         #oblige de faire une liste de dictionnaires pour uniformiser, sinon une des methodes fonctionnera pas

        self.echoppe_cases=[1,8,25,29,40,45,53]
        self.echoppe_cartes=[{},{},{},{}]

        #Tu pars du principe que dico[emplacement] = [points_rapportes, prix cartes]

        self.source_cases=[5,13,22,33,42,48]
        self.source_cartes={'emplacement':['points_rapportes', 'prix_carte']}            #{'Bureau/pygame/images/nom_image'[[3, 2]]}

        self.rencontre_cases=[3,10,20,30,38,44,49]
        self.rencontre_cartes={}

        self.relais_cases=[14,27,41]  
        self.relais_cartes={}  

        self.temple_cases=[2,9,16,21,36,43]

        self.ferme_cases=[7,17,26,31,37,47]


        #trop bg
        
    
    def test_case(self, joueur):             
        if joueur.case in self.pano_cases[1]:
            return self.pano_cartes[1].keys()
        elif joueur.case in self.pano_cases[2]:
            return self.pano_cartes[2].keys()
        elif joueur.case in self.pano_cases[3]:
            return self.pano_cartes[3].keys()
        elif joueur.case in self.echoppe_cases:
            return self.echoppe_cartes[1].keys()+self.echoppe_cartes[2].keys()+self.echoppe_cartes[3].keys()+self.echoppe_cartes[4].keys()
        elif joueur.case in self.source_cases:
            return self.source_cartes.keys()
        elif joueur.case in self.rencontre_cases:
            return self.rencontre_cartes.keys()
        elif joueur.case in self.relais_cases:    
            return self.relais_cartes.keys()



    def carte_random(self, nb_cartes_a_tirer, nb_cartes_a_choisir, liste_cartes_possibles, liste_cartes_du_joueur):
        cartes_a_proposer=[]                                                            #liste des cartes qui seront proposees au joueur                       
        for i in range (nb_cartes_a_tirer):                                             #constitution de la liste des cartes � proposer
            indice_carte=Random.randint(1,len(liste_cartes_possibles))
            cartes_a_proposer.append(liste_cartes_possibles[indice_carte])              #il faudra ajouter la partie pygame en prenant en compte le nombre de cartes a tirer
        for i in range (nb_cartes_a_choisir):
            if 'le joueur clique sur la carte'==True:
                liste_cartes_du_joueur.append('carte a ajt')  
            elif 'le joueur clique sur valider'==True:   #car dans lechoppe le joueur peut choisir plusieurs cartes
                return liste_cartes_du_joueur
        return liste_cartes_du_joueur




    def tirage(self, joueur): 

        liste_cartes_possibles=self.test_case(joueur)                                   #afin de ne pas editer la liste initiale 
            
        if joueur.case in self.pano_cases[0]:                                           #SI CASE = PANO MER
            indice=0
            while liste_cartes_possibles[indice] in joueur.cartes_pano[0] :
                indice+=1
            if indice<=len(liste_cartes_possibles):                                     #on ajoute la carte pano ssi le joueur ne la pas encore
                joueur.cartes_pano[0].append(liste_cartes_possibles[indice])            #(car les cartes pano se recoivent dans lordre)
                joueur.points+=self.pano_cartes[0][liste_cartes_possibles[indice]][0]


        elif joueur.case in self.pano_cases[1]:                                         #SI CASE = PANO MONTAGNE
            indice=0
            while liste_cartes_possibles[indice] in joueur.cartes_pano[1] :
                indice+=1
            if indice<=len(liste_cartes_possibles):                                     
                joueur.cartes_pano[1].append(liste_cartes_possibles[indice])            
                joueur.points+=self.pano_cartes[1][liste_cartes_possibles[indice]][0]   #[0] car les points sont stock�s en 1er rang dans le dico.


        elif joueur.case in self.pano_cases[2]:
            indice=0
            while liste_cartes_possibles[indice] in joueur.cartes_pano[2] :
                indice+=1
            if indice<=len(liste_cartes_possibles):                                     
                joueur.cartes_pano[2].append(liste_cartes_possibles[indice])            
                joueur.points+=self.pano_cartes[2][liste_cartes_possibles[indice]][0]



        elif joueur.case in self.echoppe_cases :    #CAS PARTICULIER : dans lechoppe, on ne doit pas proposer a un joueur une carte quil a deja        
            i=0
            for carte in liste_cartes_possibles:    
                if carte in joueur.cartes_echoppe:
                    del(liste_cartes_possibles[i])
                i+=1                     
            joueur.cartes_echoppe=self.carte_random (3,liste_cartes_possibles, joueur.cartes_echoppe)
            return 


        elif joueur.case in self.rencontre_cases:
            i=0
            for carte in liste_cartes_possibles:    
                if carte in joueur.cartes_rencontre:
                    del(liste_cartes_possibles[i])
                i+=1   
                
