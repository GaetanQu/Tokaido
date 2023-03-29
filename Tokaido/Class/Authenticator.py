#Ce fichier contient l'authentificateur. Les donnees seront enregistrees sur un fichier .csv et l'authificateur sera affiche via PySimpleGUI
import PySimpleGUI as sg
import csv

#Importation des donnees du fichier csv
with open("tests/users.csv", mode = "r") as file :
    filereader = csv.reader(file, delimiter=';')
    user = {}
    for ligne in filereader :
        user[ligne[0]] = ligne
    file.close()

#Defnition du theme de PySimpleGUI
sg.theme('GrayGrayGray')

#Creation du layout de la fenetre de connexion
login_layout = [
    [sg.Text("Identifiez vous pour jouer au Tokaido !", font = ('Comic Sans MS',20))],
    [sg.Text("")],
    [sg.Text("Nom d'utilisateur : "), sg.InputText(key = "-ID-")],
    [sg.Text("Mot de pase :       "), sg.InputText(key = "-MDP-")],
    [sg.Button("OK"), sg.Text("", key = "-WRONG-")],
    [sg.Button("Creer un compte")]
    ]
login_window = sg.Window("Connectez-vous", login_layout, finalize=True)

#Creation du layout de la fenetre d'inscription
register_layout = [
    [sg.Text("Creez un compte", font = ("Arial", 20))],
    [sg.Text("")],
    [sg.Text("Nom d'utilisateur : "), sg.InputText(key = "-NEWID-")],
    [sg.Text("Mot de passe :      "), sg.InputText(key = "-NEWMDP-")],
    [sg.Text("Confirmation mdp :  "), sg.InputText(key = "-MDPCONFIRM-")],
    [sg.Text("", key = "-NEWWRONG-")],
    [sg.Button("Creer mon compte et me connecter"), sg.Button("J'ai deja un compte, me connecter")],
    ]
register_window = sg.Window("Insrcivez-vous", register_layout, finalize=True)
#Comme on ne s'inscrit qu'une fois, on affiche par defaut la fenetre de connexion, et donc on cache la fenetre d'inscription
register_window.hide()

#Definition de la classe Auth a appeler dans le programme principal
def auth() :
    while True :
        window, event, values = sg.read_all_windows()
        if event == sg.WINDOW_CLOSED :
            break

        #Connexion
        if window == login_window and event == "OK" :
            if values["-ID-"] in user and values["-MDP-"] == user[values["-ID-"]][1] :
                break
            else :
                window["-WRONG-"].update("ID ou MDP incorrect")

        #Inscription
        if window == register_window and event == "Creer mon compte et me connecter" :

            #Verification que l'utilisateur n'est pas deja enregistre
            if values["-NEWID-"] in user :
                window["-NEWWRONG-"].update("Cet utilisateur est deja enregistre")

            #Verification de l'exactitude du mot de passe
            elif values["-NEWMDP-"] != values["-MDPCONFIRM-"] :
                window["-NEWWRONG-"].update("Les mots de passe ne correspondent pas")

            #Ajout de l'utilisateur si tout est bon
            else:
                with open("tests/users.csv", mode = "a", newline = "") as file :
                    filewriter = csv.writer(file, delimiter = ";")
                    #L'utilisateur aura pour donnees de victoire et de defaites 0, car il vient de s'inscrire
                    filewriter.writerow([str(values["-NEWID-"]), int(values["-NEWMDP-"]), 0, 0])
                    file.close()
                break

        #Passage de la fenetre de connexion a la fenetre d'inscription
        """penser a initialiser la position de la fenetre a chaque fois, de telle sorte que si l'utilisateur change de fenetre, il ne se retrouve pas teleporte d'un morceau d'ecran a l'autre"""
        if window == login_window and event == "Creer un compte" :
            login_window.hide()
            register_window.un_hide()

        #Passage de la fenetre d'inscription a la fenetre de connexion
        if window == register_window and event == "J'ai deja un compte, me connecter" :
            login_window.un_hide()
            register_window.hide()

    #Fermeture des fenetres
    login_window.close()
    register_window.close()
    return 0