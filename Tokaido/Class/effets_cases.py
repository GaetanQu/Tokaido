import random
import pygame
import PySimpleGUI as sg

pygame.font.init()

#Dimensions des images : 670x1025

JAPON = "Tokaido/Fonts/Japon.ttf"
POLICE  = pygame.font.Font(JAPON, 40)

GENERAL_DIVIDER = 2
SCALED_SIZE = (670/GENERAL_DIVIDER, 1025/GENERAL_DIVIDER)


images_source_chaude=[pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/2_points.png'), SCALED_SIZE), 
                      pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/3_points.png'), SCALED_SIZE)]
images_objets_echoppe=[[pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/gofu.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/hashi.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/koma.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/uchiwa.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/washi.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/yunomi.png'), SCALED_SIZE)], 
                       [pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/daifuku.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/kamaboko.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/konpeito.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/manju.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/ocha.png'), SCALED_SIZE), 
                        pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/sake.png'), SCALED_SIZE)], 
                        [pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/jubako.png'), SCALED_SIZE), 
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/netsuke.png'), SCALED_SIZE), 
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/shamisen.png'), SCALED_SIZE), 
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/shikki.png'), SCALED_SIZE), 
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/sumie.png'), SCALED_SIZE), 
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/ukiyoe.png'), SCALED_SIZE)], 
                         [pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/furoshiki.png'), SCALED_SIZE), 
                          pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/geta.png'), SCALED_SIZE), 
                          pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/haori.png'), SCALED_SIZE), 
                          pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/kanzashi.png'), SCALED_SIZE), 
                          pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/sandogasa.png'), SCALED_SIZE), 
                          pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/yukata.png'), SCALED_SIZE)]]
images_repas=[pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/dango.png'), SCALED_SIZE), 
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/donburi.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/fugu.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/misoshiru.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/nigirimeshi.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/sashimi.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/soba.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/sushi.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/taimeshi.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/tempura.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/tofu.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/udon.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/unagi.png'), SCALED_SIZE),
              pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/repas/yakitori.png'), SCALED_SIZE)]
images_rencontres=[pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/rencontres/annaibito.png'), SCALED_SIZE),
                   pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/rencontres/kuge.png'), SCALED_SIZE),
                   pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/rencontres/miko.png'), SCALED_SIZE),
                   pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/rencontres/samurai.png'), SCALED_SIZE),
                   pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/rencontres/shokunin.png'), SCALED_SIZE)]
images_panorama=[[pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/1.png'), SCALED_SIZE),
                  pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/2.png'), SCALED_SIZE),
                  pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/3.png'), SCALED_SIZE),
                  pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/4.png'), SCALED_SIZE),
                  pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/5.png'), SCALED_SIZE)],
                [pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/1.png'), SCALED_SIZE),
                 pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/2.png'), SCALED_SIZE),
                 pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/3.png'), SCALED_SIZE),
                 pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/4.png'), SCALED_SIZE)], 
                 [pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/riziere/1.png'), SCALED_SIZE),
                  pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/riziere/2.png'), SCALED_SIZE),
                  pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/panorama/riziere/3.png'), SCALED_SIZE)]]
images_accomplissements=[pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/accomplissements/mer.png'), SCALED_SIZE),
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/accomplissements/montagne.png'), SCALED_SIZE),
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/accomplissements/riziere.png'), SCALED_SIZE),
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/accomplissements/repas.png'), SCALED_SIZE),
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/accomplissements/rencontres.png'), SCALED_SIZE),
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/accomplissements/sources_chaudes.png'), SCALED_SIZE),
                         pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/cartes/accomplissements/souvenirs.png'), SCALED_SIZE)]

croix = pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/menu/croix.png'), (120,120))

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
source_cartes= {'source 2':[2, 0, images_source_chaude[0]], 'source 3':[3, 0, images_source_chaude[1]]}          

rencontre_cases=[3,10,20,30,38,44,49]
rencontre_cartes={'Annaibito': [0,0 , images_rencontres[0]], 'Kuge': [0,0 , images_rencontres[1]], 'Miko': [0,0 , images_rencontres[2]], 'Samurai': [0,0 , images_rencontres[3]], 'Shokunin': [0,0 , images_rencontres[4]]} 

relais_cases=[14,27,41]
relais_cartes={'dango': [6, 1, images_repas[0]], 
               'donburi': [6, 3, images_repas[1]], 
               'fugu': [6,3 , images_repas[2]], 
               'misoshiru': [6, 1, images_repas[3]], 
               'nigirimeshi': [6, 1, images_repas[4]], 
               'sashimi': [6, 3, images_repas[5]], 
               'soba': [6, 2, images_repas[6]], 
               'sushi': [6, 2, images_repas[7]], 
               'taimeshi': [6, 3, images_repas[8]], 
               'tempura': [6,2 , images_repas[9]], 
               'tofu': [6, 2, images_repas[10]], 
               'udon': [6, 3, images_repas[11]], 
               'unagi': [6, 3, images_repas[12]], 
               'yakitori': [6,2 , images_repas[13]]}

temple_cases=[2,9,16,21,36,43] 

ferme_cases=[7,17,26,31,37,47]

achievments_list=[1,1,1,1,1,1,1,1]



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
        liste_cartes_case = list(echoppe_cartes[0].keys())+list(echoppe_cartes[1].keys())+list(echoppe_cartes[2].keys())+list(echoppe_cartes[3].keys())
        objet_shokunin=liste_cartes_case[random.randint(0, len(liste_cartes_case)-1)]
        cartes_choisies=[objet_shokunin]
        #affichage de la carte tiree au sort

        for famille in echoppe_cartes:
            if objet_shokunin in list(famille.keys()):
                carte_imposee([objet_shokunin], famille, screen)
    else : 
        liste_cartes_case=test_case(current_player)
        #creation de la liste des cartes correspondant a la case
        possible_cards=cartes_a_proposer(3, liste_cartes_case)
        
        dico_cartes={**echoppe_cartes[0], **echoppe_cartes[1], **echoppe_cartes[2], **echoppe_cartes[3]}
        cartes_choisies=choix(screen, current_player, possible_cards, dico_cartes, multiple_choices_possibility=True)
    if len(cartes_choisies)!=0:
        for famille in echoppe_cartes:
            if cartes_choisies[0] in list(famille.keys()):
                carte_moins_cher=cartes_choisies[0]
                prix_carte_moins_cher=famille[carte_moins_cher][1]
    
        for carte_choisie in cartes_choisies : 
            if carte_choisie in list(echoppe_cartes[0].keys()):
                annexe_echoppe (current_player, carte_choisie, 'sushi', 0, shokunin)
                    #determiner la carte qui sera gratuite pour sasayakko
                if current_player.personnage=='Sasayakko' and shokunin==False and len(cartes_choisies)>=2:
                    if prix_carte_moins_cher>echoppe_cartes[0][carte_choisie][1]: 
                        carte_moins_cher=carte_choisie
                        prix_carte_moins_cher=echoppe_cartes[0][carte_choisie][1]
                del (echoppe_cartes[0][carte_choisie])

            elif carte_choisie in list(echoppe_cartes[1].keys()):
                annexe_echoppe (current_player, carte_choisie, 'kimono', 1, shokunin)
                if current_player.personnage=='Sasayakko' and shokunin==False and len(cartes_choisies)>=2:
                    if prix_carte_moins_cher>echoppe_cartes[1][carte_choisie][1]: 
                        carte_moins_cher=carte_choisie
                        prix_carte_moins_cher=echoppe_cartes[1][carte_choisie][1]
                del (echoppe_cartes[1][carte_choisie])

            elif carte_choisie in list(echoppe_cartes[2].keys()):
                annexe_echoppe (current_player, carte_choisie , 'statue', 2, shokunin)
                if current_player.personnage=='Sasayakko' and shokunin==False and len(cartes_choisies)>=2:
                    if prix_carte_moins_cher>echoppe_cartes[2][carte_choisie][1]: 
                        carte_moins_cher=carte_choisie
                        prix_carte_moins_cher=echoppe_cartes[2][carte_choisie][1]
                del (echoppe_cartes[2][carte_choisie])

            elif carte_choisie in list(echoppe_cartes[3].keys()):
                annexe_echoppe (current_player, carte_choisie, 'eventail', 3, shokunin)
                if current_player.personnage=='Sasayakko' and shokunin==False and len(cartes_choisies)>=2:
                    if prix_carte_moins_cher>echoppe_cartes[3][carte_choisie][1]: 
                        carte_moins_cher=carte_choisie
                        prix_carte_moins_cher=echoppe_cartes[3][carte_choisie][1]
                del (echoppe_cartes[3][carte_choisie])

def annexe_echoppe (current_player, carte_choisie, mot_cle, indice_cle, shokunin):
    if mot_cle in current_player.ordre_famille_echoppe:     #alors on va chercher le rang de sushi pr savoir le nb de points a attribuer
        for i in range(len(current_player.ordre_famille_echoppe)):  #ne pas oublier d'enlever des pieces
            if current_player.ordre_famille_echoppe[i]==mot_cle:
                current_player.points+=2*i+1
                current_player.pieces-=echoppe_cartes[indice_cle][carte_choisie][1]
    else : 
        current_player.ordre_famille_echoppe.append(mot_cle)
        current_player.points+=2*len(current_player.ordre_famille_echoppe)-1
    current_player.cartes_echoppe[indice_cle].append(carte_choisie)

    #on retire des pieces ssi cest pas le shokunin (rencontre) qui donne la carte
    if shokunin==False :
        current_player.pieces-=echoppe_cartes[indice_cle][carte_choisie][1]
        if current_player.personnage=='Zen-Emon':
            liste_prix = []
            for carte in carte_choisie :
                liste_prix.append(echoppe_cartes[indice_cle][carte][1])
            current_player.pieces+=max(liste_prix)-1
    



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
            carte_imposee([liste_cartes_case[indice]], pano_cartes[indice_cle], screen)
        else : 
            return nom_carte
    elif indice==len(liste_cartes_case)-1:
        achievments(current_player, indice_cle)

def effet_temple_sg (screen, current_player):

    layout = [
        [sg.Text("Combien de pieces voulez-vous donner ?")],
        [sg.Input(key='-PIECES-')],
        [sg.Button('Valider')]]

    window = sg.Window('Nombre de pieces', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Valider':
            nombre_pieces = int(values['-PIECES-'])

            # V�rifier si la valeur est valide
            if  1 <= nombre_pieces <= 3:
                window.close()
                current_player.pieces -= nombre_pieces
                current_player.pieces_donnees_temple += nombre_pieces
                current_player.points += nombre_pieces
                effet_temple(current_player)
                return 0
            else:
                sg.popup("Veuillez entrer un nombre de pieces valide (entre 1 et 3).")
    window.close()

def effet_rencontre(current_player, screen, chuubei=False):
    liste_cartes_case=test_case(current_player)    
    if current_player.personnage=='Yoshiyasu':
        possible_cards=cartes_a_proposer (2, liste_cartes_case)
        nouvelle_rencontre=choix (screen, current_player, possible_cards, rencontre_cartes)

    #cas ou le joueur est au relais et que son perso est chuubei :
    elif chuubei==True:
        liste_cartes_case=list(rencontre_cartes.keys())
        nouvelle_rencontre=[liste_cartes_case[random.randint(0, len(liste_cartes_case)-1)]]
    else:
        nouvelle_rencontre=cartes_a_proposer (1,  liste_cartes_case)

    current_player.cartes_rencontre.append(nouvelle_rencontre)

    nom_nouvelle_rencontre = nouvelle_rencontre[0]
    if current_player.personnage!='Yoshiyasu':
        carte_imposee(nouvelle_rencontre, rencontre_cartes, screen)
    if nom_nouvelle_rencontre=='Kuge':
        current_player.pieces+=3
    elif nom_nouvelle_rencontre=='Samurai':
        current_player.points+=3
    elif nom_nouvelle_rencontre=='Miko':
        current_player.points+=1
        current_player.pieces_donnees_temple+=1
    elif nom_nouvelle_rencontre=='Shokunin':
        effet_echoppe(current_player, screen, shokunin=True)
    elif nom_nouvelle_rencontre=='Annaibito':    
        possible_cards=[]
        for indice in range (3):
            possible_cards.append(annexe_panorama (current_player,indice, list(pano_cartes[indice].keys()), screen, hiroshige=True ))
        dico_cartes={**pano_cartes[0], **pano_cartes[1], **pano_cartes[2]}
        carte_choisie=choix(screen, current_player, possible_cards, dico_cartes)
        for i in range (3):
            if carte_choisie[0] in list(pano_cartes[i].keys()):
                current_player.cartes_pano[i].append(carte_choisie[0])
                current_player.points+=len(current_player.cartes_pano[i])
       
def effet_ferme (current_player):
    current_player.pieces+=3

#le joueur ne peut s'arreter que s'il a argent car DOIT donner 1, 2, ou 3 pièces.
#fonction a completer par du sg pour demander le nombre de pieces a donner
def effet_temple (current_player):
    if current_player.personnage=='Hirotada':
        current_player.pieces_donnees_temple+=1
        current_player.points+=1

def effet_source_chaude (current_player, screen):
    carte=random.randint(2,3)
    if current_player.personnage=='Mitsukuni':
        current_player.points+=1
    if carte==2:
        current_player.points+=2
        current_player.cartes_source.append('source 2')
        carte_imposee(['source 2'], source_cartes, screen)
    elif carte==3:
        current_player.points+=3
        current_player.cartes_source.append('source 3')
        carte_imposee(['source 3'], source_cartes, screen)

def effet_relais (current_player, players_list, possible_cards_relais, screen):
    liste_cartes_case=test_case(current_player)
    players_in_relais=0
    relais=players_list[0].case
    for player in players_list:
        if player.case == relais:
            players_in_relais+=1
    #si il ny a quun joueur dans le relais, cela signifie quon doit generer la liste des cartes tirables ET la return pour les prochains arrivants
    if players_in_relais==1:

        #on a set que il y avait 5 joueurs par defaut, et les joueurs non-definis ont pour case 99, donc :
        nb_players=0
        for player in players_list:
            if player.case!=99:
                nb_players+=1

        possible_cards_relais=cartes_a_proposer(nb_players+1, liste_cartes_case)
    if current_player.personnage=='Satsuki':
        free_card=possible_cards_relais[0]
    carte_choisie=choix(screen, current_player, possible_cards_relais, relais_cartes)




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
        possible_cards_relais.remove(carte_choisie[0])

    if current_player.personnage=='Chuubei':
        effet_rencontre(current_player, screen, chuubei=True)
    elif current_player.personnage=='Hiroshige':
        possible_cards_pano=[]
        for indice in range (3):
            possible_cards_pano.append(annexe_panorama (current_player,indice, list(pano_cartes[indice].keys()), screen, hiroshige=True ))
        
        dico_cartes={**pano_cartes[0], **pano_cartes[1], **pano_cartes[2]}
        carte_choisie_hiro=choix(screen, current_player, possible_cards_pano, dico_cartes)[0]
        for i in range (3):
            if carte_choisie_hiro in list(pano_cartes[i].keys()):
                current_player.cartes_pano[i].append(carte_choisie_hiro)
                current_player.points+=len(current_player.cartes_pano[i])

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
        effet_temple_sg(screen, current_player)

    elif current_player.case in source_cases:
        effet_source_chaude(current_player, screen)

    elif current_player.case in relais_cases:
        list_cartes_relais_restantes=effet_relais (current_player, players_list, list_cartes_relais_restantes, screen)
        return list_cartes_relais_restantes

def someone_in_relais (current_player):
    if current_player.case in relais_cases:
        return True
    else : 
        return False

def everyone_in_relais (players_list):
    relais=players_list[0].case
    for player in players_list :
        if player.case !=relais and player.case!=99:
            return False
    return True


#constitution de la liste des cartes qu'on proposera au joueur selon le nbr de cartes a tirer
def cartes_a_proposer(nb_cartes_a_tirer, liste_cartes_case):
    possible_cards=[]                      
    for i in range (nb_cartes_a_tirer):
        indice_carte=random.randint(1,len(liste_cartes_case)-i-1)
        possible_cards.append(liste_cartes_case[indice_carte])              
        del(liste_cartes_case[indice_carte])
    return possible_cards

#simple test si lachievment est deja recupere    
def achievments ( current_player, indice_achievment):       
    if achievments_list[indice_achievment]==1:
        current_player.achievments[indice_achievment]=1
        achievments[indice_achievment]=0  
        if current_player.personnage=='Mitsukuni':
            current_player.points+=1

#multiple_choices_possibility=True lorsque le joueur ne peut en choisir qu'une, 
#multiple_choices_possibility=False par defaut, si le joueur peut en prendre plusieurs (echoppe)
def choix (screen, current_player, possible_cards, dico_possible_cards, multiple_choices_possibility=False):    #PYGAME!!!! cette fonction doit me return une liste comportant la ou les cartes choisies par le joueur
    cartes_choisies = []
    
    nb_cartes = len(possible_cards)

    POS_CARTES = []
    i = 1
    for carte in possible_cards:
        POS_CARTES.append((i/(nb_cartes+1) * screen.get_width() - SCALED_SIZE[0]/2, 1/5 * screen.get_height()))
        i+=1

    BOUTON_TEXT = POLICE.render("Valider", 1, (0,0,0))
    BOUTON_POS = (screen.get_width()/2 - BOUTON_TEXT.get_width() /2, 3/4*screen.get_height())
    BOUTON_VALIDER = pygame.Surface((BOUTON_TEXT.get_width() + 30, BOUTON_TEXT.get_height() + 10))
    BOUTON_VALIDER.fill((20,230,20))
    BOUTON_VALIDER_RECT = BOUTON_VALIDER.get_rect()
    BOUTON_VALIDER_RECT.topleft = BOUTON_POS[0] - 15, BOUTON_POS[1]
    


    i=0
    rect = []
    aff_filtre(screen)
    for carte in possible_cards:
        screen.blit(dico_possible_cards[carte][2], POS_CARTES[i])
        rect.append(dico_possible_cards[carte][2].get_rect())
        rect[i].topleft = POS_CARTES[i]
        i+=1
 

    screen.blit(BOUTON_VALIDER, (BOUTON_POS[0]-15, BOUTON_POS[1]))
    screen.blit(BOUTON_TEXT, BOUTON_POS)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                i=0
                for rectangle in rect:
                    if rectangle.collidepoint(pygame.mouse.get_pos()):
                        if possible_cards[i] not in cartes_choisies:
                            pygame.draw.rect(pygame.Surface((670,1025)), (75,75,75), pygame.Rect((0,i), (50,50)))
                            cartes_choisies.append(possible_cards[i])
                        else :
                            cartes_choisies.remove(possible_cards[i])
                        if current_player.personnage == 'Satsuki' and current_player.case in relais_cases:
                            screen.blit(croix, (POS_CARTES[0][0] + 5, POS_CARTES[0][1]))
                    i+=1
                if BOUTON_VALIDER_RECT.collidepoint(pygame.mouse.get_pos()):
                    return cartes_choisies
        

#given_card ici n'est pas une liste, on veut juste 'nom_carte', DOMMAGE POUR TOI, C'EST UNE LISTE
#la fonction ne doit rien renvoyer, ni append, juste montrer au joueur sa nouvelle carte.
def carte_imposee (given_card, origin_dico, screen):
    DIVIDER=1.5
    carte=origin_dico[given_card[0]][2]
    scaled_card=pygame.transform.smoothscale (carte, (carte.get_width()/DIVIDER, carte.get_height()/DIVIDER))
    card_pos=(screen.get_width()/2-scaled_card.get_width()/2, screen.get_height()/2-scaled_card.get_height()/2-50)

    police1  = pygame.font.Font(JAPON, 18)
    texte=police1.render('Accepter la nouvelle carte', 1,(0,0,0))

    BOUTON_RECT = pygame.Rect((screen.get_width()-texte.get_width())/2-9, card_pos[1]+scaled_card.get_height()+50, texte.get_width()+18, 40)
    pygame.draw.rect(screen, (141, 147, 190), BOUTON_RECT)
    texte_rect = texte.get_rect(center=(card_pos[0] + scaled_card.get_width() // 2, card_pos[1]+scaled_card.get_height()+50 + 40 // 2))

    aff_filtre(screen)

    screen.blit(scaled_card, card_pos)
    screen.blit(texte, texte_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  BOUTON_RECT.collidepoint(pygame.mouse.get_pos()):
                    return 0



#fonction qui return false si le joueur ne peut pas s'arreter sur la case
def can_stop_here (current_player, list_players):
    if current_player.case in relais_cases:
        return True
    elif current_player.case in pano_cases[0] and len(current_player.cartes_pano[0])==5:
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

def aff_filtre(screen):
    filter = pygame.Surface(screen.get_size())
    filter.fill((20,20,20))
    filter.set_alpha(100)

    screen.blit(filter, (0,0))