import pygame
import random
from Class.Settings import *

BG_COLOR = (251,253,248)

settings = Settings()
FPS = int(settings.setting["FPS"])

JAPON = "Tokaido/Fonts/Japon.ttf"

JETONSIZE = (175, 175)

clock = pygame.time.Clock()

bg = pygame.image.load("Tokaido/Class/images/menu/bg.png")
bg = pygame.transform.scale(bg, (2*bg.get_size()[0], 2*bg.get_size()[1]))

jeton = {"bleu" : pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/jetons/bleu.png'), JETONSIZE),
          "hovered_bleu" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_bleu.png"), JETONSIZE),
          "jaune" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/jaune.png"), JETONSIZE),
          "hovered_jaune" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_jaune.png"), JETONSIZE),
          "rouge" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/rouge.png"), JETONSIZE),
          "hovered_rouge" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_rouge.png"), JETONSIZE),
          "vert" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/vert.png"), JETONSIZE),
          "hovered_vert" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_vert.png"), JETONSIZE),
          "violet" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/violet.png"), JETONSIZE),
          "hovered_violet" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_violet.png"), JETONSIZE),
          "taken_color" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/taken_color.png"), JETONSIZE)}

#perso = [nom : [desc, image, pieces]]

dico_perso = { "Chuubei" : ["Chuubei le messager pioche une carte Rencontre lorsqu'il arrive dans chacun des trois Relais intermediaires", pygame.image.load("Tokaido/Class/images/personnages/chuubei.png"), 4],
               "Hiroshige" : ["Hiroshige l'artiste prend une carte Panorama de son choix lorsqu'il arrive dans chacun des trois Relais intermediaires", pygame.image.load("Tokaido/Class/images/personnages/hiroshige.png"), 3], 
               "Hirotada" : ["A chaque arret au temple, Hirotada le pretre se verra beni d'une piece offerte gratuitement au temple.", pygame.image.load("Tokaido/Class/images/personnages/hirotada.png"), 8], 
               "Kinko" : ["Les cartes repas achetees par Kinko le ronin lui coutent une piece de moins", pygame.image.load("Tokaido/Class/images/personnages/kinko.png"), 7], 
               "Mitsukuni" : ["Chaque carte Source Chaude et chaque carte Accomplissement rapporte un point summplementaire a Mitsukuni le vieillard", pygame.image.load("Tokaido/Class/images/personnages/mitsukuni.png"), 6], 
               "Sasayakko" : ["Dans les villages, si Sasayakko la geisha achete au moins deux Souvenirs, le moins cher des deux lui est offert", pygame.image.load("Tokaido/Class/images/personnages/sasayakko.png"), 5], 
               "Satsuki" : ["Lors de son arrivee au Relais, Satsuki l'orpheline recoit aleatoirement et gratuitement pour une carte repas", pygame.image.load("Tokaido/Class/images/personnages/satsuki.png"), 2], 
               "Umegae" : ["Umegae la saltimbanque gagne un point et une piece lors de chaque rencontre", pygame.image.load("Tokaido/Class/images/personnages/umegae.png"), 5], 
               "Yoshiyasu" : ["Lors de chaque rencontre, Yoshiyasu le fonctionnaire choisi une carte Rencontre parmi deux au choix", pygame.image.load("Tokaido/Class/images/personnages/yoshiyasu.png"), 9], 
               "Zen-Emon" : ["Zen-Emon le marchand peur acheter l'un des Souvenirs pour une seule piece au lieu du prix indique, une fois par Echoppe", pygame.image.load("Tokaido/Class/images/personnages/zen-emon.png"), 6]}

liste_perso = list(dico_perso.keys())

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.couleur=None
        self.personnage=None
        self.pieces=0
        self.cartes_pano=[[],[],[]]             #mer, montagne, riziere
        self.cartes_repas=[]
        self.cartes_echoppe=[[],[],[],[]]        #4 familles de cartes, faudrait les mettre dans l'ordre 
        self.ordre_famille_echoppe=[]           #car l'ordre dans lequel le joueur prend les cartes est important. liste prendra en paramètre sushi, kimono, statue, eventail.
        self.cartes_source=[]
        self.pieces_donnees_temple=0
        self.pieces_depensees_repas=0
        self.case=0
        self.points=0
        self.achievements=[0,0,0,0,0,0,0,0]     #pano_mer, pano_montagne, pano_riziere, temples, repas, source chaude, rencontre, souvenir 
                                                #on remplace pas 1 si le mec a l'achievment.
    

    def avancer (self):
        self.case+=int(input('Combien de cases?'))

    def choix_perso(self, liste_joueurs):
        self.liste_joueurs = liste_joueurs
        
        liste_perso_joueurs = []
        for joueur in liste_joueurs :
            liste_perso_joueurs.append(joueur.personnage)

        pygame.init()
        pygame.display.init()
        pygame.font.init()

        liste_choix_perso = []
        for i in range (3) :
            perso_envisageable = dico_perso[liste_perso[random.randint(0,len(liste_perso)-1)]]
            while perso_envisageable in liste_perso_joueurs or perso_envisageable in liste_choix_perso:
                perso_envisageable = dico_perso[liste_perso[random.randint(0,len(liste_perso)-1)]]
            liste_choix_perso.append(perso_envisageable)

        screen = pygame.display.set_mode((0,0))
        screen_width, screen_height = screen.get_size()
        CENTERX = screen_width / 2
        CENTERY =  screen_height/2
        card_1 = liste_choix_perso[0]
        card_2 = liste_choix_perso[1]
        card_3 = liste_choix_perso[2]

        perso_choisi = None
        while perso_choisi == None :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pass

    def choix_couleur(self, liste_joueurs) :
        pygame.display.set_caption("Tokaido - Choisissez votre couleur")

        screen = pygame.display.set_mode((0,0))
        screen_width, screen_height = screen.get_size()
        CENTERX, CENTERY = screen_width/2, screen_height/2


        title_font = pygame.font.Font(JAPON, 100)
        title = title_font.render(str(self.nom) + ", choisissez votre couleur", 1, (0,0,0))
        title_width, title_height = title.get_size()

        TITLEPOS = (CENTERX - title_width/2, 2/3 * screen_height-title_height/2)
        JETONPOSY = CENTERY - 300
        JETON_RADIUS = jeton["bleu"].get_width()/2

        bleu_rect = jeton["bleu"].get_rect()
        BLEU_POS = (1/6*screen_width - JETON_RADIUS, JETONPOSY)
        bleu_rect.center = centrage_rect(jeton["bleu"], BLEU_POS)

        jaune_rect = jeton["jaune"].get_rect()
        JAUNE_POS = (2/6*screen_width - JETON_RADIUS, JETONPOSY)
        jaune_rect.center = centrage_rect(jeton["jaune"], JAUNE_POS)

        rouge_rect = jeton["rouge"].get_rect()
        ROUGE_POS = (3/6*screen_width - JETON_RADIUS, JETONPOSY)
        rouge_rect.center = centrage_rect(jeton["rouge"], ROUGE_POS)

        vert_rect = jeton["vert"].get_rect()
        VERT_POS = (4/6*screen_width - JETON_RADIUS, JETONPOSY)
        vert_rect.center = centrage_rect(jeton["vert"], VERT_POS)

        violet_rect = jeton["violet"].get_rect()
        VIOLET_POS = (5/6*screen_width - JETON_RADIUS, JETONPOSY)
        violet_rect.center = centrage_rect(jeton["violet"], VIOLET_POS)

        taken_colors = []

        for joueur in liste_joueurs:
            taken_colors.append(joueur.couleur)

        i=0
        while True :
            clock.tick(FPS)
            screen.fill(BG_COLOR)
            screen.blit(bg, (CENTERX - bg.get_size()[0]/2, CENTERY - bg.get_size()[1]/1.5))
            bg_filter = pygame.Surface(screen.get_size())
            bg_filter.set_alpha(128)
            bg_filter.fill((253,251,248))
            screen.blit(bg_filter, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            if bleu_rect.collidepoint(pygame.mouse.get_pos()) and "bleu" not in taken_colors:
                screen.blit(jeton["hovered_bleu"], BLEU_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "bleu"
                    break

            elif "bleu" in taken_colors:
                screen.blit(jeton["taken_color"], BLEU_POS)

            else :
                screen.blit(jeton["bleu"], BLEU_POS)

            if jaune_rect.collidepoint(pygame.mouse.get_pos()) and "jaune" not in taken_colors:
                screen.blit(jeton["hovered_jaune"], JAUNE_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "jaune"
                    break

            elif "jaune" in taken_colors:
                screen.blit(jeton["taken_color"], JAUNE_POS)

            else:
                screen.blit(jeton["jaune"], JAUNE_POS)


            if rouge_rect.collidepoint(pygame.mouse.get_pos()) and "rouge" not in taken_colors:
                screen.blit(jeton["hovered_rouge"], ROUGE_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "rouge"
                    break

            elif "rouge" in taken_colors:
                screen.blit(jeton["taken_color"], ROUGE_POS)

            else:
                screen.blit(jeton["rouge"], ROUGE_POS)


            if vert_rect.collidepoint(pygame.mouse.get_pos()) and "vert" not in taken_colors:
                screen.blit(jeton["hovered_vert"], VERT_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "vert"
                    break

            elif "vert" in taken_colors:
                screen.blit(jeton["taken_color"], VERT_POS)

            else:
                screen.blit(jeton["vert"], VERT_POS)

            if violet_rect.collidepoint(pygame.mouse.get_pos()) and "violet" not in taken_colors:
                screen.blit(jeton["hovered_violet"], VIOLET_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "violet"
                    break

            elif "violet" in taken_colors:
                screen.blit(jeton["taken_color"], VIOLET_POS)

            else:
                screen.blit(jeton["violet"], VIOLET_POS)

            screen.blit(title, TITLEPOS)

            ANIMATION_DURATION = 0.5
            animation_filter = pygame.Surface(screen.get_size())
            animation_filter.fill(BG_COLOR)

            if i <= ANIMATION_DURATION * FPS and self == liste_joueurs[0]:
                animation_filter.set_alpha(255-i*255/(ANIMATION_DURATION*FPS))
                screen.blit(animation_filter, (0,0))
                i+=1

            pygame.display.flip()


def centrage_rect(surface, pos):
    return pos[0] + surface.get_size()[0]/2, pos[1] + surface.get_size()[1]/2