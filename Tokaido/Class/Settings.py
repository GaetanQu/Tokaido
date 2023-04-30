import PySimpleGUI as sg
import csv

csv_directory = "Tokaido/class/settings.csv"

class Settings():
    def __init__(self) :
        with open(csv_directory, mode = "r") as file :
            filereader = csv.reader(file, delimiter=';')
            setting = {}
            for ligne in filereader :
                setting[ligne[0]] = ligne[1]
            file.close()

            fps_row = [[sg.Text("FPS : ", font = ("Arial", 20)), sg.InputText(text = setting["FPS"], key = "-FPS-")]]

            setting_window = sg.window("Paramètres", fps_row)

    def settings_menu(self, settings):
        self.setting_window.read()

