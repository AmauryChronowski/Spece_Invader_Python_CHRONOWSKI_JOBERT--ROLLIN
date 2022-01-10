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
        self.root.bind("<KeyRelease-z>",lambda event, e=self.canvaGame: Player.vaUpRelease(event, e))
        self.root.bind("<KeyPress-z>",lambda event, e=self.canvaGame: Player.vaUpPress(event, e))
        self.root.bind("<KeyRelease-s>",lambda event, e=self.canvaGame: Player.vaDownRelease(event, e))
        self.root.bind("<KeyPress-s>",lambda event, e=self.canvaGame: Player.vaDownPress(event, e))
        self.root.bind("<KeyRelease-q>",lambda event, e=self.canvaGame: Player.vaLeftRelease(event, e))
        self.root.bind("<KeyPress-q>",lambda event, e=self.canvaGame: Player.vaLeftPress(event, e))
        self.root.bind("<KeyRelease-d>",lambda event, e=self.canvaGame: Player.vaRightRelease(event, e))
        self.root.bind("<KeyPress-d>",lambda event, e=self.canvaGame: Player.vaRightPress(event, e))

       
        self.root.bind("<space>",lambda event, e=self.canvaGame: Player.tir(event, e))     
            
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
        self.FreamHeart1.pack(side='left')
        self.FreamHeart2= tk.Frame(self.FreamHeartContain,bg="black")
        self.FreamHeart2.pack(side='left')
        self.FreamHeart3= tk.Frame(self.FreamHeartContain,bg="black")
        self.FreamHeart3.pack(side='right')
        
        self.Heart1=tk.Canvas(self.FreamHeart1,height=180,width=180,bg="black",highlightthickness=0)
        self.Heart1.create_image(0,0,anchor='nw',image=self.heartimg)
        self.Heart1.pack(side="left")
        
        self.Heart2=tk.Canvas(self.FreamHeart2,height=180,width=180,bg="black",highlightthickness=0)
        self.Heart2.create_image(0,0,anchor='nw',image=self.heartimg)
        self.Heart2.pack(side="top")
        
        self.Heart3=tk.Canvas(self.FreamHeart3,height=180,width=180,bg="black",highlightthickness=0)
        self.Heart3.create_image(0,0,anchor='nw',image=self.heartimg)
        self.Heart3.pack(side="right")
        
        
        self.labelScore1 = tk.Label(self.FrameGame, text="Score : ", fg="green",bg="black",font=("Helvetica",50))
        self.labelScore1.pack(anchor="w")
        
        self.labelScore2 = tk.Label(self.FrameGame, text="0",font=("Helvetica",50),bg="black", fg="green")
        self.labelScore2.pack(anchor="w")

        self.RejouerB = tk.Button(self.FrameGame, text="RESTART",font=("Helvetica",50),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.Rejouer)
        self.RejouerB.pack(anchor="s", expand="yes")

        self.Quitter = tk.Button(self.FrameGame, text="QUIT",font=("Helvetica",50),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.root.destroy)
        self.Quitter.pack(anchor="s", expand="yes")
        
        self.FrameGame.pack(fill="both",expand="yes")

        self.gameStart()
        
        
        
        
        
        #player.tir(self.canvaGame)

        

    def Rejouer(self):
        self.FrameGame.destroy()
        self.startPartie()

    """ 
    def clock(self):
        return time.time()-self.clockStartTime
    """
    def gameStart(self):
        player=joueur(self,450,830)
        enemei=enemis1(self,350,330)
        enemei2=enemis1(self,250,330)
        
        
        self.bindPlayer(player)
        self.gameLoop(player)

    def gameLoop(self,player):
        if player.shots != []:
            for shoot in player.shots:
                shoot.update(self.canvaGame)
        if player.vaUpBool ==True:
            player.vaUp(self.canvaGame)
        if player.vaDownBool ==True:
            player.vaDown(self.canvaGame)
        if player.vaRightBool ==True:
            player.vaRight(self.canvaGame)
        if player.vaLeftBool ==True:
            player.vaLeft(self.canvaGame)
        self.canvaGame.after(16,lambda : self.gameLoop(player))
        

class obstacle():
    def __init__(self,root):
        self.canva=root.canvaGame
        self.root=root

class mobs():
    item=[]
    def __init__(self,root,x,y):
        self.canva=root.canvaGame
        self.x=x
        self.y=y
        """ try:
            self.item.append(self.canva.create_image(x,y, image=self.imageEnemis))
        except Exception:
            print("liste pas encore crée") 
            self.item=[self.canva.create_image(x,y, image=self.imageEnemis)] """
        mobs.item.append(self.canva.create_image(x,y, image=self.imageEnemis))
        #root.canvaGame.create_image(x,y, image=self.imageEnemis)
        self.canva.pack() 
        
    

class enemis1(mobs):
    def __init__(self, canva, x, y):
        
        self.imageEnemis = tk.PhotoImage(file="images\enemi1.gif")
        super().__init__(canva,x,y)
        it = self.canva.create_rectangle(50,50,60,60,fill='red')
        print('rouge')




    












class enemis2(mobs):
    def __init__(self, canva, x, y):
        self.imageEnemis = tk.PhotoImage(file="images/enemi2.gif")
        super().__init__(canva,x,y)

class enemis3(mobs):
    def __init__(self, canva, x, y):
        self.imageEnemis = tk.PhotoImage(file="images/enemi3.gif")
        super().__init__(canva,x,y)

class joueur(mobs):
    """ def vaUpRelease(self, event, canva):
        self.vaUpBool=False
    def vaUpPress(self, event, canva):
        self.vaUpBool=True
    def vaUp(self,event, canva):
        print('UP')
        canva.move(self.item,0,-20)

    def vaDownRelease(self, event, canva):
        self.vaDownBool=False
    def vaDownPress(self, event, canva):
        self.vaDownBool=True

    def vaDown(self, canva):
        print('DOWN')
        canva.move(self.item,0,20)
     """
    def vaRightRelease(self, event, canva):
        self.vaRightBool=False
    def vaRightPress(self, event, canva):
        self.vaRightBool=True

    def vaLeftRelease(self, event, canva):
        self.vaLeftBool=False
    def vaLeftPress(self, event, canva):
        self.vaLeftBool=True

   
    def vaRight(self, canva):
        x1,y1,x2,y2=canva.bbox(mobs.item[0])
        if x2+10<900:
            canva.move(mobs.item[0],10,0)
            self.x+=10

    def vaLeft(self, canva):
        x1,y1,x2,y2=canva.bbox(mobs.item[0])
        if x1-10>0:
            canva.move(mobs.item[0],-10,0)
            self.x-=10
            
    def tir(self, event,canva):
        #shot= canva.create_oval(self.x-10,self.y-20-self.imageHeight/2,self.x+10,self.y-self.imageHeight/2,fill='green')
        if self.shots ==[]:
            self.shots.append(tirShot(canva,self))
    #updateTir(self, shot)
        
        
    def __init__(self, canva, x, y):
        self.vaRightBool=False
        self.vaLeftBool=False
        self.vaDownBool=False
        self.vaUpBool=False

        self.imageEnemis = tk.PhotoImage(file="images\joueur.gif")
        self.imageHeight=84
        self.imageWidth=110
        self.shots=[]
        super().__init__(canva,x,y)





class tirShot():
    def __init__(self,canva,person):
        self.person=person
        self.x=person.x
        self.y=person.y
        self.shot= canva.create_oval(person.x-10,person.y-20-person.imageHeight/2,person.x+10,person.y-person.imageHeight/2,fill='green')
        self.update(canva)
    
    def update(self,canva):
        
        if self.y<=900 and self.y>=0:
            self.y-=15
            canva.move(self.shot,0,-15)
            #canva.after(16,lambda : self.update(canva))
        else:
            canva.delete(self.shot)
            self.person.shots.pop()
