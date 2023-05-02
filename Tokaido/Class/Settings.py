import PySimpleGUI as sg
import csv

csv_directory = "Tokaido/class/settings.csv"

class Settings():
    def __init__(self) :
        self.setting = {}
        with open(csv_directory, mode = "r") as file :
            filereader = csv.reader(file, delimiter=';')
            for ligne in filereader :
                self.setting[ligne[0]] = ligne[1]
            file.close()
            self.keys_list = list(self.setting.keys())

    def menu(self):
        lcol = sg.Column([[sg.Text("FPS :", font = ("Arial", 12))]])
        rcol = sg.Column([[sg.InputText(self.setting["FPS"], size = (5,5), justification = "center", key = "-FPS-")]])
        save_and_quit_row = [[sg.Button("Sauvegarder", bind_return_key = True), sg.Button("Quitter")]]

        settings_window = sg.Window("Parametres", [[lcol, rcol], save_and_quit_row], finalize = True)
        settings_window.un_hide()
        while True :
            event, values = settings_window.read()

            if event == sg.WINDOW_CLOSED or event == "Quitter" :
                break

            elif event == "Sauvegarder":

                self.setting["FPS"] = values["-FPS-"]

                with open(csv_directory, mode = 'w', newline = '') as file:
                    filewriter = csv.writer(file, delimiter = ";")
                    for key in self.keys_list :
                        filewriter.writerow([key, self.setting[key]])
                    file.close()

        settings_window.hide()