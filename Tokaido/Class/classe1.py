import pygame




IMAGES_SOURCE=[pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/2_points.png'), 
                      pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/3_points.png')]
IMAGES_ECHOPPE=[[pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/gofu.png'), 
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
IMAGES_REPAS=[pygame.image.load('Tokaido/Class/images/cartes/repas/dango.png'), 
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
IMAGES_RENCONTRE=[pygame.image.load('Tokaido/Class/images/cartes/rencontres/annaibito.png'),
                   pygame.image.load('Tokaido/Class/images/cartes/rencontres/kuge.png'),
                   pygame.image.load('Tokaido/Class/images/cartes/rencontres/miko.png'),
                   pygame.image.load('Tokaido/Class/images/cartes/rencontres/samurai.png'),
                   pygame.image.load('Tokaido/Class/images/cartes/rencontres/shokunin.png')]
IMAGES_PANORAMA=[[pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/1.png'),
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
IMAGES_ACCOMPLISSEMENTS=[pygame.image.load('Tokaido/Class/images/cartes/accomplissements/mer.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/montagne.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/riziere.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/repas.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/rencontres.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/sources_chaudes.png'),
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/souvenirs.png'),]



ECHOPPE_CARTES=[{'daifuku': [0, 2, IMAGES_ECHOPPE[1][0]], 'kamaboko': [0,1 , IMAGES_ECHOPPE[1][1]], 'konpeito': [0,1 , IMAGES_ECHOPPE[1][2]], 'manju': [0,1 , IMAGES_ECHOPPE[1][3]], 'ocha': [0, 2, IMAGES_ECHOPPE[1][4]], 'sake': [0, 2, IMAGES_ECHOPPE[1][5]]},
                {'furoshiki': [0,2 , IMAGES_ECHOPPE[3][0]], 'geta': [0, 2, IMAGES_ECHOPPE[3][1]], 'haori': [0,2 , IMAGES_ECHOPPE[3][2]], 'kanzashi': [0, 2, IMAGES_ECHOPPE[3][3]], 'sandogasa': [0,2 , IMAGES_ECHOPPE[3][4]], 'yukata': [0,2 , IMAGES_ECHOPPE[3][5]] },
                {'jubako': [0, 2, IMAGES_ECHOPPE[2][0]], 'netsuke': [0, 2, IMAGES_ECHOPPE[2][1]], 'shamisen': [0, 3, IMAGES_ECHOPPE[2][2]], 'shikki': [0,2 , IMAGES_ECHOPPE[2][3]], 'sumie': [0, 3, IMAGES_ECHOPPE[2][4]], 'ukiyoe': [0,3 , IMAGES_ECHOPPE[2][5]]},
                {'gofu': [0,1 , IMAGES_ECHOPPE[0][0]], 'hashi': [0,1 , IMAGES_ECHOPPE[0][1]], 'koma': [0,1 , IMAGES_ECHOPPE[0][2]], 'uchiwa': [0,1 , IMAGES_ECHOPPE[0][3]], 'washi': [0,1 , IMAGES_ECHOPPE[0][4]], 'yunomi': [0,1 , IMAGES_ECHOPPE[0][5]]}]               
PANO_CARTES=[{'mer_1':[1, 0, IMAGES_PANORAMA[0][0]], 'mer_2' : [2, 0, IMAGES_PANORAMA[0][1]], 
              'mer_3' : [3, 0,IMAGES_PANORAMA[0][2]] ,'mer_4' : [4, 0, IMAGES_PANORAMA[0][3]], 
              'mer_5' : [5, 0, IMAGES_PANORAMA[0][4]]},
             {'montagne_1' : [1, 0, IMAGES_PANORAMA[1][0]], 'montagne_2' : [2, 0, IMAGES_PANORAMA[1][1]],
              'montagne_3' : [3, 0, IMAGES_PANORAMA[1][2]],'montagne_4' : [4, 0, IMAGES_PANORAMA[1][3]]},
              {'riziere_1' : [1, 0, IMAGES_PANORAMA[2][0]],'riziere_2' : [2, 0, IMAGES_PANORAMA[2][1]],
               'riziere_3' : [3, 0, IMAGES_PANORAMA[2][2]]}]
SOURCE_CARTES= {'source 2':[2, 0, IMAGES_SOURCE[0]], 'source 3':[3, 0, IMAGES_SOURCE[1]]}
RENCONTRE_CARTES={'Annaibito': [0,0 , IMAGES_RENCONTRE[0]], 'Kuge': [0,0 , IMAGES_RENCONTRE[1]], 'Miko': [0,0 , IMAGES_RENCONTRE[2]], 'Samurai': [0,0 , IMAGES_RENCONTRE[3]], 'Shokunin': [0,0 , IMAGES_RENCONTRE[4]]} 
RELAIS_CARTES={'dango': [6, 1, IMAGES_REPAS[0]], 'donburi': [6, 3, IMAGES_REPAS[1]], 'fugu': [6,3 , IMAGES_REPAS[2]], 'misoshiru': [6, 1, IMAGES_REPAS[3]], 'nigirimeshi': [6, 1, IMAGES_REPAS[4]], 'sashimi': [6, 3, IMAGES_REPAS[5]], 'soba': [6, 2, IMAGES_REPAS[6]], 'sushi': [6, 2, IMAGES_REPAS[7]], 'taimeshi': [6, 3, IMAGES_REPAS[8]], 'tempura': [6,2 , IMAGES_REPAS[9]], 'tofu': [6, 2, IMAGES_REPAS[10]], 'udon': [6, 3, IMAGES_REPAS[11]], 'unagi': [6, 3, IMAGES_REPAS[12]], 'yakitori': [6,2 , IMAGES_REPAS[13]]}



def afficher_echoppe (screen, current_player):
    POS_CARTE_1= (30, 200)
    add_x=0
    add_y=0
    i=0
    for famille in current_player.cartes_echoppe : 
        for carte in famille : 
            #recuperer le chemin dacces de la carte
            image=ECHOPPE_CARTES[carte][2]
            hauteur_image=(screen.get_size()[0]-300-200)/3
            largeur_image=image.get_size()[1]/image.get_size()[0]*hauteur_image
            pygame.transform.smoothscale (image, (hauteur_image, largeur_image))
            image_pos=(POS_CARTE_1[0]+add_x+30, POS_CARTE_1[1]+add_y+50)
            screen.blit(image, image_pos)
            if i%2==0:
                add_x+=largeur_image
            else :
                add_y+=hauteur_image
                add_x-=largeur_image
            i+=1
        #passage a la famille suivante
        add_x+=screen.get_size()[0]-(6*30)-(3*largeur_image)
        add_y=0

def afficher_panorama (screen, current_player):
    if len(current_player.cartes_pano[0]+current_player.cartes_pano[1]+current_player.cartes_pano[2])==0:
        return False

    POS_CARTE_1=(100, 300)
    add_x=0
    add_y=0   

    for famille in current_player.cartes_pano:
        for carte in famille:
            image=PANO_CARTES[carte][2]
            hauteur_image=(screen.get_size()[0]-300-200)/3
            largeur_image=image.get_size()[1]/image.get_size()[0]*hauteur_image
            pygame.transform.smoothscale (image, (hauteur_image, largeur_image))
            image_pos=(POS_CARTE_1[0]+add_x, POS_CARTE_1[1]+add_y)
            screen.blit(image, image_pos)
            add_x+=image.get_size()[0]
        add_x=0
        add_y+=hauteur_image+50

   

def afficher_source (screen, current_player):
    source_2=0
    source_3=0
    for carte in current_player.cartes_source:
        if carte=='source 2':
            source_2+=1
        elif carte=='source 3':
            source_3+=1
    if source_2!=0:
        image_2=source_cartes['source 2'][2]
        #pas finito




