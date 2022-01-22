# -*- coding: utf-8 -*-
# Header

"""

Programme secondaire Sapce Invader

Que fait ce programme : Comptient les différentes fonctions pour réaliser le Space Invader

Qui l'a fait : Amaury CHRONOWSKI / Gabin JOBERT--ROLLIN

Quand a-t-il été réalisé : 15/11/2021 -22/01/2022

Que reste-t-il à faire :

"""

#Importation de bibliothèques nécessaires
import tkinter as tk
from random import random

#Fonctions utilisées dans le programme principal
class SpaceInvader(tk.Frame): #Classe de la fenêtre de jeu
    def __init__(self,root, img1,img2,img3,img4,img5,img6): #initialisation de la fenêtre de jeu | Reçoit : les images des ennemies

        super().__init__(root)
        self.root = root

        #Variables

        #Images des ennemies
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        self.img4 = img4
        self.img5 = img5
        self.img6 = img6

        # Menu

        #Frame du menu
        self.menu = tk.Frame(bg = "black")
        
        #Titre
        self.titre = tk.Label(self.menu, text = "Space Invader", font = ("Helvetica", 80), fg = "green",bg = "black")
        self.titre.pack(side = "top", expand = "yes")
        
        #Boutton poue lancer le jeu
        self.bDemarrer = tk.Button(self.menu, text = "START", font = ("Helvetica", 30), fg = "green", bg = "black", activebackground = 'green', activeforeground = 'white', highlightcolor = "white", highlightthickness = 4, relief = "flat", highlightbackground = "green", command = self.startPartie)
        self.bDemarrer.pack(side = "top", expand = "yes")
        
        #Boutton pour quitter
        self.bQuitter = tk.Button(self.menu, text = "QUIT", font = ("Helvetica", 30), fg = "green", bg = "black", activebackground = 'green', activeforeground = 'white', highlightcolor = "white", highlightthickness = 4, relief = "flat", highlightbackground = "green", command = self.root.destroy)
        self.bQuitter.pack(side = "top", expand = "yes")
        
        self.menu.pack(fill = "both",expand = "yes") 

    def bindPlayer(self,player,ennemi,scoreVar): #Fonctions atribuant des action à des touches du clavier | Reçoit : l'objet joueur, l'objet ennemie et le score du joueur | Lance : les fonction de déplacement du personnage (qui prennent les actions de touche du clavier) et la fonction de tir du personnage (qui pend les action du clavier, l'objet ennemie et le score du joueur)
        self.root.bind("<KeyRelease-z>", lambda event, e = self.canvaGame: player.vaUpRelease(event, e))
        self.root.bind("<KeyPress-z>", lambda event, e = self.canvaGame: player.vaUpPress(event, e))
        self.root.bind("<KeyRelease-s>", lambda event, e = self.canvaGame: player.vaDownRelease(event, e))
        self.root.bind("<KeyPress-s>", lambda event, e = self.canvaGame: player.vaDownPress(event, e))
        self.root.bind("<KeyRelease-q>", lambda event, e = self.canvaGame: player.vaLeftRelease(event, e))
        self.root.bind("<KeyPress-q>", lambda event, e = self.canvaGame: player.vaLeftPress(event, e))
        self.root.bind("<KeyRelease-d>", lambda event, e = self.canvaGame: player.vaRightRelease(event, e))
        self.root.bind("<KeyPress-d>", lambda event, e = self.canvaGame: player.vaRightPress(event, e))
        self.root.bind("<space>", lambda event, e = self.canvaGame: player.tir(event, e, ennemi, scoreVar))     
            
    def startPartie(self): #Fonction qui lance une partie 

        #Déstruction de la frame du menu
        self.menu.destroy()
        
        #Variables
        self.vie = 3 #Vie du personnage
        self.scoreVar = 0 #Score
        self.rafale = "yes" #Inofrmation pour le boss
        self.rafaleNb = 0 #Inofrmation pour le boss

        #Initialisation de la variable permétant de modifier le score
        self.scoreStr = tk.StringVar()  
        self.scoreStr.set(str(self.scoreVar))

        #Jeu

        #Frame du jeu
        self.frameGame = tk.Frame(bg = "black")
        
        #Canvas où se déroule le jeu
        self.canvaGame = tk.Canvas(self.frameGame, bg = 'black', height = 900, width = 900, highlightcolor = "white", highlightthickness = 2, relief = "flat", highlightbackground = "green")
        self.canvaGame.pack(side = "left")
        
        #Frame contenant l'information de la vie du joueur
        self.freamHeartContain = tk.Frame(self.frameGame, bg = "black")
        self.freamHeartContain.pack()

        #Image du coeur
        self.heartimg = tk.PhotoImage(file = 'images/heart.gif')
        
        #Frame pour chaque coeur en prévision de leur supréssions une par une
        self.FreamHeart1 = tk.Frame(self.freamHeartContain, bg = "black")
        self.FreamHeart1.pack(side = 'left')

        self.FreamHeart2 = tk.Frame(self.freamHeartContain, bg = "black")
        self.FreamHeart2.pack(side = 'left')

        self.FreamHeart3 = tk.Frame(self.freamHeartContain, bg = "black")
        self.FreamHeart3.pack(side = 'right')
        
        #Inssertion des image du coeur dans les frames
        self.Heart1 = tk.Canvas(self.FreamHeart1, height = 180, width = 180, bg = "black", highlightthickness = 0)
        self.Heart1.create_image(0, 0, anchor = 'nw', image = self.heartimg)
        self.Heart1.pack(side = "left")
        
        self.Heart2 = tk.Canvas(self.FreamHeart2, height = 180, width = 180, bg = "black", highlightthickness = 0)
        self.Heart2.create_image(0, 0, anchor = 'nw', image = self.heartimg)
        self.Heart2.pack(side = "top")
        
        self.Heart3 = tk.Canvas(self.FreamHeart3, height = 180, width = 180, bg = "black", highlightthickness = 0)
        self.Heart3.create_image(0, 0, anchor = 'nw', image = self.heartimg)
        self.Heart3.pack(side = "right")
        
        #Affichage du score
        self.labelScore1 = tk.Label(self.frameGame, text = "Score : ", fg = "green", bg = "black", font = ("Helvetica", 50))
        self.labelScore1.pack(anchor = "w")
        
        self.labelScore2 = tk.Label(self.frameGame, textvariable = self.scoreStr, font = ("Helvetica", 50), bg = "black", fg = "green")
        self.labelScore2.pack(anchor = "w")

        #Boutton rejouer
        self.bRejouer = tk.Button(self.frameGame, text = "RESTART", font = ("Helvetica", 50), fg = "green", bg = "black", activebackground = 'green', activeforeground = 'white', highlightcolor = "white", highlightthickness = 4, relief = "flat", highlightbackground = "green", command = self.rejouer)
        self.bRejouer.pack(anchor = "s", expand = "yes")

        #Boutton pour quitter
        self.bQuitter = tk.Button(self.frameGame, text = "QUIT", font = ("Helvetica",50), fg = "green", bg = "black", activebackground = 'green', activeforeground = 'white', highlightcolor = "white", highlightthickness = 4, relief = "flat", highlightbackground = "green", command = self.root.destroy)
        self.bQuitter.pack(anchor = "s", expand = "yes")
        
        self.frameGame.pack(fill = "both", expand = "yes")

        #Fonction qui enclanche la partie
        self.gameStart() 
        
    def rejouer(self): #Fonction pour rejouer une partie

        #Détruit la frame de jeu
        self.frameGame.destroy()

        #Fonction qui lance une partie
        self.startPartie()

    def gameStart(self): #Fonction qui enclanche la partie | Lance : Fonction qui associe les touches du clavier à des actions et la fonction qui rafréchit en continue du jeu
        
        #Objet utilisés dans les fonctions
        obstacl=obstacle(self,75,700) #Obstacles protégant le joueur
        player=joueur(self,450,830) #Elément joeur
        ennemi=Ennemi(self,50,300, self.img1,self.img2,self.img3,self.img5,self.img6) #Différents ennemies utilisés

        self.bindPlayer(player,ennemi,self.scorevar) #Fonction qui associe les touches du clavier à des actions
        self.gameLoop(player,ennemi,obstacl,1,"d") #Fonction qui rafréchit en continue du jeu

    def gameEnd(self): #Fonction de fin de partie

        #Déstruction de la frame de jeu 
        self.frameGame.destroy()

        #Création de la frame de fin de partie
        self.frameGame = tk.Frame(bg="black")

        #Différentiation entre la victoire et la défaite
        if self.vie != 0:
            self.fin = tk.Label(self.frameGame, text = "Vous avez gagné", fg = "green", bg = "black", font = ("Helvetica", 50))

        if self.vie == 0:
            self.fin = tk.Label(self.frameGame, text = "Vous avez perdu", fg = "green", bg = "black", font = ("Helvetica", 50))

        self.fin.pack(side = "top")

        #Affichage du score final
        self.scorefin = tk.Label(self.frameGame, text = "Votre socre est de " + str(self.scorevar), fg = "green", bg = "black", font = ("Helvetica", 50))
        self.scorefin.pack(side = "top")

        #Boutton pour quitter
        self.bQuitter = tk.Button(self.frameGame, text = "QUIT", font = ("Helvetica",50), fg = "green", bg = "black", activebackground = 'green', activeforeground = 'white', highlightcolor = "white", highlightthickness = 4, relief = "flat", highlightbackground = "green", command = self.root.destroy)
        self.bQuitter.pack(anchor = "s", expand = "yes")

        #Boutton rejouer
        self.bRejouer = tk.Button(self.frameGame, text = "RESTART", font = ("Helvetica", 50), fg = "green", bg = "black", activebackground = 'green', activeforeground = 'white', highlightcolor = "white", highlightthickness = 4, relief = "flat", highlightbackground = "green", command = self.rejouer)
        self.bRejouer.pack(anchor = "s", expand = "yes")

        self.frameGame.pack(fill = "both", expand = "yes")


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
            speed=10
            ennemi.Boss(self.img4,self.canvaGame)
            if ennemi.shotsE != []:
                for shoot in ennemi.shotsE:
                    shoot.updateE(self.canvaGame)
                    
        elif ennemi.bossvie==0:
            self.gameEnd()
            
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
            
    def tir(self, event,canva,ennemi,scoreVar):
        if self.shots ==[]:
            self.shots.append(tirShot(canva,self,ennemi,scoreVar))   
        
    def __init__(self, canva, x, y):
        self.vaRightBool=False
        self.vaLeftBool=False

        self.imageEnemis = tk.PhotoImage(file="images/joueur.gif")
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

                 elif b==ennemi.boss and ennemi.bossvie==3:
                    ennemi.bossvie-=1
                    canva.delete(self.shot)
                    self.person.shots.pop()
                    x1,y1,x2,y2=canva.bbox(ennemi.boss)
                    x=x1+(x2-x1)
                    y=y1+(y2-y1)
                    canva.delete(ennemi.boss)
                    ennemi.boss=canva.create_image(x,100, image=ennemi.imgboss1)

                elif b==ennemi.boss and ennemi.bossvie==2:
                    ennemi.bossvie-=1
                    canva.delete(self.shot)
                    self.person.shots.pop()
                    x1,y1,x2,y2=canva.bbox(ennemi.boss)
                    x=(x2+x1)/2
                    y=(y2+y1)/2
                    canva.delete(ennemi.boss)
                    ennemi.boss=canva.create_image(x,100, image=ennemi.imgboss2)

                elif b==ennemi.boss and ennemi.bossvie==1:
                    ennemi.bossvie-=1
                    canva.delete(self.shot)
                    self.person.shots.pop()
                    scorevar+=1000
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
            
            
        
