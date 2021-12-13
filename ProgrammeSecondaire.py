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
from tkinter import Tk, Frame, Button

class SpaceInvader(Tk):
    def __init__(self):
        super().__init__()
        
        # Fentêtre
        self.title('Space Invader')
        self.geometry('1600x900')
        
        # Menu
        self.Menu = Frame()
        self.Menu.pack()
        self.greenbutton = Button(self.Menu, text="Brown", fg="brown",command=self.Menu.destroy)
        self.greenbutton.pack()
        
        
        
    
        
        
