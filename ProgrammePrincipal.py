# -*- coding: utf-8 -*-
# Header

"""

Programme principale Sapce Invader

Que fait ce programme : Réalise le lancement du Space Invader

Qui l'a fait : Amaury CHRONOWSKI / Gabin JOBERT--ROLLIN

Quand a-t-il été réalisé : 15/11/2021 - 22/01/2022

Que reste-t-il à faire : 

"""

#Importation de bibliothèques nécessaires
from ProgrammeSecondaire import SpaceInvader
import tkinter as tk

#Programme principal
if __name__ == "__main__":

    #Création de la fenêtre
    root = tk.Tk()
    root.title('Space Invader!')
    root.geometry('1600x900')
    
    #Récupération des images nécessaire au jeu
    img1 = tk.PhotoImage(file="images/enemi1.gif")
    img2 = tk.PhotoImage(file="images/enemi2.gif")
    img3 = tk.PhotoImage(file="images/enemi3.gif")
    img4 = tk.PhotoImage(file="images/Boss.png")
    img5 = tk.PhotoImage(file="images/Boss1.png")
    img6 = tk.PhotoImage(file="images/Boss2.png")
    
    game = SpaceInvader(root,img1,img2,img3,img4,img5,img6) #Intancie la fenêtre de jeu | Entrées : les images des diffrentens ennemies, la fenêtre | Sorties : le jeu
    game.mainloop() #Lance le jeu
