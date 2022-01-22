# -*- coding: utf-8 -*-
    
# Header

"""
Programme principale Sapce Invader

Amaury CHRONOWSKI/Gabin JOBERT--ROLLIN

15/11/2021

Réalise le lancement du Space Invader



-------

"""
#Importation de bibliothèques nécessaires
from ProgrammeSecondaire import SpaceInvader
import tkinter as tk
#Programme principal
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Space Invader!')
    root.geometry('1600x900')
    game = SpaceInvader(root)
    game.mainloop()