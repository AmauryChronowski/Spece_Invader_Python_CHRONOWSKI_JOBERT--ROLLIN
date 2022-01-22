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
    img1 = tk.PhotoImage(file="images/enemi1.gif")
    img2 = tk.PhotoImage(file="images/enemi2.gif")
    img3 = tk.PhotoImage(file="images/enemi3.gif")
    img4 = tk.PhotoImage(file="images/Boss.gif")
    game = SpaceInvader(root,img1,img2,img3,img4)
    game.mainloop()
