import pygame
import Class.affichage_plateau as Affichage_plateau
import Class.Game as Game

pygame.font.init()

JAPON = "Tokaido/Fonts/Japon.ttf"
AFFICHAGE_SOURCE  = pygame.font.Font(JAPON, 40)

#dividers pour chaque categorie de carte que l'on veut afficher
MENU_DIVIDER = 3.5
SOUVENIRS_DIVIDER = 3


def rescale(image, divider):
    return pygame.transform.smoothscale(image, (image.get_width()/divider, image.get_height()/divider))

def hover_rescale(image, pos):
    hovered_image = pygame.transform.smoothscale(image, (int(image.get_width()*1.2), int(image.get_height()*1.2)))
    hovered_image_pos = (pos[0] - (hovered_image.get_width() - image.get_width())/2, pos[1] - (hovered_image.get_height() - image.get_height())/2)
    return(hovered_image, hovered_image_pos)

def aff_plateau(screen, liste_joueurs): #Permet, lorsqu'on parcours l'inventaire, d'avoir un affichage léger
    screen.fill((0,0,0))
    Affichage_plateau.affichage_piste(screen)
    Game.affichage_HUD(screen, liste_joueurs)
    filtre(screen)

def aff_back(screen, image, hovered_image, rect, pos):
    if rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(hovered_image, pos)
    else:
        screen.blit(image, pos)

IMAGES_SOURCE={'source_2' :pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/2_points.png'),  #Images des cartes sources, rapportant 2 ou 3 points
               'source_3' :pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/3_points.png')}

#IMAGES_SOUVENIRS = [{},{},{}]
#--> [0] = accessoires
#--> [1] = nourriture
#--> [2] = objets
#--> [3] = vetements

IMAGES_SOUVENIRS={'gofu'  :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/gofu.png'), SOUVENIRS_DIVIDER), #Famille des accessoires
                   'hashi' :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/hashi.png'), SOUVENIRS_DIVIDER),
                   'koma'  :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/koma.png'), SOUVENIRS_DIVIDER),
                   'uchiwa':rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/uchiwa.png'), SOUVENIRS_DIVIDER),
                   'washi' :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/washi.png'), SOUVENIRS_DIVIDER),
                   'yunomi':rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/accessoires/yunomi.png'), SOUVENIRS_DIVIDER),
                
                  'daifuku'   :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/daifuku.png'), SOUVENIRS_DIVIDER), #Famille de la nourriture
                   'kamaboko'  :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/kamaboko.png'), SOUVENIRS_DIVIDER),
                   'konpeito'  :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/konpeito.png'), SOUVENIRS_DIVIDER),
                   'manju'     :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/manju.png'), SOUVENIRS_DIVIDER),
                   'ocha'      :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/ocha.png'), SOUVENIRS_DIVIDER),
                   'sake'      :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/nourriture/sake.png'), SOUVENIRS_DIVIDER),
         
                  'jubako'    :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/jubako.png'), SOUVENIRS_DIVIDER), #Famille des objets
                   'netsuke'   :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/netsuke.png'), SOUVENIRS_DIVIDER),
                   'shamisen'  :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/shamisen.png'), SOUVENIRS_DIVIDER),
                   'shikki'    :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/shikki.png'), SOUVENIRS_DIVIDER),
                   'sumie'     :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/sumie.png'), SOUVENIRS_DIVIDER),
                   'ukiyoe'    :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/objets/ukiyoe.png'), SOUVENIRS_DIVIDER),
                 
                  'furoshiki' :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/furoshiki.png'), SOUVENIRS_DIVIDER), #Famille des vetements
                   'geta'      :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/geta.png'), SOUVENIRS_DIVIDER),
                   'haori'     :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/haori.png'), SOUVENIRS_DIVIDER),
                   'kanzashi'  :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/kanzashi.png'), SOUVENIRS_DIVIDER),
                   'sandogasa' :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/sandogasa.png'), SOUVENIRS_DIVIDER),
                   'yukata'    :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/vetements/yukata.png'), SOUVENIRS_DIVIDER)}


IMAGES_REPAS={'dango'       :pygame.image.load('Tokaido/Class/images/cartes/repas/dango.png'),  #Tous les repas disponibles aux relais
              'donburi'     :pygame.image.load('Tokaido/Class/images/cartes/repas/donburi.png'),
              'fugu'        :pygame.image.load('Tokaido/Class/images/cartes/repas/fugu.png'),
              'misoshiru'   :pygame.image.load('Tokaido/Class/images/cartes/repas/misoshiru.png'),
              'nigirimeshi' :pygame.image.load('Tokaido/Class/images/cartes/repas/nigirimeshi.png'),
              'sashimi'     :pygame.image.load('Tokaido/Class/images/cartes/repas/sashimi.png'),
              'soba'        :pygame.image.load('Tokaido/Class/images/cartes/repas/soba.png'),
              'sushi'       :pygame.image.load('Tokaido/Class/images/cartes/repas/sushi.png'),
              'taimeshi'    :pygame.image.load('Tokaido/Class/images/cartes/repas/taimeshi.png'),
              'tempura'     :pygame.image.load('Tokaido/Class/images/cartes/repas/tempura.png'),
              'tofu'        :pygame.image.load('Tokaido/Class/images/cartes/repas/tofu.png'),
              'udon'        :pygame.image.load('Tokaido/Class/images/cartes/repas/udon.png'),
              'unagi'       :pygame.image.load('Tokaido/Class/images/cartes/repas/unagi.png'),
              'yakitori'    :pygame.image.load('Tokaido/Class/images/cartes/repas/yakitori.png')}


IMAGES_RENCONTRE={'annaibito'   :pygame.image.load('Tokaido/Class/images/cartes/rencontres/annaibito.png'), #Les differentes rencontres
                  'kuge'        :pygame.image.load('Tokaido/Class/images/cartes/rencontres/kuge.png'),
                  'miko'        :pygame.image.load('Tokaido/Class/images/cartes/rencontres/miko.png'),
                  'samurai'     :pygame.image.load('Tokaido/Class/images/cartes/rencontres/samurai.png'),
                  'shokunin'    :pygame.image.load('Tokaido/Class/images/cartes/rencontres/shokunin.png')}


IMAGES_PANORAMA={'mer'      :[pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/1.png'), #Les panoramas de la mer
                              pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/2.png'),
                              pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/3.png'),
                              pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/4.png'),
                              pygame.image.load('Tokaido/Class/images/cartes/panorama/mer/5.png')],

                 'montagne' :[pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/1.png'), #Montagne
                              pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/2.png'),
                              pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/3.png'),
                              pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/4.png')], 
                
                 'riziere'  :[pygame.image.load('Tokaido/Class/images/cartes/panorama/riziere/1.png'), #Riziere
                              pygame.image.load('Tokaido/Class/images/cartes/panorama/riziere/2.png'),
                              pygame.image.load('Tokaido/Class/images/cartes/panorama/riziere/3.png')]}


IMAGES_ACCOMPLISSEMENTS={'mer'          :pygame.image.load('Tokaido/Class/images/cartes/accomplissements/mer.png'),       #Les differents accomplissements
                         'montage'      :pygame.image.load('Tokaido/Class/images/cartes/accomplissements/montagne.png'),
                         'riziere'      :pygame.image.load('Tokaido/Class/images/cartes/accomplissements/riziere.png'),
                         'repas'        :pygame.image.load('Tokaido/Class/images/cartes/accomplissements/repas.png'),
                         'rencontres'   :pygame.image.load('Tokaido/Class/images/cartes/accomplissements/rencontres.png'),
                         'sources'      :pygame.image.load('Tokaido/Class/images/cartes/accomplissements/sources_chaudes.png'),
                         'souvenirs'    :pygame.image.load('Tokaido/Class/images/cartes/accomplissements/souvenirs.png')}

IMAGES_BACK = {'souvenirs'  :rescale(pygame.image.load('Tokaido/Class/images/cartes/souvenirs/back.png'), MENU_DIVIDER),        #L'arriere des cartes, de dimension 670x1025
               'sources'    :rescale(pygame.image.load('Tokaido/Class/images/cartes/sources_chaudes/back.png'), MENU_DIVIDER),
               'rencontres' :rescale(pygame.image.load('Tokaido/Class/images/cartes/rencontres/back.png'), MENU_DIVIDER),
               'repas'      :rescale(pygame.image.load('Tokaido/Class/images/cartes/repas/back.png'), MENU_DIVIDER),
               'panorama'   :rescale(pygame.image.load('Tokaido/Class/images/cartes/panorama/montagne/back.png'), MENU_DIVIDER)}

back = pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/HUD/back.png'), (75,75))
hovered_back = pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/HUD/hovered_back.png'), (75,75))
back_rect = back.get_rect()
BACK_POS = (10, 160)
back_rect.topleft = BACK_POS

def afficher (screen, liste_joueurs):
    #On definit une seule fois les valeurs de largeur et hauteur d'ecran
    #Assez logiquement on comprend que �a demande moins de ressources que de remesurer a chaque fois
    screen_width, screen_height = screen.get_size()

    #Positions des cartes et de leurs colliders:
    FIRST_LAYER_Y = 1/10 * screen_height
    SECOND_LAYER_Y = 1/2 * screen_height

    SOUVENIRS_POS = (1/3 * screen_width - 335/MENU_DIVIDER, FIRST_LAYER_Y)
    hovered_souvenirs, hovered_souvenirs_pos = hover_rescale(IMAGES_BACK['souvenirs'], SOUVENIRS_POS)
    SOUVENIRS_RECT = IMAGES_BACK['souvenirs'].get_rect()
    SOUVENIRS_RECT.topleft = SOUVENIRS_POS
    
    PANORAMA_POS = (1/2 * screen_width - 335/MENU_DIVIDER, FIRST_LAYER_Y)
    hovered_panorama, hovered_panorama_pos = hover_rescale(IMAGES_BACK['panorama'], PANORAMA_POS)
    PANORAMA_RECT = IMAGES_BACK['panorama'].get_rect()
    PANORAMA_RECT.topleft = PANORAMA_POS

    REPAS_POS = (2/3 * screen_width - 335/MENU_DIVIDER, FIRST_LAYER_Y)
    hovered_repas, hovered_repas_pos = hover_rescale(IMAGES_BACK['repas'], REPAS_POS)
    REPAS_RECT = IMAGES_BACK['repas'].get_rect()
    REPAS_RECT.topleft = REPAS_POS


    SOURCES_POS = (2/5 * screen_width - 335/MENU_DIVIDER, SECOND_LAYER_Y)
    hovered_sources, hovered_sources_pos = hover_rescale(IMAGES_BACK['sources'], SOURCES_POS)
    SOURCES_RECT = IMAGES_BACK['sources'].get_rect()
    SOURCES_RECT.topleft = SOURCES_POS

    RENCONTRES_POS = (3/5 * screen_width - 335/MENU_DIVIDER, SECOND_LAYER_Y)
    hovered_rencontres, hovered_rencontres_pos = hover_rescale(IMAGES_BACK['rencontres'], RENCONTRES_POS)
    RENCONTRES_RECT = IMAGES_BACK['rencontres'].get_rect()
    RENCONTRES_RECT.topleft = RENCONTRES_POS

    quit = False
    while not quit:
        aff_plateau(screen, liste_joueurs)
        if SOUVENIRS_RECT.collidepoint(pygame.mouse.get_pos()):         #Affichage des cartes du menu d'inventaire
            screen.blit(hovered_souvenirs, hovered_souvenirs_pos)
        else:
            screen.blit(IMAGES_BACK['souvenirs'], SOUVENIRS_POS)

        if PANORAMA_RECT.collidepoint(pygame.mouse.get_pos()):
            screen.blit(hovered_panorama, hovered_panorama_pos)
        else:
            screen.blit(IMAGES_BACK['panorama'], PANORAMA_POS)

        if REPAS_RECT.collidepoint(pygame.mouse.get_pos()):
            screen.blit(hovered_repas, hovered_repas_pos)
        else:
            screen.blit(IMAGES_BACK['repas'], REPAS_POS)

        if SOURCES_RECT.collidepoint(pygame.mouse.get_pos()):
            screen.blit(hovered_sources, hovered_sources_pos)
        else:
            screen.blit(IMAGES_BACK['sources'], SOURCES_POS)

        if RENCONTRES_RECT.collidepoint(pygame.mouse.get_pos()):
            screen.blit(hovered_rencontres, hovered_rencontres_pos)
        else:
            screen.blit(IMAGES_BACK['rencontres'], RENCONTRES_POS)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 1
            elif event.type == pygame.MOUSEBUTTONUP:
                if SOUVENIRS_RECT.collidepoint(pygame.mouse.get_pos()):
                    echoppe(screen, liste_joueurs)
                else:
                    Affichage_plateau.affichage_piste(screen)
                    quit = True

def echoppe(screen, liste_joueurs):     #RAPPEL : joueur.cartes_echoppe = [[],[];[],[]]
    aff_plateau(screen, liste_joueurs)
    
    LAYER_Y = 1/5 * screen.get_height() - 512/SOUVENIRS_DIVIDER
    for famille in liste_joueurs[0].cartes_echoppe:
        POS_X = 2/7 * screen.get_width() - 335/SOUVENIRS_DIVIDER
        indice_famille = 0
        for nom_carte in famille:
            screen.blit(IMAGES_SOUVENIRS[nom_carte],(POS_X, LAYER_Y))
            indice_famille+=1
            POS_X += 1/7 * screen.get_width()

        LAYER_Y += 1/(len(famille)+1)*screen.get_height()
        
        pygame.display.flip()

    quit = False
    while not quit:
        aff_back(screen, back, hovered_back, back_rect, BACK_POS)
        pygame.display.update(back_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and back_rect.collidepoint(pygame.mouse.get_pos()):
                quit = True

def panorama(screen, liste_joueurs):
    LAYER_MER_Y = 1/4*screen.get_height()


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
            largeur_image=image_width()/DIVIDER
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
    largeur_image_2=image_2_width()/DIVIDER
    scaled_image_2=pygame.transform.smoothscale (image_2, (largeur_image_2, hauteur_image_2))
    image_2_x=screen_width()/2-largeur_image_2-50
    image_2_y=screen.get_height()/2-hauteur_image_2/2
    image_2_pos=(image_2_x, image_2_y)
    image_2_text_surface = AFFICHAGE_SOURCE.render("x"+str(source_2), 1, (0,0,0))
    image_2_text_pos = (image_2_x+largeur_image_2-15, image_2_y+hauteur_image_2-15)

    image_3=SOURCE_CARTES['source 3'][2]
    hauteur_image_3=image_3.get_height()/DIVIDER
    largeur_image_3=image_3_width()/DIVIDER
    image_3_x=screen_width()/2+50
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
    largeur_image_anna=image_anna_width()/DIVIDER
    scaled_image_anna=pygame.transform.smoothscale (image_anna, (largeur_image_anna, hauteur_image_anna))
    image_anna_x=screen_width()/2-largeur_image_anna*3/2-100
    image_anna_y=screen.get_height()/2-hauteur_image_anna-50
    image_anna_pos=(image_anna_x, image_anna_y)
    image_anna_text_surface = AFFICHAGE_SOURCE.render("x"+str(annaibito), 1, (0,0,0))
    image_anna_text_pos = (image_anna_x+largeur_image_anna-15, image_anna_y+hauteur_image_anna-15)

    image_kuge=pygame.image.load('Tokaido/Class/images/cartes/rencontres/kuge.png')
    hauteur_image_kuge=image_kuge.get_height()/DIVIDER
    largeur_image_kuge=image_kuge_width()/DIVIDER
    scaled_image_kuge=pygame.transform.smoothscale (image_kuge, (largeur_image_kuge, hauteur_image_kuge))
    image_kuge_x=screen_width()/2-largeur_image_kuge/2
    image_kuge_y=screen.get_height()/2-hauteur_image_kuge-50
    image_kuge_pos=(image_kuge_x, image_kuge_y)
    image_kuge_text_surface = AFFICHAGE_SOURCE.render("x"+str(kuge), 1, (0,0,0))
    image_kuge_text_pos = (image_kuge_x+largeur_image_kuge-15, image_kuge_y+hauteur_image_kuge-15)

    image_miko=pygame.image.load('Tokaido/Class/images/cartes/rencontres/miko.png')
    hauteur_image_miko=image_miko.get_height()/DIVIDER
    largeur_image_miko=image_miko_width()/DIVIDER
    scaled_image_miko=pygame.transform.smoothscale (image_miko, (largeur_image_miko, hauteur_image_miko))
    image_miko_x=screen_width()/2+largeur_image_miko/2+100
    image_miko_y=screen.get_height()/2-hauteur_image_miko-50
    image_miko_pos=(image_miko_x, image_miko_y)
    image_miko_text_surface = AFFICHAGE_SOURCE.render("x"+str(miko), 1, (0,0,0))
    image_miko_text_pos = (image_miko_x+largeur_image_miko-15, image_miko_y+hauteur_image_miko-15)

    image_samu=pygame.image.load('Tokaido/Class/images/cartes/rencontres/samurai.png')
    hauteur_image_samu=image_samu.get_height()/DIVIDER
    largeur_image_samu=image_samu_width()/DIVIDER
    scaled_image_samu=pygame.transform.smoothscale (image_samu, (largeur_image_samu, hauteur_image_samu))
    image_samu_x=screen_width()/2-largeur_image_samu-50
    image_samu_y=screen.get_height()/2+50
    image_samu_pos=(image_samu_x, image_samu_y)
    image_samu_text_surface = AFFICHAGE_SOURCE.render("x"+str(samurai), 1, (0,0,0))
    image_samu_text_pos = (image_samu_x+largeur_image_samu-15, image_samu_y+hauteur_image_samu-15)

    image_shoku=pygame.image.load('Tokaido/Class/images/cartes/rencontres/shokunin.png')
    hauteur_image_shoku=image_shoku.get_height()/DIVIDER
    largeur_image_shoku=image_shoku_width()/DIVIDER
    scaled_image_shoku=pygame.transform.smoothscale (image_shoku, (largeur_image_shoku, hauteur_image_shoku))
    image_shoku_x=screen_width()/2+50
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
        scaled_image = pygame.transform.smoothscale(image, (image_width()/DIVIDER, image.get_height()/DIVIDER))
        if x + scaled_image_width() > screen_width - 100:
            x = 100
            y += scaled_image.get_height() + 100
        else:
            x += scaled_image_width() + 50

        screen.blit(scaled_image, (x,y))
    
    pygame.display.flip()

def filtre(screen):
    filter=pygame.Surface(screen.get_size())
    filter.set_alpha (120)
    filter.fill((175, 160, 200))
    screen.blit(filter, (0,0))

