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
from tkinter.constants import X
from random import random


class SpaceInvader(tk.Frame):
    def __init__(self,root, img1,img2,img3,img4):
        super().__init__(root)
        self.root=root

        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        self.img4 = img4
        

        # Menu
        self.Menu = tk.Frame(bg="black")
        
        self.titre=tk.Label(self.Menu, text="Space Invader",font=("Helvetica",80), fg="green",bg="black")
        self.titre.pack(side="top", expand="yes")
        
        self.Démarrer = tk.Button(self.Menu, text="START",font=("Helvetica",30),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.startPartie)
        self.Démarrer.pack(side="top", expand="yes")
        
        self.Quitter = tk.Button(self.Menu, text="QUIT",font=("Helvetica",30),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.root.destroy)
        self.Quitter.pack(side="top", expand="yes")
        
        self.Menu.pack(fill="both",expand="yes") 

    def bindPlayer(self,Player,ennemi,scorevar):
        
        self.root.bind("<KeyRelease-q>",lambda event, e=self.canvaGame: Player.vaLeftRelease(event, e))
        self.root.bind("<KeyPress-q>",lambda event, e=self.canvaGame: Player.vaLeftPress(event, e))
        self.root.bind("<KeyRelease-d>",lambda event, e=self.canvaGame: Player.vaRightRelease(event, e))
        self.root.bind("<KeyPress-d>",lambda event, e=self.canvaGame: Player.vaRightPress(event, e))
        self.root.bind("<space>",lambda event, e=self.canvaGame: Player.tir(event, e,ennemi,scorevar))     
            
    def startPartie(self):
        self.Menu.destroy()
        
        #self.clockStartTime=time.time()

        self.scorevar=0
        self.scorestr=tk.StringVar()
        self.scorestr.set(str(self.scorevar))

        self.FrameGame= tk.Frame(bg="black")
        
        self.canvaGame=tk.Canvas(self.FrameGame, bg= 'black',height=900,width=900,highlightcolor="white",highlightthickness=2,relief="flat",highlightbackground="green")
        self.canvaGame.pack(side="left")
        
        self.FreamHeartContain= tk.Frame(self.FrameGame,bg="black")
        self.FreamHeartContain.pack()

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
        
        self.labelScore2 = tk.Label(self.FrameGame, textvariable=self.scorestr ,font=("Helvetica",50),bg="black", fg="green")
        self.labelScore2.pack(anchor="w")

        self.RejouerB = tk.Button(self.FrameGame, text="RESTART",font=("Helvetica",50),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.Rejouer)
        self.RejouerB.pack(anchor="s", expand="yes")

        self.Quitter = tk.Button(self.FrameGame, text="QUIT",font=("Helvetica",50),fg="green",bg="black",activebackground='green',activeforeground='white',highlightcolor="white",highlightthickness=4,relief="flat",highlightbackground="green",command=self.root.destroy)
        self.Quitter.pack(anchor="s", expand="yes")
        
        self.FrameGame.pack(fill="both",expand="yes")

        self.gameStart()
        
    def Rejouer(self):
        self.FrameGame.destroy()
        self.startPartie()

    def gameStart(self):
        obstacl=obstacle(self,75,700)
        player=joueur(self,450,830)
        ennemi=Ennemi(self,50,300, self.img1,self.img2,self.img3)
        self.bindPlayer(player,ennemi,self.scorevar)
        self.gameLoop(player,ennemi,obstacl,1,"d")
        print(player.imageEnemis)

    def gameLoop(self,player,ennemi,obstacl,speed,sens):
        if player.shots != []:
            for shoot in player.shots:
                self.scorevar=shoot.update(self.canvaGame,ennemi,self.scorevar)

        
        if player.vaRightBool ==True:
            player.vaRight(self.canvaGame)
        if player.vaLeftBool ==True:
            player.vaLeft(self.canvaGame)

        for i in ennemi.listeEnnemies:
            if i==[]:
                ennemi.listeEnnemies.pop( ennemi.listeEnnemies.index(i))

        if  ennemi.listeEnnemies!=[]:
            sens,speed=ennemi.move(self.canvaGame,speed,sens)
            ennemi.tire(self.canvaGame)
            if Ennemi.shotsE != []:
                for shoot in Ennemi.shotsE:
                    shoot.updateE(self.canvaGame)
            self.scorestr.set(str(self.scorevar))
            

        elif ennemi.boss==0 and ennemi.listeEnnemies==[]:
            ennemi.Boss(self.img4,self.canvaGame)
            if Ennemi.shotsE != []:
                for shoot in Ennemi.shotsE:
                    shoot.updateE(self.canvaGame)
            
            
        else:
            if Ennemi.shotsE != []:
                for shoot in Ennemi.shotsE:
                    shoot.updateE(self.canvaGame)
        self.canvaGame.after(16,lambda : self.gameLoop(player,ennemi,obstacl,speed,sens))
class obstacle():
    listeobstacle=[]
    def __init__(self,root,x,y):
        self.canva=root.canvaGame
        self.root=root
        self.x=x
        self.y=y
        #self.listeobstacle=[]
        for h in  range(3):
            for i in range(6):
                Pileobstacle=[]
                for j in range(3):
                    Pileobstacle.append(self.canva.create_rectangle (self.x,self.y,self.x+25,self.y-25,outline="gray",fill="green"))
                    self.y-=25
                self.x+=25
                self.y=y
                obstacle.listeobstacle.append(Pileobstacle)
            self.x=x+(h+1)*300
            self.y=y
class mobs():
    item=[]
    def __init__(self,root,x,y):
        self.canva=root.canvaGame
        self.x=x
        self.y=y
        mobs.item.append(self.canva.create_image(x,y, image=self.imageEnemis))
        self.canva.pack()
        
    
class Ennemi():
    
    shotsE=[]
    def __init__(self,root,x,y,img1,img2,img3):
        self.boss=0
        self.canva=root.canvaGame
        #self.shotsE=[]
        self.root=root
        self.x=x
        self.y=y
        self.listeEnnemies=[]
        for i in range(6):
            filleEnnemies=[]
            filleEnnemies.append(self.canva.create_image(self.x,self.y, image=img1))
            self.y-=100
            filleEnnemies.append(self.canva.create_image(self.x,self.y, image=img2))
            self.y-=100
            filleEnnemies.append(self.canva.create_image(self.x,self.y, image=img3))
            self.y=300
            self.x+=100
            self.listeEnnemies.append(filleEnnemies)
            

    def tire(self,canva):

        for i in range(len(self.listeEnnemies)):
            if self.listeEnnemies[i]!=[]:
                E=self.listeEnnemies[i][-1]
                prob=random()
                if prob<0.1:
                    Ennemi.shotsE.append(tireE(canva,E))

            
    def move(self,canva,speed,sens):
        r=0
        m=0
        for i in self.listeEnnemies:
            for j in i :
                if j!=0 and r==0:
                    Eg=j
                    r=1
        for i in list(reversed(self.listeEnnemies)):
            for j in i:
                if j!=0 and m==0:
                    Ed=j
                    m=1


        xd1,yd,xd2,yd=canva.bbox(Ed)
        xg1,yg,xg2,yg=canva.bbox(Eg)

        if xd2+speed>=900 and sens=="d":
            for i in self.listeEnnemies:
                for j in i:
                    canva.move(j,0,10)
            speed+=0.25
            sens="g"
            return sens,speed
        if xg1-speed<=0 and sens=="g":
            for i in self.listeEnnemies:
                for j in i:
                    canva.move(j,0,10)
            speed+=0.25
            sens="d"
            return sens,speed
        for i in self.listeEnnemies:
            for j in i:
                x1,y1,x2,y2=canva.bbox(j)
                if x2+speed<900 and sens=="d":
                    canva.move(j,speed,0)
                elif x1-speed>0 and sens=="g":
                    canva.move(j,-speed,0)
        return sens,speed
    
    def Boss (self, boss, canva):
        self.boss=canva.create_image(450,100, image=boss)


class joueur(mobs):
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
            
    def tir(self, event,canva,ennemi,scorevar):
        if self.shots ==[]:
            self.shots.append(tirShot(canva,self,ennemi,scorevar))   
        
    def __init__(self, canva, x, y):
        self.vaRightBool=False
        self.vaLeftBool=False

        self.imageEnemis = tk.PhotoImage(file="images/joueur.gif")
        print(self.imageEnemis)
        self.imageHeight=84
        self.imageWidth=110
        self.shots=[]

        super().__init__(canva,x,y)

class tirShot():
    def __init__(self,canva,person,ennemi,scorevar):
        self.person=person
        self.x=person.x
        self.y=person.y
        self.shot= canva.create_oval(person.x-10,person.y-20-person.imageHeight/2,person.x+10,person.y-person.imageHeight/2,fill='green')
        
        self.update(canva,ennemi,scorevar)
    
    def update(self,canva,ennemi,scorevar):
            if self.y<=900 and self.y>=0:
                self.y-=15
                canva.move(self.shot,0,-15)
                x1,y1,x2,y2=canva.bbox(self.shot)
                a=canva.find_overlapping(x1,y1,x2,y2)
                b=a[0]
                if b!=self.shot and b in range(56,74):
                    self.person.shots.pop()
                    canva.delete(self.shot)
                    k=0
                    for i in ennemi.listeEnnemies:
                        u=0
                        for j in i:
                            if j==b:
                                if b in [58, 61, 64, 67, 70, 73]:
                                    scorevar+=300
                                elif b in [57, 60, 63, 66, 69, 72]:
                                    scorevar+=200
                                elif b in [56, 59, 62, 65, 68, 71]:
                                    scorevar+=100

                                ennemi.listeEnnemies[k].pop(u)
                                canva.delete(b)  
                            else:
                                u+=1
                        k+=1

            else:
                canva.delete(self.shot)
                self.person.shots.pop()
            return scorevar


class tireE():
    def __init__(self,canva,entity):
        self.entity=entity
        self.x1,self.y1,self.x2,self.y2=canva.bbox(self.entity)
        self.x=(self.x1+self.x2)/2
        self.y=self.y1+60
        self.shotE= canva.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,fill='red')
        
        
    def updateE(self,canva):
        
        if self.y<=900 and self.y>=0 :
            self.y+=15
            
            canva.move(self.shotE,0,+15)  
            x1,y1,x2,y2=canva.bbox(self.shotE)
            a=canva.find_overlapping(x1,y1,x2,y2)
            b=a[0]
            
            if b!=self.shotE and b in range(55):
                canva.delete(b)
                
                for shot in Ennemi.shotsE:
                    if shot.shotE==self.shotE:
                        Ennemi.shotsE.remove(shot)
                
                canva.delete(self.shotE)
                obstacle.listeobstacle[b//3-1].pop()
                
            if b==mobs.item[0]:
                print('joueur touché')
                for shot in Ennemi.shotsE:
                    if shot.shotE==self.shotE:
                        Ennemi.shotsE.remove(shot)
                        
                canva.delete(self.shotE)
            
            
        