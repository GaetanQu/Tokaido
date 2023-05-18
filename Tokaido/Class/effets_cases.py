import random
import pygame


pygame.font.init()

JAPON = "Tokaido/Fonts/Japon.ttf"
POLICE  = pygame.font.Font(JAPON, 40)


images_source_chaude=[pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/2_points.png'), 
                      pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/3_points.png')]
images_objets_echoppe=[[pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/gofu.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/hashi.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/koma.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/uchiwa.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/washi.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/yunomi.png')], 
                       [pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/daifuku.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/kamaboko.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/konpeito.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/manju.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/ocha.png'), 
                        pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/sake.png')], 
                        [pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/jubako.png'), 
                         pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/netsuke.png'), 
                         pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/shamisen.png'), 
                         pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/shikki.png'), 
                         pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/sumie.png'), 
                         pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/ukiyoe.png')], 
                         [pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/furoshiki.png'), 
                          pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/geta.png'), 
                          pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/haori.png'), 
                          pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/kanzashi.png'), 
                          pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/sandogasa.png'), 
                          pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/yukata.png')]]
images_repas=[pygame.image.load('Tokaido/Class/images/cartes/repas/dango.png'), 
              pygame.image.load('Tokaido/Class/images/cartes/repas/donburi.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/fugu.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/misoshiru.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/nigirimeshi.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/sashimi.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/soba.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/sushi.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/taimeshi.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/tempura.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/tofu.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/udon.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/unagi.png'),
              pygame.image.load('Tokaido/Class/images/cartes/repas/yakitori.png')]
images_rencontres=[pygame.image.load('Tokaido/Class/images/cartes/rencontres/annaibito.png'),
                   pygame.image.load('Tokaido/Class/images/cartes/rencontres/kuge.png'),
                   pygame.image.load('Tokaido/Class/images/cartes/rencontres/miko.png'),
                   pygame.image.load('Tokaido/Class/images/cartes/rencontres/samurai.png'),
                   pygame.image.load('Tokaido/Class/images/cartes/rencontres/shokunin.png')]
images_panorama=[[pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/1.png'),
                  pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/2.png'),
                  pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/3.png'),
                  pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/4.png'),
                  pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/5.png')],
                [pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/1.png'),
                 pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/2.png'),
                 pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/3.png'),
                 pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/4.png')], 
                 [pygame.image.load('Tokaido/Class/images/cartes/panorama/riziere/1.png'),
                  pygame.image.load('Tokaido/Class/images/cartes/panorama/riziere/2.png'),
                  pygame.image.load('Tokaido/Class/images/cartes/panorama/riziere/3.png')]]
images_accomplissements=[pygame.image.load('Tokaido/Class/images/cartes/accomplissements/mer.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/montagne.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/riziere.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/repas.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/rencontres.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/sources_chaudes.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/souvenirs.png'),]



cases_doubles=[1,5,6,7,9,11,17,18,19,20,22,24,30,32,34,36,37,40,43,45,47,48,51,52]

#mer, montagne, riziere
pano_cases=[[11,15,24,34,39,46,52],[6,12,19,23,32,50],[4,18,28,35,51]]
pano_cartes=[{'mer_1':[1, 0, images_panorama[0][0]], 'mer_2' : [2, 0, images_panorama[0][1]], 
              'mer_3' : [3, 0,images_panorama[0][2]] ,'mer_4' : [4, 0, images_panorama[0][3]], 
              'mer_5' : [5, 0, images_panorama[0][4]]},
             {'montagne_1' : [1, 0, images_panorama[1][0]], 'montagne_2' : [2, 0, images_panorama[1][1]],
              'montagne_3' : [3, 0, images_panorama[1][2]],'montagne_4' : [4, 0, images_panorama[1][3]]},
              {'riziere_1' : [1, 0, images_panorama[2][0]],'riziere_2' : [2, 0, images_panorama[2][1]],
               'riziere_3' : [3, 0, images_panorama[2][2]]}]

echoppe_cases=[1,8,25,29,40,45,53]
#sushi, kimono, statue, eventail
#A noter que les points dans le dico echoppe ne servent a rien (mettre 0)
echoppe_cartes=[{'daifuku': [0, 2, images_objets_echoppe[1][0]], 'kamaboko': [0,1 , images_objets_echoppe[1][1]], 'konpeito': [0,1 , images_objets_echoppe[1][2]], 'manju': [0,1 , images_objets_echoppe[1][3]], 'ocha': [0, 2, images_objets_echoppe[1][4]], 'sake': [0, 2, images_objets_echoppe[1][5]]},
                {'furoshiki': [0,2 , images_objets_echoppe[3][0]], 'geta': [0, 2, images_objets_echoppe[3][1]], 'haori': [0,2 , images_objets_echoppe[3][2]], 'kanzashi': [0, 2, images_objets_echoppe[3][3]], 'sandogasa': [0,2 , images_objets_echoppe[3][4]], 'yukata': [0,2 , images_objets_echoppe[3][5]] },
                {'jubako': [0, 2, images_objets_echoppe[2][0]], 'netsuke': [0, 2, images_objets_echoppe[2][1]], 'shamisen': [0, 3, images_objets_echoppe[2][2]], 'shikki': [0,2 , images_objets_echoppe[2][3]], 'sumie': [0, 3, images_objets_echoppe[2][4]], 'ukiyoe': [0,3 , images_objets_echoppe[2][5]]},
                {'gofu': [0,1 , images_objets_echoppe[0][0]], 'hashi': [0,1 , images_objets_echoppe[0][1]], 'koma': [0,1 , images_objets_echoppe[0][2]], 'uchiwa': [0,1 , images_objets_echoppe[0][3]], 'washi': [0,1 , images_objets_echoppe[0][4]], 'yunomi': [0,1 , images_objets_echoppe[0][5]]}]               

#Tu pars du principe que dico[nom_carte] = [points_rapportes, prix carte, chemin dacces]

source_cases=[5,13,22,33,42,48]
source_cartes= {'source 2':[2, 0, images_source_chaude[0]], 'source 3':[3, 0, images_source_chaude[1]]}           #{'Bureau/pygame/images/nom_image'[[3, 2]]}

rencontre_cases=[3,10,20,30,38,44,49]
rencontre_cartes={'Annaibito': [0,0 , images_rencontres[0]], 'Kuge': [0,0 , images_rencontres[1]], 'Miko': [0,0 , images_rencontres[2]], 'Samurai': [0,0 , images_rencontres[3]], 'Shokunin': [0,0 , images_rencontres[4]]} 

relais_cases=[14,27,41]
relais_cartes={'dango': [6, 1, images_repas[0]], 'donburi': [6, 3, images_repas[1]], 'fugu': [6,3 , images_repas[2]], 'misoshiru': [6, 1, images_repas[3]], 'nigirimeshi': [6, 1, images_repas[4]], 'sashimi': [6, 3, images_repas[5]], 'soba': [6, 2, images_repas[6]], 'sushi': [6, 2, images_repas[7]], 'taimeshi': [6, 3, images_repas[8]], 'tempura': [6,2 , images_repas[9]], 'tofu': [6, 2, images_repas[10]], 'udon': [6, 3, images_repas[11]], 'unagi': [6, 3, images_repas[12]], 'yakitori': [6,2 , images_repas[13]]}

temple_cases=[2,9,16,21,36,43] 

ferme_cases=[7,17,26,31,37,47]

achievments=[1,1,1,1,1,1,1,1]



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

def effet_echoppe (current_player, screen, shokunin=False):

    if shokunin==True:
        objet_shokunin=liste_cartes_case[random.randint(0, len(liste_cartes_case)-1)]
        cartes_choisies=[objet_shokunin]       
        #affichage de la carte tiree au sort
        carte_imposee(objet_shokunin, rencontre_cartes, screen)
    else : 
        liste_cartes_case=test_case(current_player)
        #creation de la liste des cartes correspondant a la case
        possible_cards=cartes_a_proposer(3, liste_cartes_case)
        
        retail_card_zenemon=possible_cards[random.randint(0, len(possible_cards)-1)]
        cartes_choisies=choix(current_player, possible_cards, multiple_choices_possibility=True)
    for famille in echoppe_cartes:
        if cartes_choisies[0] in list(famille.keys()):
            carte_moins_cher=cartes_choisies[0]
            prix_carte_moins_cher=famille[carte_moins_cher][1]
    for carte_choisie in cartes_choisies : 

        if carte_choisie in list(echoppe_cartes[0].keys()):
            annexe_echoppe (current_player, carte_choisie, 'sushi', 0, shokunin, retail_card_zenemon)
                #determiner la carte qui sera gratuite pour sasayakko
            if current_player.personnage=='Sasayakko' and shokunin==False and len(cartes_choisies)>=2:
                if prix_carte_moins_cher>echoppe_cartes[0][carte_choisie][1]: 
                    carte_moins_cher=carte_choisie
                    prix_carte_moins_cher=echoppe_cartes[0][carte_choisie][1]

        elif carte_choisie in list(echoppe_cartes[1].keys()):
            annexe_echoppe (current_player, carte_choisie, 'kimono', 1, shokunin, retail_card_zenemon)
            if current_player.personnage=='Sasayakko' and shokunin==False and len(cartes_choisies)>=2:
                if prix_carte_moins_cher>echoppe_cartes[1][carte_choisie][1]: 
                    carte_moins_cher=carte_choisie
                    prix_carte_moins_cher=echoppe_cartes[1][carte_choisie][1]
        elif carte_choisie in list(echoppe_cartes[2].keys()):
            annexe_echoppe (current_player, carte_choisie , 'statue', 2, shokunin, retail_card_zenemon)
            if current_player.personnage=='Sasayakko' and shokunin==False and len(cartes_choisies)>=2:
                if prix_carte_moins_cher>echoppe_cartes[2][carte_choisie][1]: 
                    carte_moins_cher=carte_choisie
                    prix_carte_moins_cher=echoppe_cartes[2][carte_choisie][1]

        elif carte_choisie in list(echoppe_cartes[3].keys()):
            annexe_echoppe (current_player, carte_choisie, 'eventail', 3, shokunin, retail_card_zenemon)
            if current_player.personnage=='Sasayakko' and shokunin==False and len(cartes_choisies)>=2:
                if prix_carte_moins_cher>echoppe_cartes[3][carte_choisie][1]: 
                    carte_moins_cher=carte_choisie
                    prix_carte_moins_cher=echoppe_cartes[3][carte_choisie][1]

def annexe_echoppe (current_player, carte_choisie, mot_cle, indice_cle, shokunin, retail_card_zenemon):
    if mot_cle in current_player.ordre_famille_echoppe:     #alors on va chercher le rang de sushi pr savoir le nb de points a attribuer
        for i in range(len(current_player.ordre_famille_echoppe)):  #ne pas oublier d'enlever des pieces
            if current_player.ordre_famille_echoppe[i]==mot_cle:
                current_player.points+=2*i+1
                current_player.pieces-=echoppe_cartes[indice_cle][carte_choisie][1]
    else : 
        current_player.ordre_famille_echoppe.append(mot_cle)
        current_player.points+=2*len(current_player.ordre_famille_echoppe)+1
    current_player.cartes_echoppe[indice_cle].append(carte_choisie)
    del (echoppe_cartes[carte_choisie])

    #on retire des pieces ssi cest pas le shokunin (rencontre) qui donne la carte
    if shokunin==False :
        current_player.pieces-=echoppe_cartes[indice_cle][carte_choisie][1]
        if current_player.personnage=='Zen-Emon'and carte_choisie==retail_card_zenemon:
            current_player.pieces+=echoppe_cartes[indice_cle][carte_choisie][1]-1

def effet_panorama (current_player, screen, mer=False, montagne=False, riziere=False): 
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
        annexe_panorama (current_player, 0, liste_cartes_case, screen)
    elif current_player.case in pano_cases[1] or montagne==True:                                             #SI CASE = PANO MONTAGNE
        annexe_panorama(current_player, 1, liste_cartes_case, screen)
    elif current_player.case in pano_cases[2] or riziere==True:   
        annexe_panorama (current_player, 2, liste_cartes_case, screen)          #SI CASE = PANO RIZIERE

def annexe_panorama (current_player, indice_cle, liste_cartes_case,screen, hiroshige=False ):
    indice=0
    while liste_cartes_case[indice] in current_player.cartes_pano[indice_cle] :
        indice+=1
        if indice == len(liste_cartes_case)-1:
            break
    if indice<len(liste_cartes_case)-1:                                     #on ajoute la carte pano ssi le current_player ne la pas encore
        nom_carte=liste_cartes_case[indice]
        if hiroshige==False:
            current_player.cartes_pano[indice_cle].append(nom_carte)            #(car les cartes pano se recoivent dans lordre)
            current_player.points+=pano_cartes[indice_cle][nom_carte][0]
            carte_imposee([liste_cartes_case][indice], pano_cartes[indice_cle], screen)
        else : 
            return nom_carte
    elif indice==len(liste_cartes_case)-1:
        achievments(current_player, indice_cle)


def effet_rencontre(current_player, screen):
    liste_cartes_case=test_case(current_player)
    if current_player.personnage!='Yoshiyasu':
        nouvelle_rencontre=cartes_a_proposer (1,  liste_cartes_case)
    elif current_player.personnage=='Yoshiyasu':
        possible_cards=cartes_a_proposer (2, liste_cartes_case)
        nouvelle_rencontre=choix (current_player, possible_cards)
    current_player.cartes_rencontre.append(nouvelle_rencontre)
    carte_imposee(nouvelle_rencontre, rencontre_cartes, screen)
    if nouvelle_rencontre=='Kuge':
        current_player.pieces+=3
    elif nouvelle_rencontre=='Samurai':
        current_player.points+=3
    elif nouvelle_rencontre=='Miko':
        current_player.points+=1
        current_player.pieces_donnees_temple+=1
    elif nouvelle_rencontre=='Shokunin':
        effet_echoppe(current_player, shokunin=True)
    elif nouvelle_rencontre=='Annaibito':    
        possible_cards=[]
        for indice in range (3):
            possible_cards.append(annexe_panorama (current_player,indice, list(pano_cartes[indice].keys()), hiroshige=True ))
        carte_choisie=choix(current_player, possible_cards)
        for i in range (3):
            if carte_choisie[0] in list(pano_cartes[i].keys()):
                current_player.cartes_pano[i].append(carte_choisie[0])
       
def effet_ferme (current_player):
    current_player.pieces+=3

#le joueur ne peut s'arreter que s'il a argent car DOIT donner 1, 2, ou 3 pièces.
#fonction a completer par du sg pour demander le nombre de pieces a donner
def effet_temple (current_player):
    if current_player.personnage=='Hirotada':
        current_player.pieces_donnees_temple+=1
        current_player.points+=1
    money_given=int(input('Combien dargent donnez-vous?'))
    while money_given<1 or money_given>3 or money_given>current_player.pieces:
        money_given=int(input('Mauvais montant, reesayez : '))
    current_player.pieces-=money_given
    current_player.pieces_donnees_temple+=money_given

def effet_source_chaude (current_player, screen):
    carte=random.randint(2,3)
    if current_player.personnage=='Mitsukuni':
        current_player.points+=1
    if carte==2:
        current_player.points+=2
        current_player.cartes_source.append('carte 2')
        carte_imposee('carte 2', source_cartes, screen)
    elif carte==3:
        current_player.points+=3
        current_player.cartes_source_chaude.append('carte 3')
        carte_imposee('carte 3', source_cartes, screen)

def effet_relais (current_player, players_list, possible_cards_relais, screen):
    liste_cartes_case=test_case(current_player.case)
    players_in_relais=0

    for player in players_list:
        if player.case in relais_cases:
            players_in_relais+=1
    #si il ny a quun joueur dans le relais, cela signifie quon doit generer la liste des cartes tirables ET la return pour les prochains arrivants
    if players_in_relais==1:
        possible_cards_relais=cartes_a_proposer(len(players_list)+1, liste_cartes_case, current_player)
    if current_player.personnage=='Satsuki':
        free_card=possible_cards_relais[random.randint(0, len(possible_cards_relais)-1)]
    carte_choisie=choix (current_player, possible_cards_relais)[0]

    
    if len(carte_choisie)==1:
        #car lachat nest pas obligatoire au relais 
        new_card=carte_choisie[0]
        current_player.cartes_repas.append (new_card)
        current_player.pieces-=relais_cartes[new_card][1]
        if current_player.personnage=='Kinko':
            current_player.pieces+=1
        elif current_player.personnage=='Satsuki':
            if new_card==free_card:
                current_player.pieces+=relais_cartes[new_card][1]
        current_player.points+=relais_cartes[new_card][0]
        possible_cards_relais.remove(carte_choisie)

    if current_player.personnage=='Chuubei':
        effet_rencontre(current_player, screen)
    elif current_player.personnage=='Hiroshige':
        possible_cards_pano=[]
        for indice in range (3):
            possible_cards_pano.append(annexe_panorama (current_player,indice, list(pano_cartes[indice].keys()), hiroshige=True ))
        carte_choisie=choix(current_player, possible_cards_pano)
        for i in range (3):
            if carte_choisie[0] in list(pano_cartes[i].keys()):
                current_player.cartes_pano[i].append(carte_choisie[0])

    return possible_cards_relais          

#a faire, attribution des accomplissements
def effet_fin_de_partie(current_player):
    pass

def effet (current_player, players_list, screen, list_cartes_relais_restantes=[]):
    if current_player.case in echoppe_cases:
        effet_echoppe (current_player, screen)
    elif current_player.case in pano_cases[0]+pano_cases[1]+pano_cases[2]: 
        effet_panorama (current_player, screen)

    elif current_player.case in rencontre_cases:
        effet_rencontre(current_player, screen)
        if current_player.personnage=='Umegae':
            current_player.points+=1
            current_player.pieces+=1

    elif current_player.case in ferme_cases:
        effet_ferme(current_player)

    elif current_player.case in temple_cases:
        effet_temple(current_player)

    elif current_player.case in source_cases:
        effet_source_chaude(current_player, screen)

    elif current_player.case in relais_cases:
        list_cartes_relais_restantes=effet_relais (current_player, players_list, list_cartes_relais_restantes)
        return list_cartes_relais_restantes

def someone_in_relais (current_player):
    if current_player.case in relais_cases:
        return True
    else : 
        return False

def everyone_in_relais (players_list):
    for player in players_list :
        if player.case not in relais_cases :
            return False
    return True

def pg_test_case (numero):
    if numero in pano_cases[0]:
        return pygame.image.load('Tokaido/Class/images/cases/mer.png')
    elif numero in pano_cases[1]:
        return pygame.image.load('Tokaido/Class/images/cases/montagne.png')
    elif numero in pano_cases[2]:
        return pygame.image.load('Tokaido/Class/images/cases/riziere.png')
    elif numero in echoppe_cases:
        return pygame.image.load('Tokaido/Class/images/cases/echoppe.png')
    elif numero in source_cases:
        return pygame.image.load('Tokaido/Class/images/cases/source.png')
    elif numero in rencontre_cases:
        return pygame.image.load('Tokaido/Class/images/cases/rencontre.png')
    elif numero in relais_cases:
        return pygame.image.load('Tokaido/Class/images/cases/relais.png')
    elif numero in temple_cases:
        return pygame.image.load('Tokaido/Class/images/cases/temple.png')
    elif numero in ferme_cases :
        return pygame.image.load('Tokaido/Class/images/cases/ferme.png')

#constitution de la liste des cartes qu'on proposera au joueur selon le nbr de cartes a tirer
def cartes_a_proposer( nb_cartes_a_tirer, liste_cartes_case):
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




#multiple_choices_possibility=True lorsque le joueur ne peut en choisir qu'une, 
#multiple_choices_possibility=False par defaut, si le joueur peut en prendre plusieurs (echoppe)
def choix (screen, current_player, possible_cards, dico_possible_cards, multiple_choices_possibility=False):    #PYGAME!!!! cette fonction doit me return une liste comportant la ou les cartes choisies par le joueur
    cartes_choisies = []
    
    POS_CARTES = [(1/4 * screen.get_width() - 670/2, 1/5 * screen.get_height()), (1/2 * screen.get_width() - 670/2, 1/5 * screen.get_height()), (3/4 * screen.get_width() - 670/2, 1/5 * screen.get_height())]
    
    POS_CARTES_RECT = []
    for pos in POS_CARTES:
        POS_CARTES_RECT.append((pos[0] + 670/2, pos[1] + 1024/2))

    BOUTON_TEXT = POLICE.render("Valider", 1, (0,0,0))
    BOUTON_POS = (screen.get_width()/2 - BOUTON_TEXT.get_width() /2, screen.get_height()/2 - BOUTON_TEXT.get_height/2)
    BOUTON_VALIDER_RECT = pygame.Rect((BOUTON_POS[0]-10, BOUTON_POS[1]), (BOUTON_TEXT.get_width() + 10, BOUTON_TEXT.get_height()))
    
    pygame.draw.rect(BOUTON_VALIDER_RECT)
    pygame.blit (BOUTON_TEXT, BOUTON_POS)

    i=0
    rect = []
    for carte in possible_cards:
        screen.blit(dico_possible_cards[carte], POS_CARTES[i])
        rect.apend(dico_possible_cards[carte].get_rect())
        rect[i].center(POS_CARTES_RECT[i])
        i+=1
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                i=0
                for rectangle in rect:
                    if rectangle.collidepoint(pygame.mouse.get_pos()):
                        if possible_cards[i] not in cartes_choisies:
                            cartes_choisies.append(possible_cards[i])
                        else :
                            cartes_choisies.remove(possible_cards[i])
                if BOUTON_VALIDER_RECT.collidepoint(pygame.mouse.get_pos()):
                    return cartes_choisies

#given_card ici n'est pas une liste, on veut juste 'nom_carte'
#la fonction ne doit rien renvoyer, ni append, juste montrer au joueur sa nouvelle carte.
def carte_imposee (given_card, origin_dico, screen):
    DIVIDER=5
    carte=origin_dico[given_card][2]
    scaled_card=pygame.transform.smoothscale (carte, (carte.get_width()/DIVIDER, carte.get_height()/DIVIDER))
    card_pos=(screen.get_width()/2-scaled_card.get_width()/2, screen.get_height()/2-scaled_card.get_height()/2-50)

    police1  = pygame.font.Font(JAPON, 18)
    texte=police1.render('Accepter la nouvelle carte', 1,(0,0,0))

    BOUTON_RECT = pygame.Rect((screen.get_width()-texte.get_width())/2-9, card_pos[1]+scaled_card.get_height()+50, texte.get_width()+18, 40)
    pygame.draw.rect(screen, (141, 147, 190), BOUTON_RECT)
    texte_rect = texte.get_rect(center=(card_pos[0] + scaled_card.get_width() // 2, card_pos[1]+scaled_card.get_height()+50 + 40 // 2))

    screen.blit(scaled_card, card_pos)
    screen.blit(texte, texte_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  BOUTON_RECT.collidepoint(pygame.mouse.get_pos()):
                    break



#fonction qui return false si le joueur ne peut pas s'arreter sur la case
def can_stop_here (current_player, list_players):
    if current_player.case in pano_cases[0] and len(current_player.cartes_pano[0])==5:
        return False
    elif current_player.case in pano_cases[1] and len(current_player.cartes_pano[2])==4:
        return False
    elif current_player.case in pano_cases[2] and len(current_player.cartes_pano[2])==3:
        return False
    elif current_player.case in temple_cases and current_player.pieces==0:
        return False
    joueurs_on_case=1
    for joueur in list_players:
        if joueur!=current_player :
            if joueur.case==current_player.case and joueur.case not in cases_doubles:
                return False
            elif joueur.case==current_player.case and joueur.case in cases_doubles :
                joueurs_on_case+=1
    if joueurs_on_case>2:
        return False

    return True

