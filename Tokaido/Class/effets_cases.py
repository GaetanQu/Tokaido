import random
import Joueur


images_source_chaude=['liste chemins dacces', 'test']
images_objets_echoppe=[]

cases_doubles=[1,5,6,7,9,11,17,18,19,20,22,24,30,32,34,36,37,40,43,45,47,48,51,52]

#mer, montagne, riziere
pano_cases=[[11,15,24,34,39,46,52],[6,12,19,23,32,50],[4,18,28,35,51]]    
pano_cartes=[{},{},{}]

echoppe_cases=[1,8,25,29,40,45,53]
#sushi, kimono, statue, eventail
#A noter que les points dans le dico echoppe ne servent a rien
echoppe_cartes=[{},{},{},{}]                   

#Tu pars du principe que dico[nom_carte] = [points_rapportes, prix carte, chemin dacces]

source_cases=[5,13,22,33,42,48]
source_cartes= {'carte 2':[2, 0, images_source_chaude[0]], 'carte 3':[3, 0, images_source_chaude[1]]}           #{'Bureau/pygame/images/nom_image'[[3, 2]]}

rencontre_cases=[3,10,20,30,38,44,49]
rencontre_cartes={} 

relais_cases=[14,27,41]
relais_cartes={'nom_carte':['points_rapportes', 'prix_carte', 'chemin_dacces']}

temple_cases=[2,9,16,21,36,43] 

ferme_cases=[7,17,26,31,37,47]

achievments=[1,1,1,1,1,1,1,1]

#trop bg






def test_case(current_player):             
    if current_player.case in pano_cases[0]:
        return list(pano_cartes[0].keys())
    elif current_player.case in pano_cases[1]:
        return list(pano_cartes[1].keys())
    elif current_player.case in pano_cases[2]:
        return list(pano_cartes[2].keys())
    elif current_player.case in echoppe_cases:
        return list(echoppe_cartes[0].keys())+list(echoppe_cartes[1].keys())+list(echoppe_cartes[2].keys())+list(echoppe_cartes[3].keys())
    elif current_player.case in source_cases:
        return list(source_cartes.keys())
    elif current_player.case in rencontre_cases:
        return list(rencontre_cartes.keys())
    elif current_player.case in relais_cases:
        return list(relais_cartes.keys())
    else :
        return []

def effet_echoppe (current_player, shokunin=False):
    if shokunin==True:
        objet_shokunin=liste_cartes_case[random.randint(0, len(liste_cartes_case)-1)]
        cartes_choisies=[objet_shokunin]       
        #affichage de la carte tiree au sort
        carte_imposee(current_player, [objet_shokunin])
    else : 
        liste_cartes_case=test_case(current_player)
        #creation de la liste des cartes correspondant a la case
        possible_cards=cartes_a_proposer(3, liste_cartes_case)
        #il faudra aussi suppr les cartes choisies par le joueur de la liste generale
        cartes_choisies=choix(current_player, possible_cards)

    carte_moins_cher=cartes_choisies[0]
    for carte_choisie in cartes_choisies : 
    #determiner la carte qui sera gratuite
        if current_player.personnage=='Sasayakko' and shokunin==False and len(cartes_choisies)>=2:
            if carte_moins_cher.prix>carte_choisie.prix:    #a resoudre car metrode .prix nexiste pas
                carte_moins_cher=carte_choisie


        if carte_choisie in list(echoppe_cartes[0].keys()):
            annexe_echoppe (current_player, carte_choisie, 'sushi', 0, shokunin)

        elif carte_choisie in list(echoppe_cartes[1].keys()):
            annexe_echoppe (current_player, carte_choisie, 'kimono', 1, shokunin)

        elif carte_choisie in list(echoppe_cartes[2].keys()):
            annexe_echoppe (current_player, carte_choisie , 'statue', 2, shokunin)

        elif carte_choisie in list(echoppe_cartes[3].keys()):
            annexe_echoppe (current_player, carte_choisie, 'eventail', 3, shokunin)


def annexe_echoppe (current_player, carte_choisie, mot_cle, indice_cle, shokunin):
    if mot_cle in current_player.ordre_famille_echoppe:     #alors on va chercher le rang de sushi pr savoir le nb de points a attribuer
        for i in range(len(current_player.ordre_famille_echoppe)):  #ne pas oublier d'enlever des pieces
            if current_player.ordre_famille_echoppe[i]==mot_cle:
                current_player.points+=2*i+1
                current_player.pieces-=echoppe_cartes[indice_cle][carte_choisie][1]
    else : 
        current_player.ordre_famille_echoppe.append(mot_cle)
        current_player.points+=2*len(current_player.ordre_famille_echoppe)+1
    current_player.cartes_echoppe[indice_cle].append(carte_choisie)
    #on retire des pieces ssi cest pas le shokunin (rencontre) qui donne la carte
    if shokunin==False :
        current_player.pieces-=echoppe_cartes[indice_cle][carte_choisie][1]

    


#il faut ajouter le fait que si le joueur a deja toute une collection de pano, pas le droit de sarreter sur la case
def effet_panorama (current_player, mer=False, montagne=False, riziere=False): 
    #mer=false ect ne servent que dans le cas ou le joueur vient de rencontrer annaibito sur case rencontre
    if mer==True:
        liste_cartes_case=list(pano_cartes[0].keys())
    elif montagne==True:
        liste_cartes_case=list(pano_cartes[1].keys())
    elif riziere==True:
        liste_cartes_case=list(pano_cartes[2].keys())
    else:
        liste_cartes_case=test_case(current_player)

    if current_player.case in pano_cases[0] or mer==True:                                               #SI CASE = PANO MER
        indice=0
        while liste_cartes_case[indice] in current_player.cartes_pano[0] :
            indice+=1
            if indice == len(liste_cartes_case)-1:
                break
        if indice<len(liste_cartes_case)-1:                                     #on ajoute la carte pano ssi le current_player ne la pas encore
            current_player.cartes_pano[0].append(liste_cartes_case[indice])            #(car les cartes pano se recoivent dans lordre)
            current_player.points+=pano_cartes[0][liste_cartes_case[indice]][0]
        elif indice==len(liste_cartes_case)-1:
            achievments(current_player, 0)
    elif current_player.case in pano_cases[1] or montagne==True:                                             #SI CASE = PANO MONTAGNE
        indice=0
        while liste_cartes_case[indice] in current_player.cartes_pano[1] :
            indice+=1
            if indice == len(liste_cartes_case)-1:
                break
        if indice<len(liste_cartes_case)-1:                                     
            current_player.cartes_pano[1].append(liste_cartes_case[indice])            
            current_player.points+=pano_cartes[1][liste_cartes_case[indice]][0]   #[0] car les points sont stock�s en 1er rang dans le dico.
        elif indice==len(liste_cartes_case)-1:
            achievments(current_player, 0)
    elif current_player.case in pano_cases[2] or riziere==True:                                             #SI CASE = PANO RIZIERE
        indice=0
        while liste_cartes_case[indice] in current_player.cartes_pano[2] :
            indice+=1
            if indice == len(liste_cartes_case)-1:
                break
        if indice<len(liste_cartes_case)-1:                                     
            current_player.cartes_pano[2].append(liste_cartes_case[indice])            
            current_player.points+=pano_cartes[2][liste_cartes_case[indice]][0]
        elif indice==len(liste_cartes_case)-1:
            achievments(current_player, 0)
    #choix en fin de code ici car cest ces tests qui determineront la carte a append
    #choix sert ici juste a afficher nouvelle carte
    carte_imposee(current_player, [liste_cartes_case[indice]])
    

def effet_rencontre(current_player):
    liste_cartes_case=test_case(current_player)
    nouvelle_rencontre=cartes_a_proposer (1,  liste_cartes_case)
    current_player.cartes_rencontre.append(nouvelle_rencontre)
    carte_imposee(current_player, [nouvelle_rencontre])
    if nouvelle_rencontre=='Kuge':
        current_player.pieces+=3
    elif nouvelle_rencontre=='Samurai':
        current_player.points+=3
    elif nouvelle_rencontre=='Miko':
        current_player.points+=1
        current_player.pieces_donnees_temple+=1
    elif nouvelle_rencontre=='Shokunin':
        effet_echoppe(current_player, shokunin=True)
    elif nouvelle_rencontre=='Annaibito_mer':    #partie bien chiante
        effet_panorama (current_player, mer=True)
    elif nouvelle_rencontre=='Annaibito_montagne':
        effet_panorama (current_player, montagne=True)
    elif nouvelle_rencontre=='Annaibito_riziere':
        effet_panorama (current_player, riziere=True)
       
def effet_ferme (current_player):
    current_player.pieces+=3

#le joueur ne peut s'arreter que s'il a argent car DOIT donner 1, 2, ou 3 pièces.
def effet_temple (current_player):
    if current_player.personnage=='Hirotata':
        current_player.pieces_donnees_temple+=1
        current_player.points+=1
    money_given=int(input('Combien dargent donnez-vous?'))
    while money_given<1 or money_given>3 or money_given>current_player.pieces:
        money_given=int(input('Mauvais montant, reesayez : '))
    current_player.pieces-=money_given
    current_player.pieces_donnees_temple+=money_given

def effet_source_chaude (current_player):
    carte=random.randint(2,3)
    if current_player.personnage=='Mitsukuni':
        current_player.points+=1
    if carte==2:
        current_player.points+=2
        current_player.cartes_source.append('carte 2')
        carte_imposee(current_player, )
    elif carte==3:
        current_player.points+=3
        current_player.cartes_source_chaude.append('carte 3')

def effet_relais (current_player):
    liste_cartes_case=test_case(current_player.case)
    possible_cards=cartes_a_proposer(nbr_joueurs+1, liste_cartes_case, current_player)
    pass            #a finir


def effet (current_player):     
    if current_player.case in echoppe_cases:
        effet_echoppe (current_player)
    elif current_player.case in pano_cases[0]+pano_cases[1]+pano_cases[2]: 
        effet_panorama (current_player)

    elif current_player.case in rencontre_cases:
        effet_rencontre(current_player)

    elif current_player.case in ferme_cases:
        effet_ferme(current_player)

    elif current_player.case in temple_cases:
        effet_temple(current_player)

    elif current_player.case in source_cases:
        effet_source_chaude(current_player)

    elif current_player.case in relais_cases:
        effet_relais (current_player, nbr_joueurs)
        #galere car le tirage depend du nombre de joueurs









#constitution de la liste des cartes qu'on proposera au joueur selon le nbr de cartes a tirer
def cartes_a_proposer( nb_cartes_a_tirer, liste_cartes_case, current_player=None, Rencontre=False):
    possible_cards=[]                      
    for i in range (nb_cartes_a_tirer):
        indice_carte=random.randint(1,len(liste_cartes_case)-i-1)
        possible_cards.append(liste_cartes_case[indice_carte])              
        del(liste_cartes_case[indice_carte])
    return possible_cards


#simple test si lachievment est deja recupere    
def achievments ( current_player, indice_achievment):       
    if achievments[indice_achievment]==1:
        current_player.achievments[indice_achievment]=1
        achievments[indice_achievment]=0  
        if current_player.personnage=='Mitsukuni':
            current_player.points+=1



def choix (current_player, possible_cards):             #PYGAME!!!! cette fonction doit me return une liste comportant la ou 

    while 'le joueur ne clique pas sur valider'==True:  #les cartes choisies par le joueur (même si la carte est imposee)
        if 'le joueur clique sur carte'==True:          #Je lappelle regulierement simplement pour montrer au joueur 
            pass                                        #la carte qu'il a obtenue, ce nest pas tjrs un choix a proprement parler



#carte_imposee ici n'est pas une liste, on veut juste 'nom_carte'
#la fonction ne doit rien renvoyer, ni append, juste montrer au joueur sa nouvelle carte.
def carte_imposee (current_player, carte_imposee):
    pass