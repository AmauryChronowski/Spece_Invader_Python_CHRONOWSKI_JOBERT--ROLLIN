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
from tkinter import Canvas, Tk, Frame, Button, Label, PhotoImage
from time import time

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
        

    def startPartie(self):
        self.Menu.destroy()
        #self.clockStartTime=time.time()
        self.FrameGame= Frame(bg="black")
        
        self.canvaGame=Canvas(self.FrameGame, bg= 'black',height=900,width=900,highlightcolor="white",highlightthickness=2,relief="flat",highlightbackground="green")
        self.canvaGame.pack(side="left")
        

        """"
        self.side=Frame(self.FrameGame)
        self.side.grid(column=1, row=0)
        self.labelScore = Label(self.side, text="Score", fg="blue")
        self.labelScore.pack()
        self.labelVie = Label(self.side, text="X vies", fg="blue" )
        self.labelVie.pack()
        """
        self.FrameGame.pack(fill="both",expand="yes")
        mobs(self,150,150)

    

    """ def clock(self):
        return time.time()-self.clockStartTime

 """
class mobs(SpaceInvader):
    def __init__(self,SpaceInvader,x,y):

        imageEnemis = PhotoImage(file="/fs03/share/users/gabin.jobert-rollin/home/Documents/python/TP4/Spece_Invader_Python_CHRONOWSKI_JOBERT--ROLLIN/enemis.gif")
        item = SpaceInvader.canvaGame.create_image(x,y, image=imageEnemis)
        SpaceInvader.canvaGame.pack() 
        SpaceInvader.mainloop()
    #def move(self):
        
