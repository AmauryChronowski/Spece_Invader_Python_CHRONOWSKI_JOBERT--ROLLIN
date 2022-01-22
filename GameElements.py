

from random import random
import tkinter as tk
import ClasseProjectiles as CP




class Obstacle():
    listeobstacle=[]
    def __init__(self,root,x,y):
        self.canva=root.canvaGame
        self.root=root
        self.x=x
        self.y=y
        for h in  range(3):
            for i in range(6):
                Pileobstacle=[]
                for j in range(3):
                    Pileobstacle.append(self.canva.create_rectangle (self.x,self.y,self.x+25,self.y-25,outline="gray",fill="green"))
                    self.y-=25
                self.x+=25
                self.y=y
                Obstacle.listeobstacle.append(Pileobstacle)
            self.x=x+(h+1)*300
            self.y=y





class Ennemi():
    shotsE=[]
    def __init__(self,root,x,y,img1,img2,img3,img4,img5):
        self.imgboss1=img4
        self.imgboss2=img5
        self.boss=0
        self.bossvie=3
        self.canva=root.canvaGame
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
                if prob<0.01:
                    Ennemi.shotsE.append(CP.TireE(canva,E))
            
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

    def BossMouv(self,canva,speed,sens):
        x1,y1,x2,y2=canva.bbox(self.boss)

        if x2+speed>=900 and sens=="d":
            sens="g"
            return sens,speed

        if x1-speed<=0 and sens=="g":
            sens="d"
            return sens,speed

        if x2+speed<900 and sens=="d":
            canva.move(self.boss,speed,0)
        elif x1-speed>0 and sens=="g":
            canva.move(self.boss,-speed,0)

        return sens,speed





class Joueur():
    theJoueur=[]
    def vaRightRelease(self, event, canva):
        self.vaRightBool=False
    def vaRightPress(self, event, canva):
        self.vaRightBool=True

    def vaLeftRelease(self, event, canva):
        self.vaLeftBool=False
    def vaLeftPress(self, event, canva):
        self.vaLeftBool=True

    def vaRight(self, canva):
        x1,y1,x2,y2=canva.bbox(Joueur.theJoueur[0])
        if x2+10<900:
            canva.move(Joueur.theJoueur[0],10,0)
            self.x+=10

    def vaLeft(self, canva):
        x1,y1,x2,y2=canva.bbox(Joueur.theJoueur[0])
        if x1-10>0:
            canva.move(Joueur.theJoueur[0],-10,0)
            self.x-=10
            
    def tir(self, event,canva,ennemi,scoreVar):
        if self.shots ==[]:
            self.shots.append(CP.TirShot(canva,self,ennemi,scoreVar))   
        
    def __init__(self, root, x, y):
        self.vaRightBool=False
        self.vaLeftBool=False

        self.imageEnemis = tk.PhotoImage(file="images/joueur.gif")
        self.imageHeight=84
        self.imageWidth=110
        self.shots=[]

        self.canva=root.canvaGame
        self.x=x
        self.y=y
        Joueur.theJoueur.append(self.canva.create_image(x,y, image=self.imageEnemis))
        self.canva.pack()

        #super().__init__(canva,x,y)