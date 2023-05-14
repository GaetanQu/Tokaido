import pygame
import random
from Class.Settings import *

BG_COLOR = (251,253,248)

settings = Settings()
FPS = int(settings.setting["FPS"])

JAPON = "Tokaido/Fonts/Japon.ttf"

BIGJETONSIZE = (175, 175)
LITTLEJETONSIZE = (125,125)

dims_card_de_base = 1144, 1533
div_dim_card = 3
CARDSIZE = dims_card_de_base[0]/div_dim_card, dims_card_de_base[1]/div_dim_card
DESC_MARGIN = 30

clock = pygame.time.Clock()

bg = pygame.image.load("Tokaido/Class/images/menu/bg.png")
bg = pygame.transform.scale(bg, (2*bg.get_size()[0], 2*bg.get_size()[1]))

jeton = { "bleu" : pygame.transform.smoothscale(pygame.image.load('Tokaido/Class/images/jetons/bleu.png'), BIGJETONSIZE),
          "hovered_bleu" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_bleu.png"), BIGJETONSIZE),
          "jaune" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/jaune.png"), BIGJETONSIZE),
          "hovered_jaune" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_jaune.png"), BIGJETONSIZE),
          "rouge" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/rouge.png"), BIGJETONSIZE),
          "hovered_rouge" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_rouge.png"), BIGJETONSIZE),
          "vert" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/vert.png"), BIGJETONSIZE),
          "hovered_vert" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_vert.png"), BIGJETONSIZE),
          "violet" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/violet.png"), BIGJETONSIZE),
          "hovered_violet" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/hovered_violet.png"), BIGJETONSIZE),
          "taken_color" : pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/jetons/taken_color.png"), BIGJETONSIZE)}

#perso = [nom : [desc, image, pieces]]

dico_perso = { "Chuubei" : ["Chuubei le messager\npioche une carte Rencontre lorsqu'il arrive\ndans chacun des trois Relais intermediaires", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/chuubei.png"), CARDSIZE), 4],
               "Hiroshige" : ["Hiroshige l'artiste\nprend une carte Panorama de son choix\nlorsqu'il arrive dans chacun\ndes trois Relais intermediaires", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/hiroshige.png"), CARDSIZE), 3], 
               "Hirotada" : ["A chaque arret au temple,\nHirotada le pretre se verra beni\nd'une piece offerte gratuitement au temple.", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/hirotada.png"), CARDSIZE), 8], 
               "Kinko" : ["Les cartes repas achetees par Kinko le ronin\nlui coutent une piece de moins,\nun repas coutant une piece devient gratuit", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/kinko.png"), CARDSIZE), 7], 
               "Mitsukuni" : ["Chaque carte Source Chaude\net chaque carte Accomplissement\nrapporte un point summplementaire a\nMitsukuni le vieillard", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/mitsukuni.png"), CARDSIZE), 6], 
               "Sasayakko" : ["Dans les villages,\nsi Sasayakko la geisha achete au moins deux Souvenirs,\nle moins cher des deux lui est offert", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/sasayakko.png"), CARDSIZE), 5], 
               "Satsuki" : ["Lors de son arrivee au Relais,\nSatsuki l'orpheline recoit aleatoirement\net gratuitement pour une carte repas", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/satsuki.png"), CARDSIZE), 2], 
               "Umegae" : ["Umegae la saltimbanque\ngagne un point et une piece\nlors de chaque rencontre", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/umegae.png"), CARDSIZE), 5], 
               "Yoshiyasu" : ["Lors de chaque rencontre,\nYoshiyasu le fonctionnaire choisit\nune carte Rencontre parmi deux au choix", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/yoshiyasu.png"), CARDSIZE), 9], 
               "Zen-Emon" : ["Zen-Emon le marchand\npeut acheter l'un des Souvenirs\npour une seule piece au lieu du prix indique,\nune fois par Echoppe", pygame.transform.smoothscale(pygame.image.load("Tokaido/Class/images/personnages/zen-emon.png"), CARDSIZE), 6]}


liste_perso = list(dico_perso.keys())

class Joueur:
    def __init__(self, nom, screen):
        self.screen = screen
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

        liste_choix_perso = []
        liste_keys_perso = []
        for i in range (3) :
            perso_envisageable = dico_perso[liste_perso[random.randint(0,len(liste_perso)-1)]]
            while [key for key, value in dico_perso.items() if value == perso_envisageable][0] in liste_perso_joueurs or perso_envisageable in liste_choix_perso:
                perso_envisageable = dico_perso[liste_perso[random.randint(0,len(liste_perso)-1)]]
            
            for key, value in dico_perso.items():
                if value == perso_envisageable:
                    liste_keys_perso.append(key)

            liste_choix_perso.append(perso_envisageable)

        self.screen_width, self.screen_height = self.screen.get_size()
        CENTERX, CENTERY = self.screen_width/2, self.screen_height/2

        pygame.display.set_caption("Tokaido - " + self.nom + ", choisissez votre personnage")
        card_1 = liste_choix_perso[0]
        card_2 = liste_choix_perso[1]
        card_3 = liste_choix_perso[2]

        card1_rect = card_1[1].get_rect()
        card2_rect = card_2[1].get_rect()
        card3_rect = card_3[1].get_rect()

        card_desc_font = pygame.font.Font(JAPON, 30)

        CARDPOSY = 1/2*self.screen_height - 3/4*CARDSIZE[1]
        DESCPOSY = CARDPOSY + CARDSIZE[1] + DESC_MARGIN

        CARD1_POS = (2/9*self.screen_width - CARDSIZE[0]/2, CARDPOSY)
        CARD2_POS = (1/2*self.screen_width - CARDSIZE[0]/2, CARDPOSY)
        CARD3_POS = (7/9*self.screen_width - CARDSIZE[0]/2, CARDPOSY)

        card1_rect.center = centrage_rect(card_1[1], CARD1_POS)
        card2_rect.center = centrage_rect(card_2[1], CARD2_POS)
        card3_rect.center = centrage_rect(card_3[1], CARD3_POS)

        CARD1JETON_POS = jeton_pos(CARD1_POS)
        CARD2JETON_POS = jeton_pos(CARD2_POS)
        CARD3JETON_POS = jeton_pos(CARD3_POS)

        text_zone = [pygame.Rect(CARD1_POS[0],DESCPOSY,CARDSIZE[0],70),
                     pygame.Rect(CARD2_POS[0],DESCPOSY,CARDSIZE[0],70),
                     pygame.Rect(CARD3_POS[0],DESCPOSY,CARDSIZE[0],70)]

        while True:
            clock.tick(FPS)
            self.screen.fill(BG_COLOR)
            
            self.screen.blit(bg, (CENTERX - bg.get_size()[0]/2, CENTERY - bg.get_size()[1]/1.5))
            
            bg_filter = pygame.Surface(self.screen.get_size())
            bg_filter.set_alpha(128)
            bg_filter.fill(BG_COLOR)
            self.screen.blit(bg_filter, (0,0))

            event = pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION, {'pos' : (0,0)})) #Je pense que ca peut permettre de regler les problemes

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

            self.screen.blit(card_1[1], CARD1_POS)
            self.screen.blit(card_2[1], CARD2_POS)
            self.screen.blit(card_3[1], CARD3_POS)

            if card1_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(pygame.transform.smoothscale(jeton[self.couleur], LITTLEJETONSIZE), CARD1JETON_POS)
                if event.type == pygame.MOUSEBUTTONUP:  #des fois ca bug, des fois non, je comprends pas
                    self.personnage = liste_keys_perso[0]
                    self.pieces = dico_perso[self.personnage][2]
                    break

            if card2_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(pygame.transform.smoothscale(jeton[self.couleur], LITTLEJETONSIZE), CARD2JETON_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.personnage = liste_keys_perso[1]
                    self.pieces = dico_perso[self.personnage][2]
                    break

            if card3_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(pygame.transform.smoothscale(jeton[self.couleur], LITTLEJETONSIZE), CARD3JETON_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.personnage = liste_keys_perso[2]
                    self.pieces = dico_perso[self.personnage][2]
                    break

            i=0
            for textzone in text_zone:
                x,y = textzone.midtop
                for ligne in liste_choix_perso[i][0].splitlines():
                    ligne_text = card_desc_font.render(ligne,1,(0,0,0))
                    ligne_text_size = ligne_text.get_size()
                    x,y = self.screen.blit(ligne_text, (x - ligne_text_size[0]/2,y)).midbottom
                i+=1

            self.aff_titre("personnage")

            pygame.display.flip()

    def choix_couleur(self, liste_joueurs) :
        pygame.display.set_caption("Tokaido -" + self.nom + ", choisissez votre couleur") #Le soucis du detail, meme si des fois ca bug je comprends pas pourquoi

        self.screen_width, self.screen_height = self.screen.get_size()
        CENTERX, CENTERY = self.screen_width/2, self.screen_height/2

        JETONPOSY = CENTERY - 300
        JETON_RADIUS = jeton["bleu"].get_width()/2

        bleu_rect = jeton["bleu"].get_rect()
        BLEU_POS = (1/6*self.screen_width - JETON_RADIUS, JETONPOSY)
        bleu_rect.center = centrage_rect(jeton["bleu"], BLEU_POS)

        jaune_rect = jeton["jaune"].get_rect()
        JAUNE_POS = (2/6*self.screen_width - JETON_RADIUS, JETONPOSY)
        jaune_rect.center = centrage_rect(jeton["jaune"], JAUNE_POS)

        rouge_rect = jeton["rouge"].get_rect()
        ROUGE_POS = (3/6*self.screen_width - JETON_RADIUS, JETONPOSY)
        rouge_rect.center = centrage_rect(jeton["rouge"], ROUGE_POS)

        vert_rect = jeton["vert"].get_rect()
        VERT_POS = (4/6*self.screen_width - JETON_RADIUS, JETONPOSY)
        vert_rect.center = centrage_rect(jeton["vert"], VERT_POS)

        violet_rect = jeton["violet"].get_rect()
        VIOLET_POS = (5/6*self.screen_width - JETON_RADIUS, JETONPOSY)
        violet_rect.center = centrage_rect(jeton["violet"], VIOLET_POS)

        taken_colors = []

        for joueur in liste_joueurs:
            taken_colors.append(joueur.couleur)

        i=0
        while True :
            clock.tick(FPS)
            self.screen.fill(BG_COLOR)
            self.screen.blit(bg, (CENTERX - bg.get_size()[0]/2, CENTERY - bg.get_size()[1]/1.5))
            bg_filter = pygame.Surface(self.screen.get_size())
            bg_filter.set_alpha(128)
            bg_filter.fill(BG_COLOR)
            self.screen.blit(bg_filter, (0,0))


            event = pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION, {'pos' : (0,0)}))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            if bleu_rect.collidepoint(pygame.mouse.get_pos()) and "bleu" not in taken_colors:
                self.screen.blit(jeton["hovered_bleu"], BLEU_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "bleu"
                    break

            elif "bleu" in taken_colors:
                self.screen.blit(jeton["taken_color"], BLEU_POS)

            else :
                self.screen.blit(jeton["bleu"], BLEU_POS)

            if jaune_rect.collidepoint(pygame.mouse.get_pos()) and "jaune" not in taken_colors:
                self.screen.blit(jeton["hovered_jaune"], JAUNE_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "jaune"
                    break

            elif "jaune" in taken_colors:
                self.screen.blit(jeton["taken_color"], JAUNE_POS)

            else:
                self.screen.blit(jeton["jaune"], JAUNE_POS)


            if rouge_rect.collidepoint(pygame.mouse.get_pos()) and "rouge" not in taken_colors:
                self.screen.blit(jeton["hovered_rouge"], ROUGE_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "rouge"
                    break

            elif "rouge" in taken_colors:
                self.screen.blit(jeton["taken_color"], ROUGE_POS)

            else:
                self.screen.blit(jeton["rouge"], ROUGE_POS)


            if vert_rect.collidepoint(pygame.mouse.get_pos()) and "vert" not in taken_colors:
                self.screen.blit(jeton["hovered_vert"], VERT_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "vert"
                    break

            elif "vert" in taken_colors:
                self.screen.blit(jeton["taken_color"], VERT_POS)

            else:
                self.screen.blit(jeton["vert"], VERT_POS)

            if violet_rect.collidepoint(pygame.mouse.get_pos()) and "violet" not in taken_colors:
                self.screen.blit(jeton["hovered_violet"], VIOLET_POS)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.couleur = "violet"
                    break

            elif "violet" in taken_colors:
                self.screen.blit(jeton["taken_color"], VIOLET_POS)

            else:
                self.screen.blit(jeton["violet"], VIOLET_POS)

            ANIMATION_DURATION = 0.5
            animation_filter = pygame.Surface(self.screen.get_size())
            animation_filter.fill(BG_COLOR)

            if i <= ANIMATION_DURATION * FPS and self == liste_joueurs[0]:
                animation_filter.set_alpha(255-i*255/(ANIMATION_DURATION*FPS))
                self.screen.blit(animation_filter, (0,0))
                i+=1

            self.aff_titre("couleur")

            pygame.display.flip()

    def aff_titre(self, title):
        title_font = pygame.font.Font(JAPON, 100)
        
        account = title_font.render(self.nom, 1, (200,30,30))
        account_size = account.get_size()

        title = title_font.render("choisissez votre " + title, 1, (30,30,30))
        title_width, title_height = title.get_size()
        TITLEPOS = (self.screen_width/2 - title_width/2, 4/5 * self.screen_height-title_height/2)
    
        self.screen.blit(account, (self.screen_width / 2 - account_size[0]/2, TITLEPOS[1]))
        self.screen.blit(title, (TITLEPOS[0], TITLEPOS[1] + 100))


def centrage_rect(surface, pos):
    return pos[0] + surface.get_size()[0]/2, pos[1] + surface.get_size()[1]/2

def jeton_pos(carte_pos):
    return carte_pos[0] + 5, carte_pos[1] + 5
