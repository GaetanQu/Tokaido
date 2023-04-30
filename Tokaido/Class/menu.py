from math import *
import cv2
import pygame

##########################################################################################################
##                                                                                                      ##
##C'est encore largement ameliorable, mais j'en peux plus de ce menu de mort j'y retournerais plus tard ##
##                                                                                                      ##
##########################################################################################################

"""La classe menu"""
class Menu():

    #main player = [Pseudo, Victoires, Defaites]
    def __init__(self, main_player):
        self.main_player = main_player

        """Initialisation de pygme"""
        pygame.init()
        pygame.display.init()
        pygame.font.init()

        pygame.display.set_caption("Tokaido")

        global screen
        screen = pygame.display.set_mode((0,0))

        """--Par mesure de simplicite, on met tout en global (necessaire pour passer de l'authenticator au menu et vice-versa)--"""
        #Les dimensions de l'ecran ainsi que les coordonnes du centre
        global screen_width, screen_height
        screen_width, screen_height = screen.get_size()
        
        global CENTERX, CENTERY
        CENTERX = screen_width / 2
        CENTERY = screen_height / 2
        
        #L'horloge
        global clock
        clock = pygame.time.Clock()

        #Les images
        global bg
        global BG_WIDTH, BG_HEIGHT, BG_COLOR, BG_POS
        global BG_RATIO, bg_array
        
        BG_COLOR = (251,253,248)

        bg = pygame.image.load('Tokaido/class/images/menu/bg.png')
        bg_array = pygame.surfarray.array3d(bg.convert_alpha())

        BG_WIDTH, BG_HEIGHT = bg.get_size()
        BG_RATIO = int(BG_WIDTH / BG_HEIGHT)

        BG_COLOR = (251,253,248)
        BG_POS = (CENTERX - BG_WIDTH/2 ,CENTERY - BG_HEIGHT/1.5)


        global title, hovered_title
        global title_rect, TITLE_WIDTH, TITLE_HEIGHT, TITLE_POS

        title = pygame.image.load('Tokaido/class/images/menu/title.png')
        hovered_title = pygame.image.load('Tokaido/class/images/menu/hovered_title.png')

        TITLE_WIDTH, TITLE_HEIGHT = title.get_size()
        TITLE_POS = (CENTERX - TITLE_WIDTH/2, screen_height - 2*TITLE_HEIGHT)

        title_rect = title.get_rect()
        title_rect.center = TITLE_POS[0] + TITLE_WIDTH / 2, TITLE_POS[1] + TITLE_HEIGHT / 2

        global account, back, hovered_account, hovered_back
        global account_and_back_rect, ACCOUNT_AND_BACK_WIDTH, ACCOUNT_AND_BACK_HEIGHT, ACCOUNT_POS, BACK_POS

        ACCOUNT_POS = (30, 30)
        BACK_POS = (40,40)

        account = pygame.image.load('Tokaido/class/images/menu/account.png')
        hovered_account = pygame.image.load('Tokaido/class/images/menu/hovered_account.png')

        back = pygame.image.load('Tokaido/class/images/menu/back.png')
        hovered_back = pygame.image.load('Tokaido/class/images/menu/hovered_back.png')

        ACCOUNT_AND_BACK_WIDTH, ACCOUNT_AND_BACK_HEIGHT = account.get_size()

        account_and_back_rect = account.get_rect()
        account_and_back_rect.center = ACCOUNT_POS[0] + ACCOUNT_AND_BACK_WIDTH / 2, ACCOUNT_POS[1] + ACCOUNT_AND_BACK_HEIGHT / 2
        

        global croix, hovered_croix
        global croix_rect, CROIX_WIDTH, CROIX_HEIGHT, CROIX_POS, CROIX_MARGIN

        CROIX_MARGIN = 20

        croix = pygame.image.load('Tokaido/class/images/menu/croix.png')
        hovered_croix = pygame.image.load('Tokaido/class/images/menu/hovered_croix.png')

        CROIX_WIDTH, CROIX_HEIGHT = croix.get_size()
        CROIX_POS = (screen_width - CROIX_WIDTH - CROIX_MARGIN, CROIX_MARGIN)

        croix_rect = croix.get_rect()
        croix_rect.center = CROIX_POS[0] + CROIX_WIDTH / 2, CROIX_POS[1] + CROIX_HEIGHT / 2

        #Les polices
        JAPON = 'Tokaido/Fonts/Japon.ttf'

        
        global main_player_name_surface, MAIN_PLAYER_NAME_SURFACE_POS

        ACCOUNT_NAME_MARGIN = 10
        MAIN_PLAYER_NAME_SURFACE_POS = (ACCOUNT_POS[0] + ACCOUNT_AND_BACK_WIDTH + ACCOUNT_NAME_MARGIN, ACCOUNT_POS[1] + ACCOUNT_AND_BACK_HEIGHT /4)

        main_player_name_font = pygame.font.Font(JAPON, 40)
        main_player_name_surface = main_player_name_font.render(str(self.main_player[0]), 1, (50,50,50))

        
        global MAIN_PLAYER_WINS_POS_X, MAIN_PLAYER_LOSES_POS_X
        global main_player_wins_surface, main_player_loses_surface
        global MAIN_PLAYER_WINS_SURFACE_WIDTH, MAIN_PLAYER_LOSES_SURFACE_WIDTH

        STATS_COLOR = (50,50,50)
        
        main_player_stats_font = pygame.font.Font(JAPON, 100)
        main_player_wins_surface = main_player_stats_font.render("Victoires : " + str(self.main_player[1]), 1, STATS_COLOR)
        main_player_loses_surface = main_player_stats_font.render("Defaites : " + str(self.main_player[2]), 1, STATS_COLOR)

        MAIN_PLAYER_WINS_SURFACE_WIDTH = main_player_wins_surface.get_width()
        MAIN_PLAYER_LOSES_SURFACE_WIDTH = main_player_loses_surface.get_width()

        MAIN_PLAYER_WINS_POS_X = 3/10 * screen_width - MAIN_PLAYER_WINS_SURFACE_WIDTH / 2
        MAIN_PLAYER_LOSES_POS_X = 7/10 * screen_width - MAIN_PLAYER_LOSES_SURFACE_WIDTH / 2


        
        global disconnect_surface, hovered_disconnect_surface
        global disconnect_rect, DISCONNECT_POS

        DISCONNECT_TEXT = "Changer de compte"
        DISCONNECT_MARGIN = 10
        DISCONNECT_COLOR = (70,70,70)
        HOVERED_DISCONNECT_COLOR = (0,0,0)

        disconnect_font = pygame.font.Font(JAPON, 25)
        disconnect_surface = disconnect_font.render(DISCONNECT_TEXT, 1, DISCONNECT_COLOR)
        hovered_disconnect_surface = disconnect_font.render(DISCONNECT_TEXT, 1, HOVERED_DISCONNECT_COLOR)

        DISCONNECT_WIDTH, DISCONNECT_HEIGHT = disconnect_surface.get_size()
        DISCONNECT_POS = screen_width - DISCONNECT_WIDTH - DISCONNECT_MARGIN, screen_height - DISCONNECT_HEIGHT - DISCONNECT_MARGIN

        disconnect_rect = disconnect_surface.get_rect()
        disconnect_rect.center = DISCONNECT_POS[0] + DISCONNECT_WIDTH/2, DISCONNECT_POS[1] + DISCONNECT_HEIGHT/2
        
        global PLAY_SOLO_POS
        global play_solo_surface, hovered_play_solo_surface
        global play_solo_rect
        
        global PLAY_SPLIT_POS
        global play_split_surface, hovered_play_split_surface
        global play_split_rect

        global SETTINGS_POS
        global settings_surface, hovered_settings_surface
        global settings_rect

        global PLAY_MARGIN_LEFT, PLAY_MARGIN_BETWEEN, PLAY_MARGIN_BOTTOM

        PLAY_MARGIN_LEFT = 50
        PLAY_MARGIN_BETWEEN = 10
        PLAY_MARGIN_BOTTOM = 50

        play_font = pygame.font.Font(JAPON, 50)
        PLAY_COLOR = (70,70,70)
        HOVERED_PLAY_COLOR = (150,150,150)


        SETTINGS_TEXT = "Parametres"

        settings_surface = play_font.render(SETTINGS_TEXT, 1, PLAY_COLOR)
        hovered_settings_surface = play_font.render(SETTINGS_TEXT, 1, HOVERED_PLAY_COLOR)

        SETTINGS_WIDTH, SETTINGS_HEIGHT = settings_surface.get_size()
        SETTINGS_POS = PLAY_MARGIN_LEFT, screen_height - SETTINGS_HEIGHT - PLAY_MARGIN_BOTTOM

        settings_rect = settings_surface.get_rect()
        settings_rect.center = SETTINGS_POS[0] + SETTINGS_WIDTH / 2, SETTINGS_POS[1] + SETTINGS_HEIGHT / 2


        PLAY_SPLIT_TEXT = "Jouer a plusieurs sur le meme ecran"

        play_split_surface = play_font.render(PLAY_SPLIT_TEXT, 1, PLAY_COLOR)
        hovered_play_split_surface = play_font.render(PLAY_SPLIT_TEXT, 1, HOVERED_PLAY_COLOR)

        PLAY_SPLIT_WIDTH, PLAY_SPLIT_HEIGHT = play_split_surface.get_size()
        PLAY_SPLIT_POS = PLAY_MARGIN_LEFT, SETTINGS_POS[1] - PLAY_SPLIT_HEIGHT - PLAY_MARGIN_BETWEEN

        play_split_rect = play_split_surface.get_rect()
        play_split_rect.center = PLAY_SPLIT_POS[0] + PLAY_SPLIT_WIDTH / 2, PLAY_SPLIT_POS[1] + PLAY_SPLIT_HEIGHT / 2
        

        PLAY_SOLO_TEXT = "Jouer seul"
        
        play_solo_surface = play_font.render(PLAY_SOLO_TEXT, 1, PLAY_COLOR)
        hovered_play_solo_surface = play_font.render(PLAY_SOLO_TEXT, 1, HOVERED_PLAY_COLOR)

        PLAY_SOLO_WIDTH, PLAY_SOLO_HEIGHT = play_solo_surface.get_size()
        PLAY_SOLO_POS = PLAY_MARGIN_LEFT, PLAY_SPLIT_POS[1] - PLAY_SOLO_HEIGHT - PLAY_MARGIN_BETWEEN

        play_solo_rect = play_solo_surface.get_rect()
        play_solo_rect.center = PLAY_SOLO_POS[0] + PLAY_SOLO_WIDTH/2, PLAY_SOLO_POS[1] + PLAY_SOLO_HEIGHT / 2

    def affichage_constant(self, event) :
        screen.fill(BG_COLOR)

        fake_event = pygame.event.Event(pygame.MOUSEMOTION, {'pos' : (0,0)})
        pygame.time.set_timer(fake_event, int(1000/FPS))
        #Affichage de la croix, on doit pourvoir fermer le jeu a tout instant
        if croix_rect.collidepoint(pygame.mouse.get_pos()) :
            screen.blit(hovered_croix, CROIX_POS)
            if event.type == pygame.MOUSEBUTTONUP :
                return("quit")
        else :
            screen.blit(croix, CROIX_POS)
        
        #Affichage du pseudo du joueur connecte
        screen.blit(main_player_name_surface, MAIN_PLAYER_NAME_SURFACE_POS)

    def launch(self) :
        global FPS
        FPS = 75
        while True :
            clock.tick(FPS)
            for event in pygame.event.get():

                if self.affichage_constant(event) == "quit":
                    return "quit"

                if event.type == pygame.QUIT :
                    pygame.quit()
                    return "quit"

                if event.type == pygame.MOUSEBUTTONUP :
                    if account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                        action = self.account_menu()
                        if action == "deconnexion" :
                            return "deconnexion"
                    
                        elif action == "quit" :
                            return "quit"
                    elif settings_rect.collidepoint(pygame.mouse.get_pos()):
                        settings_list = self.settings_menu()
                        FPS = settings_list[1]

                        if settings_list[0] == "quit":
                            return "quit"

                #Affichage du background
                screen.blit(bg, BG_POS)

                #Affichage du titre
                if title_rect.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(hovered_title, TITLE_POS)
                else :
                    screen.blit(title, TITLE_POS)

                #Affichage du bouton de menu de compte
                if account_and_back_rect.collidepoint(pygame.mouse.get_pos()) :
                    screen.blit(hovered_account, ACCOUNT_POS)
                else :
                    screen.blit(account, ACCOUNT_POS)

                #Affichage des boutons pour jouer
                if play_solo_rect.collidepoint(pygame.mouse.get_pos()) :
                    screen.blit(hovered_play_solo_surface, PLAY_SOLO_POS)
                else :
                    screen.blit(play_solo_surface, PLAY_SOLO_POS)

                if play_split_rect.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(hovered_play_split_surface, PLAY_SPLIT_POS)
                else :
                    screen.blit(play_split_surface, PLAY_SPLIT_POS)

                if settings_rect.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(hovered_settings_surface, SETTINGS_POS)
                else :
                    screen.blit(settings_surface, SETTINGS_POS)

                #Actualisation de l'ecran
                pygame.display.flip()

    def account_menu(self):
        pos_list = self.account_menu_transition(0, [bg, BG_POS, TITLE_POS, PLAY_SOLO_POS, PLAY_SPLIT_POS, SETTINGS_POS, (1/3 * screen_width - MAIN_PLAYER_WINS_SURFACE_WIDTH, screen_height), (3/4 * screen_width - MAIN_PLAYER_LOSES_SURFACE_WIDTH/2, screen_height)])                   #pos_list = [bg, bg_pos, title_pos, play_solo_pos, play_split_pos, main_player_wins_pos, main_player_loses_pos]
            
        while True:
            for event in pygame.event.get() :
                if self.affichage_constant(event) == "quit":
                    return "quit"
                if event.type == pygame.QUIT :
                    pygame.quit()

                if account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(hovered_back, BACK_POS)
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.account_menu_transition(1, pos_list)
                        return True
                else :
                    screen.blit(back, BACK_POS)
            
            screen.blit(pos_list[0], pos_list[1])
            screen.blit(title, pos_list[2])
            screen.blit(main_player_wins_surface, pos_list[6])
            screen.blit(main_player_loses_surface, pos_list[7])

            pygame.display.flip()

    def account_menu_transition(self, switch, pos_list):
        #Duree de l'animation en secondes
        global ANIMATION_DURATION
        ANIMATION_DURATION = 1

        bg_size = pos_list[0].get_size()

        for i in range (FPS * ANIMATION_DURATION):
            clock.tick(FPS)

            
            #J'ai aucune idee de ce que veulent dire ces fonction
            #A la base je voulais une vitesse dont la valeur valait
            #((-1)**switch * POWER * exp(-(ANIMATION_STRENGTH/(FPS * ANIMATION_DURATION) * (i - (START - (2*abs(START-(FPS*ANIMATION_DURATION)/2) * switch))))**2))
            #Par exemple la vitesse de translation des stats valait +-30*exp(-((8/60) * {(i-40) a l'allee, (i-20) au retour} ))
            #Le but etait que la vitesse fasse une symetrie centrale autour de la moitie de l'animation en fonction de sa duree et du framerate
            #Sauf que pour obtenir la position il me fallait l'integrale de cette fonction, et clairement c'etait trop dur
            #donc la fonction est devenue : ((-1)**switch * POWER * exp(-(ANIMATION_STRENGTH/(FPS * ANIMATION_DURATION) * (i - START))**2))
            #une simple symetrie axiale autour de l'axe des abcisses
            #fonction dont j'ai obtenu l'integrale avec Symbolab
            #De toute facon on est en info pas en maths

            #En verite j'avais deja fait une autre classe desormais nommee Menu1 qui fonctionnait en utilisant uniquement les vitesses mais c'est moche, vous y avez acces si vous le souhaitez
            

            #Je suis quand meme un monstre :                                                                \/ ici, on a 2.2*FPS car on veut commencer le resize de retour directement a la valeur de l'integrale de 0 a FPS de la vitesse de resize
            diff_bg_resize = (60 / FPS) * ((-1) ** switch * ((5*sqrt(pi)*FPS)/4) * erf((4/FPS) * (i - (FPS * switch))) - 2.22 * FPS * switch)
            diff_bg_translation = (0, (-1) * (60/FPS) * ((-1)**switch * -7/8 * sqrt(pi) * erf(2 * (FPS - 2*i) / FPS) * FPS)) #idem ici etc...
            diff_title_translation = (0, (-1)**switch * 50*FPS/3 * sqrt(pi)/2 * erf(i/20))
            diff_play_translation = ((60/FPS)*((-1) * (-1)**switch * 15/2 * sqrt(pi) * FPS * erf(2*i/FPS) - switch * ( 15/2 * sqrt(pi) * erf(2))), 0)
            diff_stats_translation = (0, (60/FPS) *(-(-1)**switch * 35/8 * sqrt(pi) * FPS * erf((8*(i-(2*FPS/3)+FPS/3*switch))/FPS) + 35/16 * sqrt(pi) * (erf(8/3)+erf(16/3))* FPS * switch))


            #J'avais ease_in_and_out_animation(i, POWER, STRENGTH, START, switch) = ((-1)**switch * POWER * exp(-(ANIMATION_STRENGTH/(FPS * ANIMATION_DURATION) * (i - (START - (2*abs(START-(FPS*ANIMATION_DURATION)/2) * switch))))**2))
            #Sauf que c'etait trop approximatif
            """bg_rescale = self.ease_in_and_out_animation(i, 10, 3, 0, switch)
            diff_bg_translation = (0, self.ease_in_and_out_animation(i, 7, 4, 30, switch))
            diff_title_translation = (0, self.ease_in_and_out_animation(i, -50, 3, 0, switch))
            diff_play_translation = (self.ease_in_and_out_animation(i, 15, 2, 0, switch))
            diff_stats_translation = (0, self.ease_in_and_out_animation(i, 30, 8, 40, switch))"""

            bg_scaled_size = (bg_size[0] - int(BG_RATIO * diff_bg_resize), bg_size[1] - int(diff_bg_resize))
            bg_scaled_array = cv2.resize(bg_array, bg_scaled_size[::-1], interpolation = cv2.INTER_CUBIC)
            scaled_bg = pygame.surfarray.make_surface(bg_scaled_array)
            
            #pos_list = [bg, bg_pos, title_pos, play_solo_pos, play_split_pos, settings_pos, main_player_wins_pos, main_player_loses_pos]

            bg_pos = self.translation((CENTERX - bg_scaled_size[0] / 2, CENTERY - bg_scaled_size[1] / 1.23333), diff_bg_translation)   #J'ignore pourquoi le 1.5 de base devient 1.23333 mais ca fonctionne
            title_pos = self.translation(pos_list[2], diff_title_translation)
            play_solo_pos = self.translation(pos_list[3], diff_play_translation)
            play_split_pos = self.translation(pos_list[4], diff_play_translation)
            settings_pos = self.translation(pos_list[5], diff_play_translation)
            main_player_wins_pos = self.translation(pos_list[6], diff_stats_translation)
            main_player_loses_pos = self.translation(pos_list[7], diff_stats_translation)

            for event in pygame.event.get():
                self.affichage_constant(event)
            screen.blit(scaled_bg, bg_pos)
            screen.blit(title, title_pos)
            screen.blit(play_solo_surface, play_solo_pos)
            screen.blit(play_split_surface, play_split_pos)
            screen.blit(main_player_wins_surface, main_player_wins_pos)
            screen.blit(main_player_loses_surface, main_player_loses_pos)
            screen.blit(settings_surface, settings_pos)

            if account_and_back_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(hovered_back, BACK_POS)
            else :
                screen.blit(back, BACK_POS)

            pygame.display.flip()

        return [scaled_bg, bg_pos, title_pos, play_solo_pos, play_split_pos, settings_pos, main_player_wins_pos, main_player_loses_pos]
    
    def translation (self, pos, diff_pos):
        return (pos[0] + diff_pos[0], pos[1] + diff_pos[1])

menu = Menu(["Anateg", 8, 2])
menu.launch()