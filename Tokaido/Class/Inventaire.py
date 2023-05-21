import pygame
import Class.Joueur
import PySimpleGUI as sg

pygame.font.init()

JAPON = "Tokaido/Fonts/Japon.ttf"
AFFICHAGE_SOURCE  = pygame.font.Font(JAPON, 40)

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
                         pygame.image.load('Tokaido/Class/images/cartes/accomplissements/souvenirs.png')]



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

def afficher (screen, current_player):    
    DIVIDER=3
    image_souvenirs=pygame.image.load('Tokaido/Class/images/cartes/souvenirs/back.png')
    hauteur_image_souvenirs=image_souvenirs.get_height()/DIVIDER
    largeur_image_souvenirs=image_souvenirs.get_width()/DIVIDER
    scaled_image_souvenirs=pygame.transform.smoothscale (image_souvenirs, (largeur_image_souvenirs, hauteur_image_souvenirs))
    image_souvenirs_x=screen.get_width()/2-largeur_image_souvenirs*3/2-100
    image_souvenirs_y=screen.get_height()/2-hauteur_image_souvenirs-50
    image_souvenirs_pos=(image_souvenirs_x, image_souvenirs_y)


    image_sources_chaudes=pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/back.png')
    hauteur_image_sources_chaudes=image_sources_chaudes.get_height()/DIVIDER
    largeur_image_sources_chaudes=image_sources_chaudes.get_width()/DIVIDER
    scaled_image_sources_chaudes=pygame.transform.smoothscale (image_sources_chaudes, (largeur_image_sources_chaudes, hauteur_image_sources_chaudes))
    image_sources_chaudes_x=screen.get_width()/2-largeur_image_sources_chaudes/2
    image_sources_chaudes_y=screen.get_height()/2-hauteur_image_sources_chaudes-50
    image_sources_chaudes_pos=(image_sources_chaudes_x, image_sources_chaudes_y)


    image_rencontres=pygame.image.load('Tokaido/Class/images/cartes/rencontres/back.png')
    hauteur_image_rencontres=image_rencontres.get_height()/DIVIDER
    largeur_image_rencontres=image_rencontres.get_width()/DIVIDER
    scaled_image_rencontres=pygame.transform.smoothscale (image_rencontres, (largeur_image_rencontres, hauteur_image_rencontres))
    image_rencontres_x=screen.get_width()/2+largeur_image_rencontres/2+100
    image_rencontres_y=screen.get_height()/2-hauteur_image_rencontres-50
    image_rencontres_pos=(image_rencontres_x, image_rencontres_y)


    image_repas=pygame.image.load('Tokaido/Class/images/cartes/repas/back.png')
    hauteur_image_repas=image_repas.get_height()/DIVIDER
    largeur_image_repas=image_repas.get_width()/DIVIDER
    scaled_image_repas=pygame.transform.smoothscale (image_repas, (largeur_image_repas, hauteur_image_repas))
    image_repas_x=screen.get_width()/2-largeur_image_repas-50
    image_repas_y=screen.get_height()/2+50
    image_repas_pos=(image_repas_x, image_repas_y)


    image_panorama=pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/back.png')
    hauteur_image_panorama=image_panorama.get_height()/DIVIDER
    largeur_image_panorama=image_panorama.get_width()/DIVIDER
    scaled_image_panorama=pygame.transform.smoothscale (image_panorama, (largeur_image_panorama, hauteur_image_panorama))
    image_panorama_x=screen.get_width()/2+50
    image_panorama_y=screen.get_height()/2+50
    image_panorama_pos=(image_panorama_x, image_panorama_y)

    souvenirs_rect = scaled_image_souvenirs.get_rect()
    souvenirs_rect.topleft = (image_souvenirs_x, image_souvenirs_y)

    sources_chaudes_rect = scaled_image_sources_chaudes.get_rect()
    sources_chaudes_rect.topleft = (largeur_image_sources_chaudes, hauteur_image_sources_chaudes)

    rencontres_rect = scaled_image_rencontres.get_rect()
    rencontres_rect.topleft = (largeur_image_rencontres, hauteur_image_rencontres)

    repas_rect = scaled_image_repas.get_rect()
    repas_rect.topleft = (largeur_image_repas, hauteur_image_repas)

    panorama_rect = scaled_image_panorama.get_rect()
    panorama_rect.topleft = (largeur_image_panorama, hauteur_image_panorama)

    filter=pygame.Surface(screen.get_size())
    filter.set_alpha (120)
    filter.fill((175, 160, 200))
    screen.blit(filter, (0,0))

    screen.blit (scaled_image_souvenirs, image_souvenirs_pos)

    screen.blit (scaled_image_sources_chaudes, image_sources_chaudes_pos)

    screen.blit (scaled_image_rencontres, image_rencontres_pos)

    screen.blit (scaled_image_repas, image_repas_pos)

    screen.blit (scaled_image_panorama, image_panorama_pos)


    pygame.display.flip()

    quit = False

    while not quit: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                while event != pygame.MOUSEBUTTONUP:
                    for event in pygame.event.get():
                        if souvenirs_rect.collidepoint(pygame.mouse.get_pos()):
                            afficher_echoppe(screen, current_player)

                        elif sources_chaudes_rect.collidepoint(pygame.mouse.get_pos()):
                            while event != pygame.MOUSEBUTTONUP :
                                for event in pygame.event.get():
                                    afficher_source(screen, current_player)

                        elif rencontres_rect.collidepoint(pygame.mouse.get_pos()):
                            while event != pygame.MOUSEBUTTONUP :
                                for event in pygame.event.get():
                                        afficher_rencontre(screen, current_player)

                        elif repas_rect.collidepoint(pygame.mouse.get_pos()):
                            while event != pygame.MOUSEBUTTONUP :
                                for event in pygame.event.get():
                                    afficher_repas(screen, current_player)

                        elif panorama_rect.collidepoint(pygame.mouse.get_pos()):
                            while event != pygame.MOUSEBUTTONUP :
                                for event in pygame.event.get():
                                    afficher_panorama(screen, current_player)
                        else:
                            quit = True
            
def afficher_echoppe (screen, current_player):
    POS_CARTE_1= (100, 200)
    add_x=0
    add_y=0
    i=0
    j=0
    DIVIDER=5
    for famille in current_player.cartes_echoppe : 
        if famille == []:
            largeur_image = 0
        for carte in famille : 
            #recuperer le chemin dacces de la carte
            image=ECHOPPE_CARTES[j][carte][2]
            hauteur_image=image.get_height()/DIVIDER
            largeur_image=image.get_width()/DIVIDER

            scaled_image=pygame.transform.smoothscale (image, (largeur_image, hauteur_image))
            image_pos=(POS_CARTE_1[0]+add_x, POS_CARTE_1[1]+add_y+50)
            screen.blit(scaled_image, image_pos)
            if i%2==0:
                add_x+=largeur_image+30
            else :
                add_y+=hauteur_image
                add_x-=(largeur_image+30)
            i+=1
        #passage a la famille suivante
        add_x+=screen.get_size()[0]-(6*120)-(3*largeur_image)
        add_y=0
        j+=1
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                return True
        pygame.display.flip()

def afficher_panorama (screen, current_player):
    if len(current_player.cartes_pano[0]+current_player.cartes_pano[1]+current_player.cartes_pano[2])==0:
        return False

    POS_CARTE_1=(100, 200)
    add_x=0
    add_y=0   
    i=0
    DIVIDER = 5

    for famille in current_player.cartes_pano:
        for carte in famille:
            image=PANO_CARTES[i][carte][2]
            hauteur_image=image.get_height()/DIVIDER
            largeur_image=image.get_width()/DIVIDER
            scaled_image = pygame.transform.smoothscale (image, (largeur_image, hauteur_image))
            image_pos=(POS_CARTE_1[0]+add_x, POS_CARTE_1[1]+add_y)
            screen.blit(scaled_image, image_pos)
            add_x+=scaled_image.get_size()[0]
            pygame.display.flip()
        i+=1
        add_x=0
        add_y+=hauteur_image+50

def afficher_source (screen, current_player):
    #variables qui stockent le nombre de fois que le joueur a cette carte
    source_2=0
    source_3=0
    DIVIDER=6



    for carte in current_player.cartes_source:
        if carte=='source 2':
            source_2+=1
        elif carte=='source 3':
            source_3+=1

    image_2=SOURCE_CARTES['source 2'][2]
    hauteur_image_2=image_2.get_height()/DIVIDER
    largeur_image_2=image_2.get_width()/DIVIDER
    scaled_image_2=pygame.transform.smoothscale (image_2, (largeur_image_2, hauteur_image_2))
    image_2_x=screen.get_width()/2-largeur_image_2-50
    image_2_y=screen.get_height()/2-hauteur_image_2/2
    image_2_pos=(image_2_x, image_2_y)
    image_2_text_surface = AFFICHAGE_SOURCE.render("x"+str(source_2), 1, (0,0,0))
    image_2_text_pos = (image_2_x+largeur_image_2-15, image_2_y+hauteur_image_2-15)

    image_3=SOURCE_CARTES['source 3'][2]
    hauteur_image_3=image_3.get_height()/DIVIDER
    largeur_image_3=image_3.get_width()/DIVIDER
    image_3_x=screen.get_width()/2+50
    image_3_y=screen.get_height()/2-hauteur_image_2/2
    image_3_pos=(image_3_x, image_3_y)
    scaled_image_3=pygame.transform.smoothscale (image_3, (largeur_image_3, hauteur_image_3))
    image_3_text_surface = AFFICHAGE_SOURCE.render("x"+str(source_3), 1, (0,0,0))
    image_3_text_pos = (image_3_x+largeur_image_3-15, image_3_y+hauteur_image_3-15)

    screen.blit (scaled_image_2, image_2_pos)
    screen.blit (scaled_image_3, image_3_pos)
    screen.blit (image_2_text_surface, image_2_text_pos)
    screen.blit (image_3_text_surface, image_3_text_pos)

    pygame.display.flip()

def afficher_rencontre (screen, current_player):
    annaibito=0
    kuge=0
    miko=0
    samurai=0
    shokunin=0
    for carte in current_player.cartes_rencontre : 
        if carte=='Annaibito':
            annaibito+=1
        elif carte=='Kuge':
            kuge+=1
        elif carte=='Miko':
            miko+=1
        elif carte=='Samurai':
            samurai+=1
        elif carte=='Shokunin':
            shokunin+=1
    

    DIVIDER=3
    image_anna=pygame.image.load('Tokaido/Class/images/cartes/rencontres/annaibito.png')
    hauteur_image_anna=image_anna.get_height()/DIVIDER
    largeur_image_anna=image_anna.get_width()/DIVIDER
    scaled_image_anna=pygame.transform.smoothscale (image_anna, (largeur_image_anna, hauteur_image_anna))
    image_anna_x=screen.get_width()/2-largeur_image_anna*3/2-100
    image_anna_y=screen.get_height()/2-hauteur_image_anna-50
    image_anna_pos=(image_anna_x, image_anna_y)
    image_anna_text_surface = AFFICHAGE_SOURCE.render("x"+str(annaibito), 1, (0,0,0))
    image_anna_text_pos = (image_anna_x+largeur_image_anna-15, image_anna_y+hauteur_image_anna-15)

    image_kuge=pygame.image.load('Tokaido/Class/images/cartes/rencontres/kuge.png')
    hauteur_image_kuge=image_kuge.get_height()/DIVIDER
    largeur_image_kuge=image_kuge.get_width()/DIVIDER
    scaled_image_kuge=pygame.transform.smoothscale (image_kuge, (largeur_image_kuge, hauteur_image_kuge))
    image_kuge_x=screen.get_width()/2-largeur_image_kuge/2
    image_kuge_y=screen.get_height()/2-hauteur_image_kuge-50
    image_kuge_pos=(image_kuge_x, image_kuge_y)
    image_kuge_text_surface = AFFICHAGE_SOURCE.render("x"+str(kuge), 1, (0,0,0))
    image_kuge_text_pos = (image_kuge_x+largeur_image_kuge-15, image_kuge_y+hauteur_image_kuge-15)

    image_miko=pygame.image.load('Tokaido/Class/images/cartes/rencontres/miko.png')
    hauteur_image_miko=image_miko.get_height()/DIVIDER
    largeur_image_miko=image_miko.get_width()/DIVIDER
    scaled_image_miko=pygame.transform.smoothscale (image_miko, (largeur_image_miko, hauteur_image_miko))
    image_miko_x=screen.get_width()/2+largeur_image_miko/2+100
    image_miko_y=screen.get_height()/2-hauteur_image_miko-50
    image_miko_pos=(image_miko_x, image_miko_y)
    image_miko_text_surface = AFFICHAGE_SOURCE.render("x"+str(miko), 1, (0,0,0))
    image_miko_text_pos = (image_miko_x+largeur_image_miko-15, image_miko_y+hauteur_image_miko-15)

    image_samu=pygame.image.load('Tokaido/Class/images/cartes/rencontres/samurai.png')
    hauteur_image_samu=image_samu.get_height()/DIVIDER
    largeur_image_samu=image_samu.get_width()/DIVIDER
    scaled_image_samu=pygame.transform.smoothscale (image_samu, (largeur_image_samu, hauteur_image_samu))
    image_samu_x=screen.get_width()/2-largeur_image_samu-50
    image_samu_y=screen.get_height()/2+50
    image_samu_pos=(image_samu_x, image_samu_y)
    image_samu_text_surface = AFFICHAGE_SOURCE.render("x"+str(samurai), 1, (0,0,0))
    image_samu_text_pos = (image_samu_x+largeur_image_samu-15, image_samu_y+hauteur_image_samu-15)

    image_shoku=pygame.image.load('Tokaido/Class/images/cartes/rencontres/shokunin.png')
    hauteur_image_shoku=image_shoku.get_height()/DIVIDER
    largeur_image_shoku=image_shoku.get_width()/DIVIDER
    scaled_image_shoku=pygame.transform.smoothscale (image_shoku, (largeur_image_shoku, hauteur_image_shoku))
    image_shoku_x=screen.get_width()/2+50
    image_shoku_y=screen.get_height()/2+50
    image_shoku_pos=(image_shoku_x, image_shoku_y)
    image_shoku_text_surface = AFFICHAGE_SOURCE.render("x"+str(shokunin), 1, (0,0,0))
    image_shoku_text_pos = (image_shoku_x+largeur_image_shoku-15, image_shoku_y+hauteur_image_shoku-15)



    filter=pygame.Surface(screen.get_size())
    filter.set_alpha (120)
    filter.fill((175, 160, 200))
    screen.blit(filter, (0,0))

    screen.blit (scaled_image_anna, image_anna_pos)
    screen.blit (image_anna_text_surface, image_anna_text_pos)

    screen.blit (scaled_image_kuge, image_kuge_pos)
    screen.blit (image_kuge_text_surface, image_kuge_text_pos)

    screen.blit (scaled_image_miko, image_miko_pos)
    screen.blit (image_miko_text_surface, image_miko_text_pos)

    screen.blit (scaled_image_samu, image_samu_pos)
    screen.blit (image_samu_text_surface, image_samu_text_pos)

    screen.blit (scaled_image_shoku, image_shoku_pos)
    screen.blit (image_shoku_text_surface, image_shoku_text_pos)


    pygame.display.flip()

def afficher_repas(screen, current_player):
    x,y = 100,250
    DIVIDER = 4
    for carte in current_player.carte_repas:
        image = RELAIS_CARTES[carte][2]
        scaled_image = pygame.transform.smoothscale(image, (image.get_width()/DIVIDER, image.get_height()/DIVIDER))
        if x + scaled_image.get_width() > screen.get_width - 100:
            x = 100
            y += scaled_image.get_height() + 100
        else:
            x += scaled_image.get_width() + 50

        screen.blit(scaled_image, (x,y))
    
    pygame.display.flip()
