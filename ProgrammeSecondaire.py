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
from tkinter import Canvas, Tk, Frame, Button, Label

class SpaceInvader(Tk):
    def __init__(self):
        super().__init__()
        
        # Fentêtre
        self.title('Space Invader')
        self.geometry('1600x900')
        

        # Menu
        self.Menu = Frame()
        self.Menu.pack()
        self.greenbutton = Button(self.Menu, text="Brown", fg="brown",command=self.startPartie)
        self.greenbutton.pack()
        
        

    def startPartie(self):
        self.Menu.destroy()
        self.FrameGame= Frame()
        self.FrameGame.pack()
        self.FrameGame.columnconfigure(0, weight)
        
        
        self.canvaGame=Canvas(self.FrameGame, bg= 'black')
        self.canvaGame.grid(column=0, row=0)
        

        
        self.side=Frame(self.FrameGame)
        self.side.grid(column=1, row=0)
        self.labelScore = Label(self.side, text="Score", fg="blue")
        self.labelScore.pack()
        self.labelVie = Label(self.side, text="X vies", fg="blue" )
        self.labelVie.pack()
        
        

        
        
    
        
        
