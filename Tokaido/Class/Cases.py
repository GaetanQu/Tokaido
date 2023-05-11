import random
import Class.Joueur


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
source_cartes= {'carte 2':[2, 0, 'images.cartes_source_chaude.2'], 'carte 3':[3, 0, 'images.cartes_source_chaude.3']}           #{'Bureau/pygame/images/nom_image'[[3, 2]]}

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
    elif current_player.case in relais_cases
        return list(relais_cartes.keys())
    else :
        return []

def effet_echoppe (current_player, shokunin=False):
    if shokunin==True:
        objet_shokunin=liste_cartes_case[random.randint(0, len(liste_cartes_case)-1)]
        cartes_choisies=[objet_shokunin]       
        choix(current_player, [objet_shokunin])
    else : 
        liste_cartes_case=test_case(current_player)
        possible_cards=cartes_a_proposer(3, liste_cartes_case, current_player)
        #il faudra aussi suppr les cartes choisies par le joueur de la liste generale
        cartes_choisies=choix(current_player, possible_cards)           

    for carte_choisie in cartes_choisies : 
        if carte_choisie in list(echoppe_cartes[0].keys()):
            if 'sushi' in current_player.ordre_famille_echoppe:     #alors on va chercher le rang de sushi pr savoir le nb de points a attribuer
                for i in range(len(current_player.ordre_famille_echoppe)):  #ne pas oublier d'enlever des pieces
                    if current_player.ordre_famille_echoppe[i]=='sushi':
                        current_player.points+=2*i+1
            else : 
                current_player.ordre_famille_echoppe.append('sushi')
                current_player.points+=2*len(current_player.ordre_famille_echoppe)+1
            current_player.pieces-=echoppe_cartes[0][carte_choisie][1]
            current_player.cartes_echoppe[0].append(carte_choisie)
        elif carte_choisie in list(echoppe_cartes[1].keys()):
            if 'kimono' in current_player.ordre_famille_echoppe:     
                for i in range(len(current_player.ordre_famille_echoppe)):
                    if current_player.ordre_famille_echoppe[i]=='kimono':
                        current_player.points+=2*i+1
                        current_player.pieces-=echoppe_cartes[1][carte_choisie][1]
            else : 
                current_player.ordre_famille_echoppe.append('kimono')
                current_player.points+=2*len(current_player.ordre_famille_echoppe)+1
            current_player.pieces-=echoppe_cartes[1][carte_choisie][1]
            current_player.cartes_echoppe[1].append(carte_choisie)
        elif carte_choisie in list(echoppe_cartes[2].keys()):
            if 'statue' in current_player.ordre_famille_echoppe:     
                for i in range(len(current_player.ordre_famille_echoppe)):
                    if current_player.ordre_famille_echoppe[i]=='statue':
                        current_player.points+=2*i+1
            else : 
                current_player.ordre_famille_echoppe.append('statue')
                current_player.points+=2*len(current_player.ordre_famille_echoppe)+1
            current_player.pieces-=echoppe_cartes[2][carte_choisie][1]
            current_player.cartes_echoppe[2].append(carte_choisie)
        elif carte_choisie in list(echoppe_cartes[3].keys()):
            if 'eventail' in current_player.ordre_famille_echoppe:     #alors on va chercher le rang de sushi pr savoir le nb de points a attribuer
                for i in range(len(current_player.ordre_famille_echoppe)):
                    if current_player.ordre_famille_echoppe[i]=='eventail':
                        current_player.points+=2*i+1
            else : 
                current_player.ordre_famille_echoppe.append('eventail')
                current_player.points+=2*len(current_player.ordre_famille_echoppe)+1
            current_player.pieces-=echoppe_cartes[3][carte_choisie][1]
            current_player.cartes_echoppe[3].append(carte_choisie)

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
    choix(current_player, [liste_cartes_case[indice]])

def effet_rencontre(current_player):
    liste_cartes_case=test_case(current_player)
    nouvelle_rencontre=cartes_a_proposer (1,  liste_cartes_case, current_player.cartes_rencontre)
    current_player.cartes_rencontre.append(nouvelle_rencontre)
    choix(current_player, [nouvelle_rencontre])
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
    money_given=int(input('Combien dargent donnez-vous?'))
    while money_given<1 or money_given>3 or money_given>current_player.pieces:
        money_given=int(input('Mauvais montant, reesayez : '))
    current_player.pieces-=money_given
    current_player.pieces_donnees_temple+=money_given

def effet_source_chaude (current_player):
    carte=random.randint(2,3)
    if carte==2:
        current_player.points+=2
        current_player.cartes_source.append('carte 2')
    elif carte==3:
        current_player.points+=3
        current_player.cartes_source_chaude.append('carte 3')



def effet ( carte_tiree, current_player):      #carte tiree a resoudre, peut etre a enlever des parametres 
    liste_cartes_case=test_case(current_player)
    if current_player.case in echoppe_cases:
        effet_echoppe (current_player)
    elif current_player.case in pano_cases[0]+pano_cases[1]+pano_cases[2]: 
        effet_panorama (current_player, liste_cartes_case)

    elif current_player.case in rencontre_cases:
        effet_rencontre(current_player)


        current_player.cartes_rencontre=cartes_a_proposer (1,  liste_cartes_case, current_player.cartes_rencontre)




#constitution de la liste des cartes qu'on proposera au joueur selon le nbr de cartes a tirer
def cartes_a_proposer( nb_cartes_a_tirer, liste_cartes_case, current_player):
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



def choix (current_player, possible_cards):             #PYGAME!!!! cette fonction doit me return une liste comportant la ou 

    while 'le joueur ne clique pas sur valider'==True:  #les cartes choisies par le joueur (même si la carte est imposee)
        if 'le joueur clique sur carte'==True:          #Je lappelle regulierement simplement pour montrer au joueur 
            pass                                        #la carte qu'il a obtenue, ce nest pas tjrs un choix a proprement parler
