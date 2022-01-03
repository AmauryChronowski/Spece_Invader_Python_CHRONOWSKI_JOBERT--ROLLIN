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
import tkinter as tk
from time import time
from PIL import Image


class SpaceInvader(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        # Fentêtre
        
        

        # Menu
        self.Menu = tk.Frame(bg="black")
        
        self.titre=tk.Label(self.Menu, text="Space Invader",font=("Helvetica",80), fg="green",bg="black")
        self.titre.pack(side="top", expand="yes")
        
        self.Démarrer = tk.Button(self.Menu, text="START",font=("Helvetica",30),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.startPartie)
        self.Démarrer.pack(side="top", expand="yes")
        
        self.Quitter = tk.Button(self.Menu, text="QUIT",font=("Helvetica",30),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.root.destroy)
        self.Quitter.pack(side="top", expand="yes")
        
        self.Menu.pack(fill="both",expand="yes") 

    def bindPlayer(self,Player):
        self.root.bind("z",lambda event, e=self.canvaGame: Player.vaUp(event, e))
        self.root.bind("q",lambda event, e=self.canvaGame: Player.vaLeft(event, e))   
        self.root.bind("s",lambda event, e=self.canvaGame: Player.vaDown(event, e))   
        self.root.bind("d",lambda event, e=self.canvaGame: Player.vaRight(event, e))   
            
    def startPartie(self):
        self.Menu.destroy()
        
        #self.clockStartTime=time.time()

        self.FrameGame= tk.Frame(bg="black")
        
        self.canvaGame=tk.Canvas(self.FrameGame, bg= 'black',height=900,width=900,highlightcolor="white",highlightthickness=2,relief="flat",highlightbackground="green")
        self.canvaGame.pack(side="left")
        
        self.FreamHeartContain= tk.Frame(self.FrameGame,bg="black")
        self.FreamHeartContain.pack()
        """"
        self.FreamHeartContain.columnconfigure(0,weight=1)
        self.FreamHeartContain.columnconfigure(1,weight=1)
        self.FreamHeartContain.columnconfigure(2,weight=1)
        """
        self.heartimg=tk.PhotoImage(file='images/heart.png')
        
        self.FreamHeart1= tk.Frame(self.FreamHeartContain,bg="black")
        self.FreamHeart1.pack()
        self.FreamHeart2= tk.Frame(self.FreamHeartContain,bg="black")
        self.FreamHeart2.pack()
        self.FreamHeart3= tk.Frame(self.FreamHeartContain,bg="black")
        self.FreamHeart3.pack()
        
        self.Heart1=tk.Canvas(self.FreamHeart1,height=180,width=180,bg="black",highlightthickness=0)
        self.Heart1.create_image(0,0,anchor='nw',image=self.heartimg)
        self.Heart1.pack(side="left")
        
        self.Heart2=tk.Canvas(self.FreamHeart2,height=180,width=180,bg="black",highlightthickness=0)
        self.Heart2.create_image(0,0,anchor='nw',image=self.heartimg)
        self.Heart2.pack(side="top")
        
        self.Heart3=tk.Canvas(self.FreamHeart3,height=180,width=180,bg="black",highlightthickness=0)
        self.Heart3.create_image(0,0,anchor='nw',image=self.heartimg)
        self.Heart3.pack(side="right")
        
        
        self.labelScore1 = tk.Label(self.FrameGame, text="Score :", fg="green",bg="black",font=("Helvetica",50))
        self.labelScore1.pack(anchor="ne")
        
        self.labelScore2 = tk.Label(self.FrameGame, text=" ",font=("Helvetica",50),bg="black", fg="green")
        self.labelScore2.pack(anchor="ne")

        self.Quitter = tk.Button(self.FrameGame, text="QUIT",font=("Helvetica",50),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.root.destroy)
        self.Quitter.pack(anchor="se")
        
        self.FrameGame.pack(fill="both",expand="yes")

        player=joueur(self,450,830)
        self.bindPlayer(player)
    

    """ 
    def clock(self):
        return time.time()-self.clockStartTime

    """
class mobs():
    def __init__(self,root,x,y):
        self.canva=root.canvaGame
        self.root=root
        self.item = root.canvaGame.create_image(x,y, image=self.imageEnemis)
        root.canvaGame.pack() 
        
    

class enemis1(mobs):
    def __init__(self, canva, x, y):
        self.imageEnemis = PhotoImage(file="images/enemi1.gif")
        super().__init__(canva,x,y)
class enemis2(mobs):
    def __init__(self, canva, x, y):
        self.imageEnemis = PhotoImage(file="images/enemi2.gif")
        super().__init__(canva,x,y)

class enemis3(mobs):
    def __init__(self, canva, x, y):
        self.imageEnemis = PhotoImage(file="images/enemi3.gif")
        super().__init__(canva,x,y)

class joueur(mobs):
    """
    def vaUp(self, event, canva):
        print('UP')
        canva.move(self.item,0,-20)
    
    def vaDown(self, event, canva):
        print('DOWN')
        canva.move(self.item,0,20)
    """
    def vaRight(self, event, canva):
        print('RIGHT')
        x1,x2,y1,y2=canva.coords(self.item)
        print(x1,x2)
        
        canva.move(self.item,10,0)

    def vaLeft(self, event, canva):
        print('LEFT')
        canva.move(self.item,-10,0)

    def tir(self, canva):
        shot= canva.create_oval(self.x-10,self.y-20-self.imageHeight/2,self.x+10,self.y-self.imageHeight/2,fill='green')
      
    def __init__(self, canva, x, y):
        imgj=Image.open("images/joueur.png")
        imgj_copy= imgj.copy()
        imgj = imgj_copy.resize((110, 84))
        self.imageEnemis = tk.PhotoImage(imgj)
        super().__init__(canva,x,y)