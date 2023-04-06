#Ce fichier contient l'authentificateur. Les donnees seront enregistrees sur un fichier .csv et l'authificateur sera affiche via PySimpleGUI
import PySimpleGUI as sg
import csv

csv_directory = "Tokaido/Class/users.csv"

#Importation des donnees du fichier csv
with open(csv_directory, mode = "r") as file :
    filereader = csv.reader(file, delimiter=';')
    user = {}
    for ligne in filereader :
        user[ligne[0]] = ligne
    file.close()

#Defnition du theme de PySimpleGUI
sg.theme('GrayGrayGray')

#Creation du layout de la fenetre de connexion
login_title = [[sg.Text("Connectez-vous pour jouer au Tokaido !", font = ("Arial", 20))]]
login_lcol = sg.Column([[sg.Text("Nom d'utilisateur")],
                        [sg.Text("Mot de passe")]])
login_rcol = sg.Column([[sg.InputText(key="-ID-")],
                        [sg.InputText(key="-MDP-", password_char="*")]])
login_buttons = [[sg.Button("Connexion", bind_return_key = True), sg.Button("Creer un compte"), sg.Text("", key="-WRONG-")]]

#Creation de la fenetre de connexion
login_window = sg.Window("Connectez-vous", [[login_title],[login_lcol, login_rcol], login_buttons ], finalize=True)

#Creation du layout de la fenetre d'inscription
register_title = [[sg.Text("S'inscrire", font = ("Arial", 20))]]
register_lcol = sg.Column([[sg.Text("Nom d'utilisateur")],
                           [sg.Text("Mot de passe")],
                           [sg.Text("Confirmation du mot de passe")]])
register_rcol = sg.Column([[sg.InputText(key="-NEWID-")],
                           [sg.InputText(key="-NEWMDP-", password_char="*")],
                           [sg.InputText(key="-MDPCONFIRM-", password_char="*")]])
register_wrong = [[sg.Text("", key="-NEWWRONG-")]]
register_buttons = [[sg.Button("Creer un compte et me connecter"), sg.Button("J'ai deja un compte, me connecter")]]

#Creation de la fenetre d'inscription
register_window = sg.Window("Insrcivez-vous", [[register_title], [register_lcol, register_rcol],[register_wrong], [register_buttons]], finalize=True)

#Comme on ne s'inscrit qu'une fois, on affiche par defaut la fenetre de connexion, et donc on cache la fenetre d'inscription
register_window.hide()

#Definition de la classe Auth a appeler dans le programme principal
def auth() :
    while True :
        window, event, values = sg.read_all_windows()

        #L'utilisateur ne se connecte pas
        if event == sg.WINDOW_CLOSED:
            return False

        #Connexion
        if window == login_window and event == "Connexion" or window == login_window and event == sg.Input("Return"):
            if values["-ID-"].lower() in user and values["-MDP-"] == user[values["-ID-"].lower()][1] :
                break
            else :
                window["-WRONG-"].update("Identifiant ou mot de passe incorrect")

        #Inscription
        if window == register_window and event == "Creer un compte et me connecter" :

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
                    #L'utilisateur aura pour donnees de victoire et de defaites 0, car il vient de s'inscrire
                    filewriter.writerow([str(values["-NEWID-"].lower()), str(values["-NEWMDP-"]), 0, 0])
                    file.close()
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
    login_window.close()
    register_window.close()
    return True
