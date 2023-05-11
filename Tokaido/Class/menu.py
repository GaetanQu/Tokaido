from math import *
import cv2
import pygame
import PySimpleGUI as sg
from Class.Settings import *
import Class.Authenticator

settings = Settings()

##########################################################################################################
##                                                                                                      ##
## C'est encore largement ameliorable, mais j'en peux plus de ce menu j'y retournerais plus tard (non)  ##
##                                                                                                      ##
##########################################################################################################

"""La classe menu"""
class Menu():

    #main player = [Pseudo, Victoires, Defaites]
    def __init__(self, players_list):
        self.players_list = players_list
        self.main_player = self.players_list[0]

        """Initialisation de pygme"""
        pygame.init()
        pygame.display.init()
        pygame.font.init()

        pygame.display.set_caption("Tokaido")

        self.screen = pygame.display.set_mode((0,0))

        #Les dimensions de l'ecran ainsi que les coordonnes du centre
        self.screen_width, self.screen_height = self.screen.get_size()
        
        self.CENTERX = self.screen_width / 2
        self.CENTERY = self.screen_height / 2
        
        #L'horloge
        self.clock = pygame.time.Clock()

        #Les images
        
        self.BG_COLOR = (251,253,248)
        self.bg = pygame.image.load('Tokaido/class/images/menu/bg.png')

        self.bg_array = pygame.surfarray.array3d(self.bg.convert_alpha())


        self.BG_WIDTH, self.BG_HEIGHT = self.bg.get_size()
        self.BG_RATIO = int(self.BG_WIDTH / self.BG_HEIGHT)
        
        bg_scaled_size = (int(self.BG_WIDTH * 1920 / (1.3 *self.screen_width)), int(self.BG_HEIGHT * 1080 /(1.3* self.screen_height)))
        bg_scaled_array = cv2.resize(self.bg_array, bg_scaled_size[::-1], interpolation = cv2.INTER_CUBIC)
        self.bg = pygame.surfarray.make_surface(bg_scaled_array)

        self.BG_WIDTH, self.BG_HEIGHT = self.bg.get_size()

        self.BG_POS = (self.CENTERX - self.BG_WIDTH/2 ,self.CENTERY - self.BG_HEIGHT/1.5)


        self.title = pygame.image.load('Tokaido/class/images/menu/title.png')
        self.hovered_title = pygame.image.load('Tokaido/class/images/menu/hovered_title.png')

        TITLE_WIDTH, TITLE_HEIGHT = self.title.get_size()
        self.TITLE_POS = (self.CENTERX - TITLE_WIDTH/2, self.screen_height - 2*TITLE_HEIGHT)

        self.title_rect = self.title.get_rect()
        self.title_rect.center= self.TITLE_POS[0] + TITLE_WIDTH / 2, self.TITLE_POS[1] + TITLE_HEIGHT / 2

        self.ACCOUNT_POS = (30, 30)
        self.BACK_POS = (40,40)

        self.account = pygame.image.load('Tokaido/class/images/menu/account.png')
        self.hovered_account = pygame.image.load('Tokaido/class/images/menu/hovered_account.png')

        self.back = pygame.image.load('Tokaido/class/images/menu/back.png')
        self.hovered_back = pygame.image.load('Tokaido/class/images/menu/hovered_back.png')

        ACCOUNT_AND_BACK_WIDTH, ACCOUNT_AND_BACK_HEIGHT = self.account.get_size()

        self.account_and_back_rect = self.account.get_rect()
        self.account_and_back_rect.center = self.ACCOUNT_POS[0] + ACCOUNT_AND_BACK_WIDTH / 2, self.ACCOUNT_POS[1] + ACCOUNT_AND_BACK_HEIGHT / 2
        

        CROIX_MARGIN = 20

        self.croix = pygame.image.load('Tokaido/class/images/menu/croix.png')
        self.hovered_croix = pygame.image.load('Tokaido/class/images/menu/hovered_croix.png')

        CROIX_WIDTH, CROIX_HEIGHT = self.croix.get_size()
        self.CROIX_POS = (self.screen_width - CROIX_WIDTH - CROIX_MARGIN, CROIX_MARGIN)

        self.croix_rect = self.croix.get_rect()
        self.croix_rect.center = self.CROIX_POS[0] + CROIX_WIDTH / 2, self.CROIX_POS[1] + CROIX_HEIGHT / 2

        #Les polices
        JAPON = 'Tokaido/Fonts/Japon.ttf'

        ACCOUNT_NAME_MARGIN = 10
        self.MAIN_PLAYER_NAME_SURFACE_POS = (self.ACCOUNT_POS[0] + ACCOUNT_AND_BACK_WIDTH + ACCOUNT_NAME_MARGIN, self.ACCOUNT_POS[1] + ACCOUNT_AND_BACK_HEIGHT /4)

        main_player_name_font = pygame.font.Font(JAPON, 40)
        self.main_player_name_surface = main_player_name_font.render(str(self.main_player[0]), 1, (50,50,50))


        STATS_COLOR = (50,50,50)
        
        main_player_stats_font = pygame.font.Font(JAPON, 100)
        self.main_player_wins_surface = main_player_stats_font.render("Victoires : " + str(self.main_player[1]), 1, STATS_COLOR)
        self.main_player_loses_surface = main_player_stats_font.render("Defaites : " + str(self.main_player[2]), 1, STATS_COLOR)

        self.MAIN_PLAYER_WINS_SURFACE_WIDTH = self.main_player_wins_surface.get_width()
        self.MAIN_PLAYER_LOSES_SURFACE_WIDTH = self.main_player_loses_surface.get_width()

        self.MAIN_PLAYER_WINS_POS_X = 3/10 * self.screen_width - self.MAIN_PLAYER_WINS_SURFACE_WIDTH / 2
        self.MAIN_PLAYER_LOSES_POS_X = 7/10 * self.screen_width - self.MAIN_PLAYER_LOSES_SURFACE_WIDTH / 2


        DISCONNECT_TEXT = "Changer de compte"
        DISCONNECT_MARGIN = 10
        DISCONNECT_COLOR = (70,70,70)
        HOVERED_DISCONNECT_COLOR = (0,0,0)

        disconnect_font = pygame.font.Font(JAPON, 25)
        self.disconnect_surface = disconnect_font.render(DISCONNECT_TEXT, 1, DISCONNECT_COLOR)
        self.hovered_disconnect_surface = disconnect_font.render(DISCONNECT_TEXT, 1, HOVERED_DISCONNECT_COLOR)

        DISCONNECT_WIDTH, DISCONNECT_HEIGHT = self.disconnect_surface.get_size()
        self.DISCONNECT_POS = self.screen_width - DISCONNECT_WIDTH - DISCONNECT_MARGIN, self.screen_height - DISCONNECT_HEIGHT - DISCONNECT_MARGIN

        self.disconnect_rect = self.disconnect_surface.get_rect()
        self.disconnect_rect.center = self.DISCONNECT_POS[0] + DISCONNECT_WIDTH/2, self.DISCONNECT_POS[1] + DISCONNECT_HEIGHT/2

        PLAY_MARGIN_LEFT = 50
        PLAY_MARGIN_BETWEEN = 10
        PLAY_MARGIN_BOTTOM = 50

        play_font = pygame.font.Font(JAPON, 50)
        FONT_COLOR = (70,70,70)
        HOVERED_FONT_COLOR = (150,150,150)


        SETTINGS_TEXT = "Parametres"

        self.settings_surface = play_font.render(SETTINGS_TEXT, 1, FONT_COLOR)
        self.hovered_settings_surface = play_font.render(SETTINGS_TEXT, 1, HOVERED_FONT_COLOR)

        SETTINGS_WIDTH, SETTINGS_HEIGHT = self.settings_surface.get_size()
        self.SETTINGS_POS = PLAY_MARGIN_LEFT, self.screen_height - SETTINGS_HEIGHT - PLAY_MARGIN_BOTTOM

        self.settings_rect = self.settings_surface.get_rect()
        self.settings_rect.center = self.SETTINGS_POS[0] + SETTINGS_WIDTH / 2, self.SETTINGS_POS[1] + SETTINGS_HEIGHT / 2


        PLAY_SPLIT_TEXT = "Jouer a plusieurs sur le meme ecran"

        self.play_split_surface = play_font.render(PLAY_SPLIT_TEXT, 1, FONT_COLOR)
        self.hovered_play_split_surface = play_font.render(PLAY_SPLIT_TEXT, 1, HOVERED_FONT_COLOR)

        PLAY_SPLIT_WIDTH, PLAY_SPLIT_HEIGHT = self.play_split_surface.get_size()
        self.PLAY_SPLIT_POS = PLAY_MARGIN_LEFT, self.SETTINGS_POS[1] - PLAY_SPLIT_HEIGHT - PLAY_MARGIN_BETWEEN

        self.play_split_rect = self.play_split_surface.get_rect()
        self.play_split_rect.center = self.PLAY_SPLIT_POS[0] + PLAY_SPLIT_WIDTH / 2, self.PLAY_SPLIT_POS[1] + PLAY_SPLIT_HEIGHT / 2
        

        PLAY_SOLO_TEXT = "Jouer seul"
        
        self.play_solo_surface = play_font.render(PLAY_SOLO_TEXT, 1, FONT_COLOR)
        self.hovered_play_solo_surface = play_font.render(PLAY_SOLO_TEXT, 1, HOVERED_FONT_COLOR)

        PLAY_SOLO_WIDTH, PLAY_SOLO_HEIGHT = self.play_solo_surface.get_size()
        self.PLAY_SOLO_POS = PLAY_MARGIN_LEFT, self.PLAY_SPLIT_POS[1] - PLAY_SOLO_HEIGHT - PLAY_MARGIN_BETWEEN

        self.play_solo_rect = self.play_solo_surface.get_rect()
        self.play_solo_rect.center = self.PLAY_SOLO_POS[0] + PLAY_SOLO_WIDTH/2, self.PLAY_SOLO_POS[1] + PLAY_SOLO_HEIGHT / 2


        SPLIT_PLAYER_NUMBER_HEIGHT = 50
        SPLIT_PLAYER_NUMBER_WIDTH = 50

        PLAY_SPLIT_MARGIN = 30
        SPLIT_PLAYER_NUMBER_MARGIN = 10

        self.SPLIT_PLAYER_2_POS = self.PLAY_SPLIT_POS[0] + PLAY_SPLIT_WIDTH + PLAY_SPLIT_MARGIN, self.PLAY_SPLIT_POS[1] + PLAY_SPLIT_HEIGHT/2 - SPLIT_PLAYER_NUMBER_HEIGHT/3
        self.SPLIT_PLAYER_3_POS = self.SPLIT_PLAYER_2_POS[0] + SPLIT_PLAYER_NUMBER_WIDTH + SPLIT_PLAYER_NUMBER_MARGIN, self.SPLIT_PLAYER_2_POS[1]
        self.SPLIT_PLAYER_4_POS = self.SPLIT_PLAYER_3_POS[0] + SPLIT_PLAYER_NUMBER_WIDTH + SPLIT_PLAYER_NUMBER_MARGIN, self.SPLIT_PLAYER_3_POS[1]
        self.SPLIT_PLAYER_5_POS = self.SPLIT_PLAYER_4_POS[0] + SPLIT_PLAYER_NUMBER_WIDTH + SPLIT_PLAYER_NUMBER_MARGIN, self.SPLIT_PLAYER_4_POS[1]

        split_player_number_font = pygame.font.Font(JAPON, SPLIT_PLAYER_NUMBER_HEIGHT)
        
        self.split_player_2 = split_player_number_font.render("2", 1, FONT_COLOR)
        self.split_player_3 = split_player_number_font.render("3", 1,  FONT_COLOR)
        self.split_player_4 = split_player_number_font.render("4", 1, FONT_COLOR)
        self.split_player_5 = split_player_number_font.render("5", 1, FONT_COLOR)

        self.hovered_split_player_2 = split_player_number_font.render("2", 1, HOVERED_FONT_COLOR)
        self.hovered_split_player_3 = split_player_number_font.render("3", 1, HOVERED_FONT_COLOR)
        self.hovered_split_player_4 = split_player_number_font.render("4", 1, HOVERED_FONT_COLOR)
        self.hovered_split_player_5 = split_player_number_font.render("5", 1, HOVERED_FONT_COLOR)


        self.split_player_2_rectangle = pygame.Rect(0,0,SPLIT_PLAYER_NUMBER_WIDTH, SPLIT_PLAYER_NUMBER_HEIGHT)
        self.split_player_2_rectangle.center = self.SPLIT_PLAYER_2_POS[0] + SPLIT_PLAYER_NUMBER_WIDTH / 2, self.SPLIT_PLAYER_2_POS[1] + SPLIT_PLAYER_NUMBER_HEIGHT / 2

        self.split_player_3_rectangle = pygame.Rect(0,0,SPLIT_PLAYER_NUMBER_WIDTH, SPLIT_PLAYER_NUMBER_HEIGHT)
        self.split_player_3_rectangle.center = self.SPLIT_PLAYER_3_POS[0] + SPLIT_PLAYER_NUMBER_WIDTH / 2, self.SPLIT_PLAYER_3_POS[1] + SPLIT_PLAYER_NUMBER_HEIGHT / 2

        self.split_player_4_rectangle = pygame.Rect(0,0,SPLIT_PLAYER_NUMBER_WIDTH, SPLIT_PLAYER_NUMBER_HEIGHT)
        self.split_player_4_rectangle.center = self.SPLIT_PLAYER_4_POS[0] + SPLIT_PLAYER_NUMBER_WIDTH / 2, self.SPLIT_PLAYER_4_POS[1] + SPLIT_PLAYER_NUMBER_HEIGHT / 2

        self.split_player_5_rectangle = pygame.Rect(0,0,SPLIT_PLAYER_NUMBER_WIDTH, SPLIT_PLAYER_NUMBER_HEIGHT)
        self.split_player_5_rectangle.center = self.SPLIT_PLAYER_5_POS[0] + SPLIT_PLAYER_NUMBER_WIDTH / 2, self.SPLIT_PLAYER_5_POS[1] + SPLIT_PLAYER_NUMBER_HEIGHT / 2

    def launch(self) :
        global FPS
        FPS = int(settings.setting["FPS"])
        while True :
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if self.affichage_constant_avec_interaction(event) == "quit":
                    return "Quit"

                if event.type == pygame.QUIT :
                    pygame.quit()
                    return "quit"

                if event.type == pygame.MOUSEBUTTONUP :
                    if self.account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                        action = self.account_menu()
                        if action == "deconnexion" :
                            return "Deconnexion"
                    
                        elif action == "quit" :
                            return "Quit"
                    elif self.settings_rect.collidepoint(pygame.mouse.get_pos()):
                        settings.menu()
                        FPS = int(settings.setting["FPS"])

                    elif self.play_solo_rect.collidepoint(pygame.mouse.get_pos()):
                        return"Solo"

                    elif self.play_split_rect.collidepoint(pygame.mouse.get_pos()):
                        nb_joueurs = self.play_split_menu()
                        if nb_joueurs == "quit":
                            return "Quit"
                        elif nb_joueurs == "account":
                            action = self.account_menu()
                            if action == "deconnexion": #<<< Je sais c'est moche mais ca fonctionne, et puis de toute facon j'ai deja perdu trop de temps a vouloir faire un truc prorpe qui au final est pas si propre
                                return"Deconnexion"

            #Affichage du background
            self.screen.blit(self.bg, self.BG_POS)

            #Affichage du titre
            if self.title_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_title, self.TITLE_POS)
            else :
                self.screen.blit(self.title, self.TITLE_POS)

            #Affichage du bouton de menu de compte
            if self.account_and_back_rect.collidepoint(pygame.mouse.get_pos()) :
                self.screen.blit(self.hovered_account, self.ACCOUNT_POS)
            else :
                self.screen.blit(self.account, self.ACCOUNT_POS)

            #Affichage des boutons pour jouer
            if self.play_solo_rect.collidepoint(pygame.mouse.get_pos()) :
                self.screen.blit(self.hovered_play_solo_surface, self.PLAY_SOLO_POS)
            else :
                self.screen.blit(self.play_solo_surface, self.PLAY_SOLO_POS)

            if self.play_split_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_play_split_surface, self.PLAY_SPLIT_POS)
            else :
                self.screen.blit(self.play_split_surface, self.PLAY_SPLIT_POS)

            if self.settings_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_settings_surface, self.SETTINGS_POS)
            else :
                self.screen.blit(self.settings_surface, self.SETTINGS_POS)

            self.affichage_constant()
            #Actualisation de l'ecran
            pygame.display.flip()

    def account_menu(self):
        pos_list = self.account_menu_transition(0, [self.bg, self.BG_POS, self.TITLE_POS, self.PLAY_SOLO_POS, self.PLAY_SPLIT_POS, self.SETTINGS_POS, (self.MAIN_PLAYER_WINS_POS_X, self.screen_height), (self.MAIN_PLAYER_LOSES_POS_X, self.screen_height)])                   #pos_list = [bg, bg_pos, title_pos, play_solo_pos, play_split_pos, main_player_wins_pos, main_player_loses_pos]
            
        while True:
            for event in pygame.event.get() :
                if self.affichage_constant_avec_interaction(event) == "quit":
                    return "quit"
                if event.type == pygame.QUIT :
                    pygame.quit()

                if self.account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                    self.screen.blit(self.hovered_back, self.BACK_POS)
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos_list = self.account_menu_transition(1, pos_list)
                        return True

                else :
                    self.screen.blit(self.back, self.BACK_POS)
                
                if self.disconnect_rect.collidepoint(pygame.mouse.get_pos()):
                    self.screen.blit(self.hovered_disconnect_surface, self.DISCONNECT_POS)
                    if event.type == pygame.MOUSEBUTTONUP :
                        pygame.quit()
                        return "deconnexion"
                else :
                    self.screen.blit(self.disconnect_surface, self.DISCONNECT_POS)
            
            self.screen.blit(pos_list[0], pos_list[1])
            self.screen.blit(self.title, pos_list[2])
            self.screen.blit(self.main_player_wins_surface, pos_list[6])
            self.screen.blit(self.main_player_loses_surface, pos_list[7])

            self.affichage_constant()

            pygame.display.flip()

    def account_menu_transition(self, switch, pos_list):
        #Duree de l'animation en secondes
        global ANIMATION_DURATION
        ANIMATION_DURATION = 1

        bg_size = pos_list[0].get_size()
                                                 #\/ je ne sais pas pourquoi si je ne mets pas ce "+2" au retour l'animation ne se fait pas pleinement
        for i in range (FPS * ANIMATION_DURATION):
            self.clock.tick(FPS)

            #J'en ai bave a faire les animations, a la base je comptais partir sur la vitesse : 
            #J'avais ease_in_and_out_animation(i, POWER, STRENGTH, START, switch) = ((-1)**switch * POWER * exp(-(ANIMATION_STRENGTH/(FPS * ANIMATION_DURATION) * (i - (START - (2*abs(START-(FPS*ANIMATION_DURATION)/2) * switch))))**2))
            #Sauf que c'etait trop approximatif
            """bg_rescale = self.ease_in_and_out_animation(i, 10, 3, 0, switch)
            diff_bg_translation = (0, self.ease_in_and_out_animation(i, 7, 4, 30, switch))
            diff_title_translation = (0, self.ease_in_and_out_animation(i, -50, 3, 0, switch))
            diff_play_translation = (self.ease_in_and_out_animation(i, 15, 2, 0, switch))
            diff_stats_translation = (0, self.ease_in_and_out_animation(i, 30, 8, 40, switch))"""
            

            #donc j'ai mis au point un truc toujours un peu approximatif mais au moins on peut faire machine arriere facilement : j'ai integre les fonctions a l'aide de wolframalpha et j'ai adapte le truc pour etre compatible avec n'importe quel framerate
            diff_bg_resize = (60 / FPS) * ((-1) ** switch * ((5*sqrt(pi)*FPS)/4) * erf((4/FPS) * (i - (FPS * switch))) - 2.22 * FPS * switch)
            diff_bg_translation = (0, (-1) * (60/FPS) * ((-1)**switch * -7/8 * sqrt(pi) * erf(2 * (FPS - 2*i) / FPS) * FPS)) #idem ici etc...
            diff_title_translation = (0, (-1)**switch * 50*FPS/3 * sqrt(pi)/2 * erf(i/20))
            diff_play_translation = ((60/FPS)*((-1) * (-1)**switch * 15/2 * sqrt(pi) * FPS * erf(2*i/FPS) - switch * ( 15/2 * sqrt(pi) * erf(2))), 0)
            diff_stats_translation = (0, (60/FPS) *(-(-1)**switch * 35/8 * sqrt(pi) * FPS * erf((8*(i-(2*FPS/3)+FPS/3*switch))/FPS) + 35/16 * sqrt(pi) * (erf(8/3)+erf(16/3))* FPS * switch))


            bg_scaled_size = (bg_size[0] - int(self.BG_RATIO * diff_bg_resize), bg_size[1] - int(diff_bg_resize))
            bg_scaled_array = cv2.resize(self.bg_array, bg_scaled_size[::-1], interpolation = cv2.INTER_CUBIC)
            scaled_bg = pygame.surfarray.make_surface(bg_scaled_array)
            
            #pos_list = [bg, bg_pos, title_pos, play_solo_pos, play_split_pos, settings_pos, main_player_wins_pos, main_player_loses_pos]

            bg_pos = self.translation((self.CENTERX - bg_scaled_size[0] / 2, self.CENTERY - bg_scaled_size[1] / 1.23333), diff_bg_translation)   #J'ignore pourquoi le 1.5 de base devient 1.23333 mais ca fonctionne on garde comme ca
            title_pos = self.translation(pos_list[2], diff_title_translation)
            play_solo_pos = self.translation(pos_list[3], diff_play_translation)
            play_split_pos = self.translation(pos_list[4], diff_play_translation)
            settings_pos = self.translation(pos_list[5], diff_play_translation)
            main_player_wins_pos = self.translation(pos_list[6], diff_stats_translation)
            main_player_loses_pos = self.translation(pos_list[7], diff_stats_translation)

            for event in pygame.event.get():
                self.affichage_constant_avec_interaction(event)
            self.screen.blit(scaled_bg, bg_pos)
            self.screen.blit(self.title, title_pos)
            self.screen.blit(self.play_solo_surface, play_solo_pos)
            self.screen.blit(self.play_split_surface, play_split_pos)
            self.screen.blit(self.main_player_wins_surface, main_player_wins_pos)
            self.screen.blit(self.main_player_loses_surface, main_player_loses_pos)
            self.screen.blit(self.settings_surface, settings_pos)

            if self.account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_back, self.BACK_POS)
            else :
                self.screen.blit(self.back, self.BACK_POS)

            self.affichage_constant()
            pygame.display.flip()

        return [scaled_bg, bg_pos, title_pos, play_solo_pos, play_split_pos, settings_pos, main_player_wins_pos, main_player_loses_pos]

    def play_split_menu(self):
        while True :
            FPS = int(settings.setting["FPS"])
            self.clock.tick(FPS)
            for event in pygame.event.get() :

                #On verifie si l'utilisateur a deja ferme le programme
                if ["Closed", None, None] in self.players_list:
                    self.players_list = [self.main_player]

                if self.affichage_constant_avec_interaction(event) == "quit":
                    return "quit"

                if event.type == pygame.MOUSEBUTTONUP :
                    if self.account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                        return "account"
                    #On teste le nombre de joueurs
                    elif self.split_player_2_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.players_list = self.is_connected(Class.Authenticator.auth(), self.players_list)
                        return ("Split", self.players_list)

                    elif self.split_player_3_rectangle.collidepoint(pygame.mouse.get_pos()):
                        for i in range (2):
                            self.players_list = self.is_connected(Class.Authenticator.auth(), self.players_list)
                        print(self.players_list)
                        return ("Split", self.players_list)

                    elif self.split_player_4_rectangle.collidepoint(pygame.mouse.get_pos()):
                        for i in range (3):
                            self.players_list = self.is_connected(Class.Authenticator.auth(), self.players_list)
                        return ("Split", self.players_list)

                    elif self.split_player_5_rectangle.collidepoint(pygame.mouse.get_pos()):
                        for i in range (4):
                            self.players_list = self.is_connected(Class.Authenticator.auth(), self.players_list)
                        return ("Split", self.players_list)

                    elif self.settings_rect.collidepoint(pygame.mouse.get_pos()):
                        settings.menu()
                        FPS = int(settings.setting["FPS"])

                    else :
                        return None
            
            #Affichage des differents choix possible pour le nombre de joueurs
            if self.split_player_2_rectangle.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_split_player_2, self.SPLIT_PLAYER_2_POS)
            else:
                self.screen.blit(self.split_player_2, self.SPLIT_PLAYER_2_POS)

            if self.split_player_3_rectangle.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_split_player_3, self.SPLIT_PLAYER_3_POS)
            else:
                self.screen.blit(self.split_player_3, self.SPLIT_PLAYER_3_POS)

            if self.split_player_4_rectangle.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_split_player_4, self.SPLIT_PLAYER_4_POS)
            else:
                self.screen.blit(self.split_player_4, self.SPLIT_PLAYER_4_POS)

            if self.split_player_5_rectangle.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_split_player_5, self.SPLIT_PLAYER_5_POS)
            else:
                self.screen.blit(self.split_player_5, self.SPLIT_PLAYER_5_POS)

            #Affichage du background
            self.screen.blit(self.bg, self.BG_POS)

            #Affichage du titre
            if self.title_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_title, self.TITLE_POS)
            else :
                self.screen.blit(self.title, self.TITLE_POS)

            #Affichage du bouton de menu de compte
            if self.account_and_back_rect.collidepoint(pygame.mouse.get_pos()) :
                self.screen.blit(self.hovered_account, self.ACCOUNT_POS)
            else :
                self.screen.blit(self.account, self.ACCOUNT_POS)

            #Affichage des boutons pour jouer
            if self.play_solo_rect.collidepoint(pygame.mouse.get_pos()) :
                self.screen.blit(self.hovered_play_solo_surface, self.PLAY_SOLO_POS)
            else :
                self.screen.blit(self.play_solo_surface, self.PLAY_SOLO_POS)

            if self.play_split_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_play_split_surface, self.PLAY_SPLIT_POS)
            else :
                self.screen.blit(self.play_split_surface, self.PLAY_SPLIT_POS)

            if self.settings_rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.hovered_settings_surface, self.SETTINGS_POS)
            else :
                self.screen.blit(self.settings_surface, self.SETTINGS_POS)

            self.affichage_constant()
            #Actualisation de l'ecran
            pygame.display.flip()

    def is_connected(self, ID, ID_list):
        while ID in ID_list and ID[0] != "Invite":
            sg.popup("Cet utilisateur est deja connecte !")
            ID = Class.Authenticator.auth()
        ID_list.append(ID)
        return ID_list

    def translation (self, pos, diff_pos):
        return (pos[0] + diff_pos[0], pos[1] + diff_pos[1])

    def affichage_constant(self) : #Ca parait inutile mais ca permet une meilleure evolutivite du programme
        #Affichage du pseudo du joueur connecte
        self.screen.blit(self.main_player_name_surface, self.MAIN_PLAYER_NAME_SURFACE_POS)
        
    def affichage_constant_avec_interaction(self, event):
        fake_event = pygame.event.Event(pygame.MOUSEMOTION, {'pos' : (0,0)})
        pygame.time.set_timer(fake_event, int(1000/FPS))

        self.screen.fill(self.BG_COLOR)  #Oui il n'y a pas d'interaction avec le BG mais c'est plus pratique de le mettre la
        
        #Affichage de la croix, on doit pourvoir fermer le jeu a tout instant

        if self.croix_rect.collidepoint(pygame.mouse.get_pos()) :
            self.screen.blit(self.hovered_croix, self.CROIX_POS)
            if event.type == pygame.MOUSEBUTTONUP :
                pygame.quit()
                return("quit")
        else :
            self.screen.blit(self.croix, self.CROIX_POS)