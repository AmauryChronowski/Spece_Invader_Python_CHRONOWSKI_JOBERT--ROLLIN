# -*- coding: utf-8 -*-

# Header

"""
Programme secondaire Sapce Invader

Amaury CHRONOWSKI/Gabin JOBERT--ROLLIN

15/11/2021

Réalise le lancement du Space Invader



-------

"""
#Importation de bibliothèques nécessaires
from tkinter import Tk, Frame, Button,Label

class SpaceInvader(Tk):
    def __init__(self):
        super().__init__()
        
        # Fentêtre
        self.title('Space Invader')
        self.geometry('1600x900')
        
        # Menu
        self.Menu = Frame(bg="black")
        self.titre=Label(self.Menu, text="Sapce Invader",font=("Helvetica",80), fg="green",bg="black")
        self.titre.pack(side="top", expand="yes")
        self.Démarrer = Button(self.Menu, text="START",font=("Helvetica",30),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.startPartie)
        self.Démarrer.pack(side="top", expand="yes")
        self.Quitter = Button(self.Menu, text="QUIT",font=("Helvetica",30),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.destroy)
        self.Quitter.pack(side="top", expand="yes")
        self.Menu.pack(fill="both",expand="yes") 
        
        
    
        
        
