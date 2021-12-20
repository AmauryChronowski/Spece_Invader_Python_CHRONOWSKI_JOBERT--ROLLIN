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
from os import spawnl
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
        
        self.titre=Label(self.Menu, text="Space Invader",font=("Helvetica",80), fg="green",bg="black")
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
        
        self.FreamHeartContain= Frame(self.FrameGame,bg="black")
        self.FreamHeartContain.pack()
        """"
        self.FreamHeartContain.columnconfigure(0,weight=1)
        self.FreamHeartContain.columnconfigure(1,weight=1)
        self.FreamHeartContain.columnconfigure(2,weight=1)
        """
        self.heartimg=PhotoImage(file='images/heart.png')
        
        self.FreamHeart1= Frame(self.FreamHeartContain,bg="black")
        self.FreamHeart1.pack()
        self.FreamHeart2= Frame(self.FreamHeartContain,bg="black")
        self.FreamHeart2.pack()
        self.FreamHeart3= Frame(self.FreamHeartContain,bg="black")
        self.FreamHeart3.pack()
        
        self.Heart1=Canvas(self.FreamHeart1,height=180,width=180,bg="black",highlightthickness=0)
        self.Heart1.create_image(0,0,anchor='nw',image=self.heartimg)
        self.Heart1.pack(side="left")
        
        self.Heart2=Canvas(self.FreamHeart2,height=180,width=180,bg="black",highlightthickness=0)
        self.Heart2.create_image(0,0,anchor='nw',image=self.heartimg)
        self.Heart2.pack(side="top")
        
        self.Heart3=Canvas(self.FreamHeart3,height=180,width=180,bg="black",highlightthickness=0)
        self.Heart3.create_image(0,0,anchor='nw',image=self.heartimg)
        self.Heart3.pack(side="right")
        
        
        self.labelScore1 = Label(self.FrameGame, text="Score :", fg="green",bg="black",font=("Helvetica",50))
        self.labelScore1.pack(anchor="ne")
        
        self.labelScore2 = Label(self.FrameGame, text=" ",font=("Helvetica",50),bg="black", fg="green")
        self.labelScore2.pack(anchor="ne")

        self.Quitter = Button(self.FrameGame, text="QUIT",font=("Helvetica",50),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.destroy)
        self.Quitter.pack(anchor="se")
        
        self.FrameGame.pack(fill="both",expand="yes")
        joueur(self,150,150)

    

    """ 
    def clock(self):
        return time.time()-self.clockStartTime

    """
class mobs(SpaceInvader):
    def __init__(self,SpaceInvader,x,y):
        item = SpaceInvader.canvaGame.create_image(x,y, image=self.imageEnemis)
        SpaceInvader.canvaGame.pack() 
        SpaceInvader.mainloop()
    

class enemis1(mobs):
    def __init__(self, SpaceInvader, x, y):
        self.imageEnemis = PhotoImage(file="images\enemi1.gif")
        super().__init__(SpaceInvader,x,y)
class enemis2(mobs):
    def __init__(self, SpaceInvader, x, y):
        self.imageEnemis = PhotoImage(file="images\enemi2.gif")
        super().__init__(SpaceInvader,x,y)

class enemis3(mobs):
    def __init__(self, SpaceInvader, x, y):
        self.imageEnemis = PhotoImage(file="images\enemi3.gif")
        super().__init__(SpaceInvader,x,y)

class joueur(mobs):
    
        

    def vaUp(self, event):
        print('UP')
        self.fenetre.move(self.imageEnemis,0,20)

    def vaDown(self, SpaceInvader, event):
        print('DOWN')
        SpaceInvader.canvaGame.move(self.imageEnemis,0,-20)
    def vaRight(self, SpaceInvader, event):
        print('RIGHT')
        SpaceInvader.canvaGame.move(self.imageEnemis,20,0)

    def vaLeft(self, SpaceInvader, event):
        print('LEFT')
        SpaceInvader.canvaGame.move(self.imageEnemis,-20,0)

    def __init__(self, SpaceInvader, x, y):
        self.fenetre=SpaceInvader.canvaGame
        SpaceInvader.bind("z",self.vaUp)
        SpaceInvader.bind("q",self.vaLeft)   
        SpaceInvader.bind("s",self.vaDown)   
        SpaceInvader.bind("d",self.vaRight)      
        self.imageEnemis = PhotoImage(file="images\joueur.gif")
        super().__init__(SpaceInvader,x,y)

    

    def move(self):
        SpaceInvader.bind("<key>",self.vaRight)   
        SpaceInvader.canvaGame.pack()
        SpaceInvader.mainloop()
    