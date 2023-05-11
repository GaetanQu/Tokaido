import random
import Class.Joueur


cases_doubles=[1,5,6,7,9,11,17,18,19,20,22,24,30,32,34,36,37,40,43,45,47,48,51,52]


pano_cases=[[11,15,24,34,39,46,52],[6,12,19,23,32,50],[4,18,28,35,51]]    #mer, montagne, riziere
pano_cartes=[{},{},{}]         #oblige de faire une liste de dictionnaires pour uniformiser, sinon une des methodes fonctionnera pas

echoppe_cases=[1,8,25,29,40,45,53]
echoppe_cartes=[{},{},{},{}]                   #sushi, kimono, statue, eventail

#Tu pars du principe que dico[nom_carte] = [points_rapportes, prix cartes, chemin dacces]

source_cases=[5,13,22,33,42,48]
source_cartes={'nom_carte':['points_rapportes', 'prix_carte', 'chemin_dacces']}            #{'Bureau/pygame/images/nom_image'[[3, 2]]}

rencontre_cases=[3,10,20,30,38,44,49]
rencontre_cartes={} 

relais_cases=[14,27,41]
relais_cartes={}

temple_cases=[2,9,16,21,36,43] 

ferme_cases=[7,17,26,31,37,47]

achievments=[1,1,1,1,1,1,1,1]

#trop bg






def test_case(current_player):             
    if current_player.case in pano_cases[1]:
        return list(pano_cartes[1].keys())
    elif current_player.case in pano_cases[2]:
        return list(pano_cartes[2].keys())
    elif current_player.case in pano_cases[3]:
        return list(pano_cartes[3].keys())
    elif current_player.case in echoppe_cases:
        return list(echoppe_cartes[1].keys())+list(echoppe_cartes[2].keys())+list(echoppe_cartes[3].keys())+list(echoppe_cartes[4].keys())
    elif current_player.case in source_cases:
        return list(source_cartes.keys())
    elif current_player.case in rencontre_cases:
        return list(rencontre_cartes.keys())
    elif current_player.case in relais_cases
        return list(relais_cartes.keys())
    else :
        return []

def effet_echoppe (current_player, shokunin=False):
    liste_cartes_case=test_case(current_player)
    if shokunin==True:
        nouvel_objet=liste_cartes_case[random.randint(0, len(liste_cartes_case)-1)]
        current_player                      #a finir, ajouter la carte dans la bonne liste.
        return
    possible_cards=cartes_a_proposer(3, liste_cartes_case, current_player)
    cartes_choisies=choix(current_player, possible_cards)           #il faudra aussi suppr les cartes choisies par le joueur de la liste generale
    for carte_choisie in cartes_choisies : 
        if carte_choisie in list(echoppe_cartes[0].keys()):
            if 'sushi' in current_player.ordre_famille_echoppe:     #alors on va chercher le rang de sushi pr savoir le nb de points a attribuer
                for i in range(len(current_player.ordre_famille_echoppe)):  #ne pas oublier d'enlever des pieces
                    if current_player.ordre_famille_echoppe[i]=='sushi':
                        current_player.points+=2*i+1
            else : 
                current_player.ordre_famille_echoppe.append('sushi')
                current_player.points+=2*len(current_player.ordre_famille_echoppe)+1
        elif carte_choisie in list(echoppe_cartes[1].keys()):
            if 'kimono' in current_player.ordre_famille_echoppe:     
                for i in range(len(current_player.ordre_famille_echoppe)):
                    if current_player.ordre_famille_echoppe[i]=='kimono':
                        current_player.points+=2*i+1
            else : 
                current_player.ordre_famille_echoppe.append('kimono')
                current_player.points+=2*len(current_player.ordre_famille_echoppe)+1
        elif carte_choisie in list(echoppe_cartes[2].keys()):
            if 'statue' in current_player.ordre_famille_echoppe:     
                for i in range(len(current_player.ordre_famille_echoppe)):
                    if current_player.ordre_famille_echoppe[i]=='statue':
                        current_player.points+=2*i+1
            else : 
                current_player.ordre_famille_echoppe.append('statue')
                current_player.points+=2*len(current_player.ordre_famille_echoppe)+1
        elif carte_choisie in list(echoppe_cartes[3].keys()):
            if 'eventail' in current_player.ordre_famille_echoppe:     #alors on va chercher le rang de sushi pr savoir le nb de points a attribuer
                for i in range(len(current_player.ordre_famille_echoppe)):
                    if current_player.ordre_famille_echoppe[i]=='eventail':
                        current_player.points+=2*i+1
        else : 
            current_player.ordre_famille_echoppe.append('eventail')
            current_player.points+=2*len(current_player.ordre_famille_echoppe)+1

def effet_panorama (current_player):
    liste_cartes_case=test_case(current_player)
    if current_player.case in pano_cases[0]:                                               #SI CASE = PANO MER
        indice=0
        while liste_cartes_case[indice] in current_player.cartes_pano[0] :
            indice+=1
        if indice<=len(liste_cartes_case):                                     #on ajoute la carte pano ssi le current_player ne la pas encore
            current_player.cartes_pano[0].append(liste_cartes_case[indice])            #(car les cartes pano se recoivent dans lordre)
            current_player.points+=pano_cartes[0][liste_cartes_case[indice]][0]
    elif current_player.case in pano_cases[1]:                                             #SI CASE = PANO MONTAGNE
        indice=0
        while liste_cartes_case[indice] in current_player.cartes_pano[1] :
            indice+=1
        if indice<=len(liste_cartes_case):                                     
            current_player.cartes_pano[1].append(liste_cartes_case[indice])            
            current_player.points+=pano_cartes[1][liste_cartes_case[indice]][0]   #[0] car les points sont stock�s en 1er rang dans le dico.
    elif current_player.case in pano_cases[2]:                                             #SI CASE = PANO RIZIERE

        indice=0
        while liste_cartes_case[indice] in current_player.cartes_pano[2] :
            indice+=1
        if indice<=len(liste_cartes_case):                                     
            current_player.cartes_pano[2].append(liste_cartes_case[indice])            
            current_player.points+=pano_cartes[2][liste_cartes_case[indice]][0]
    choix(current_player, [liste_cartes_case[indice]][0])

def effet_rencontre(current_player):
    liste_cartes_case=test_case(current_player)
    i=0
    for carte in liste_cartes_case:    
        if carte in current_player.cartes_rencontre:
            del(liste_cartes_case[i])
        i+=1   
    nouvelle_rencontre=cartes_a_proposer (1,  liste_cartes_case, current_player.cartes_rencontre)
    current_player.cartes_rencontre.append(nouvelle_rencontre)
    if nouvelle_rencontre=='Kuge':
        current_player.pieces+=3
    elif nouvelle_rencontre=='Samurai':
        current_player.points+=3
    elif nouvelle_rencontre=='Miko':
        current_player.points+=1
        current_player.pieces_donnees_temple+=1
    elif nouvelle_rencontre=='Shokunin':
        effet_echoppe(current_player, shokunin=True)


def effet ( carte_tiree, current_player):      #carte tiree a resoudre, peut etre a enlever des parametres 
    liste_cartes_case=test_case(current_player)
    if current_player.case in echoppe_cases:
        effet_echoppe (current_player)
    elif current_player.case in pano_cases[0]+pano_cases[1]+pano_cases[2]: 
        effet_panorama (current_player, liste_cartes_case)

    elif current_player.case in rencontre_cases:
        effet_rencontre(current_player)
        i=0
        for carte in liste_cartes_case:    
            if carte in current_player.cartes_rencontre:
                del(liste_cartes_case[i])
            i+=1   
        current_player.cartes_rencontre=cartes_a_proposer (1,  liste_cartes_case, current_player.cartes_rencontre)





def cartes_a_proposer( nb_cartes_a_tirer, liste_cartes_case, current_player):
    possible_cards=[]                                                            #liste des cartes qui seront proposees au current_player                       
    for i in range (nb_cartes_a_tirer):                                             #constitution de la liste des cartes � proposer
        indice_carte=Random.randint(1,len(liste_cartes_case)-i-1)
        possible_cards.append(liste_cartes_case[indice_carte])              #il faudra ajouter la partie pygame en prenant en compte le nombre de cartes a tirer
        del(liste_cartes_case[indice_carte])
    return possible_cards





    
def achievments ( current_player, indice_achievment):
    if achievments[indice_achievment]==1:
        current_player.achievments[indice_achievment]=1
        achievments[indice_achievment]=0  



def choix (current_player, possible_cards):             #PYGAME!!!! cette fonction doit me return une liste comportant la ou 
    while 'le joueur ne clique pas sur valider'==True:  #les cartes choisies par le joueur (même si la carte est imposee)
        if 'le joueur clique'==True:
            pass
