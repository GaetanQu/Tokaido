"""
Ce fichier contient l'authentificateur. Les donnees seront enregistrees sur un fichier .csv et l'authificateur sera affiche via PySimpleGUI
Il permettra de se connecter ou de creer un compte
En plus de saisir des infomations dans le .csv, il retournera une liste contenant le pseudo du joueur ainsi que ses statistiques afin de les afficher dans le menu

On vous l'accorde, il faudrait une cle de cryptage du mot de passe
"""

import PySimpleGUI as sg
import csv
import random

csv_directory = "Tokaido/Class/users.csv"

invite_adj_list = ["Big", "Huge", "Little", "Dark", "Evil", "Emo", "Invincible", "Weird", "Stinky", "Short", "Super", "Wise", "Awesome"] #On voulait rire un peu 
invite_name_list = ["Kid", "Cat", "Boy", "Girl", "Combat_Helicopter", "Dog", "Tree", "Weirdo", "Gangsta", "Grandmother", "Dwarf", "Walmart_bag", "Unicorn", "Sensei", "Macron"]

#Defnition du theme de PySimpleGUI
sg.theme('GrayGrayGray')

#Creation du layout de la fenetre de connexion
login_title = [[sg.Text("Connectez-vous pour jouer au Tokaido !", font = ("Arial", 20))]]
login_lcol = sg.Column([[sg.Text("Nom d'utilisateur")],
                        [sg.Text("Mot de passe")]])
login_rcol = sg.Column([[sg.InputText(key="-ID-")],
                        [sg.InputText(key="-MDP-", password_char="*")]])
login_buttons = [[sg.Button("Jouer en tant qu'invite"), sg.Button("Connexion", bind_return_key = True), sg.Button("Creer un compte")]]

#Creation de la fenetre de connexion
login_window = sg.Window("Connectez-vous", [[login_title],[login_lcol, login_rcol], [sg.Text("Saisissez vos identifiants", key="-WRONG-")], login_buttons], finalize=True)

#Creation du layout de la fenetre d'inscription
register_title = [[sg.Text("S'inscrire", font = ("Arial", 20))]]
register_lcol = sg.Column([[sg.Text("Nom d'utilisateur")],
                           [sg.Text("Mot de passe")],
                           [sg.Text("Confirmation du mot de passe")]])
register_rcol = sg.Column([[sg.InputText(key="-NEWID-")],
                           [sg.InputText(key="-NEWMDP-", password_char="*")],
                           [sg.InputText(key="-MDPCONFIRM-", password_char="*")]])
register_wrong = [[sg.Text("", key="-NEWWRONG-")]]
register_buttons = [[sg.Button("Creer un compte et me connecter",bind_return_key = True), sg.Button("J'ai deja un compte, me connecter")]]

#Creation de la fenetre d'inscription
register_window = sg.Window("Insrcivez-vous", [[register_title], [register_lcol, register_rcol],[register_wrong], [register_buttons]], finalize=True)

#Comme on ne s'inscrit qu'une fois, on affiche par defaut la fenetre de connexion, et donc on cache la fenetre d'inscription
register_window.hide()

#Definition de la classe Auth a appeler dans le programme principal
def auth() :

    #Importation des donnees du fichier csv
    with open(csv_directory, mode = "r") as file :
        filereader = csv.reader(file, delimiter=';')
        user = {}
        for ligne in filereader :
            user[ligne[0]] = ligne
        file.close()

    login_window.un_hide()
    login_window["-MDP-"].update("")
    login_window["-ID-"].update("")
    login_window["-WRONG-"].update("Saisissez vos identifiants")

    register_window["-NEWID-"].update("")
    register_window["-NEWMDP-"].update("")
    register_window["-MDPCONFIRM-"].update("")
    register_window["-NEWWRONG-"].update("")

    while True :
        window, event, values = sg.read_all_windows()

        #L'utilisateur ne se connecte pas
        if event == sg.WINDOW_CLOSED:
            player = ["Closed", None, None]
            break

        #Jouer en tant qu'invite
        if window == login_window and event == "Jouer en tant qu'invite":
            invite_adj = invite_adj_list[random.randint(0, len(invite_adj_list)-1)]
            invite_name = invite_name_list[random.randint(0, len(invite_name_list)-1)]
            player = [invite_adj + "_" + invite_name + " " + str(random.randint(0,100)), 0, 0]
            sg.popup("Bienvenue " + player[0] + " !")
            break

        #Connexion
        if window == login_window and event == "Connexion":
            if values["-ID-"].lower() in user and values["-MDP-"] == user[values["-ID-"].lower()][1] :
                ID = values["-ID-"].lower()
                player = [user[ID][0][0].upper()+user[ID][0][1::].lower(), user[ID][2], user[ID][3]]
                break
            else :
                window["-WRONG-"].update("Identifiant ou mot de passe incorrect")

        #Inscription
        if window == register_window and event == "Creer un compte et me connecter":

            #Verification que l'utilisateur n'est pas deja enregistre
            if values["-NEWID-"].lower() in user :
                window["-NEWWRONG-"].update("Cet utilisateur est deja enregistre")

            #Verification de l'exactitude du mot de passe
            elif values["-NEWMDP-"] != values["-MDPCONFIRM-"] :
                window["-NEWWRONG-"].update("Les mots de passe ne correspondent pas")

            #Ajout de l'utilisateur si tout est bon
            else:
                with open(csv_directory, mode = "a", newline = "") as file :
                    filewriter = csv.writer(file, delimiter = ";")
                    filewriter.writerow([str(values["-NEWID-"].lower()), str(values["-NEWMDP-"]), 0, 0])
                    file.close()
                    #L'utilisateur aura pour donnees de victoire et de defaites 0, car il vient de s'inscrire
                    player = [values["-NEWID-"][0].upper()+values["-NEWID-"][1::].lower(), 0, 0]
                break

        #Passage de la fenetre de connexion a la fenetre d'inscription
        if window == login_window and event == "Creer un compte" :
            login_window.hide()
            register_window.un_hide()

        #Passage de la fenetre d'inscription a la fenetre de connexion
        if window == register_window and event == "J'ai deja un compte, me connecter" :
            login_window.un_hide()
            register_window.hide()

    #Fermeture des fenetres
    login_window.hide()
    register_window.hide()    

    return player
