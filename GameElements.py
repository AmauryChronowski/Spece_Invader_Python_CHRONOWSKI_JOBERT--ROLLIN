# -*- coding: utf-8 -*-

# Header

"""

Programme secondaire du projet SpaceInvader

Que fait ce programme : Contient les Classes : 
                                - Obstacle (défense du joueur)
                                - Ennemi
                                - Joueur 
                        (tous les éléments de jeu hors tir)

Créateurs : Amaury CHRONOWSKI / Gabin JOBERT--ROLLIN

Date de réalisation: 15/11/2021 - 22/01/2022

Que reste-t-il à faire : - Augmenter la variter d'ennemies et leur capacité
                         - Donner des capacité suplémentaire au joueur pour le rendre plus fort 

"""

#Bibliothèques standards
from random import random
import tkinter as tk

#Bibliothèques personelles
import ClasseProjectiles as CP




class Obstacle():
#Permet de générer 3 bloc d'obstacles

    listeobstacle=[]    #Tableau de la classe Obstacle (et non à un de ses objets) contenants toutes les briques

    def __init__(self,root,x,y):
    #Fait apparaitre les obstacles | Reçoit les coordonnées à partir des quelles on commence à mettre les obstacles  
        
        self.canva=root.canvaGame
        self.root=root
        self.x=x
        self.y=y

        for h in  range(3): #Crée 3 blocs d'obstacles
            for i in range(6): #Crée 6 colonnes par bloc d'obstacle
                Pileobstacle=[] #Pile d'obstacle
                for j in range(3): #Empile les obstacles sur 3 lignes
                    Pileobstacle.append(self.canva.create_rectangle (self.x,self.y,self.x+25,self.y-25,outline="gray",fill="green"))
                    self.y-=25
                self.x+=25
                self.y=y
                Obstacle.listeobstacle.append(Pileobstacle)
            self.x=x+(h+1)*300
            self.y=y





class Ennemi():
#Permet de s'occuper des ennemis 

    shotsE=[]   #Tableau de la classe Ennemi (et non à un de ses objets) contenants tous les tires des ennemies

    def __init__(self,root,x,y,img1,img2,img3,img4,img5):
    #génère 3 lignes de 6 ennemis | Reçoit : la fenêtre, les coordonnées apartir des quels on va placer les ennemies et les images d'ennemies
        
        self.imgboss1=img4
        self.imgboss2=img5
        self.boss=0
        self.bossvie=3
        self.canva=root.canvaGame
        self.root=root
        self.x=x
        self.y=y
        self.listeEnnemies=[]

        for i in range(6): #Crée les 6 colonnes d'ennemies
            filleEnnemies=[] #Fille de colonnes d'ennemie
            filleEnnemies.append(self.canva.create_image(self.x,self.y, image=img1))
            self.y-=100
            filleEnnemies.append(self.canva.create_image(self.x,self.y, image=img2))
            self.y-=100
            filleEnnemies.append(self.canva.create_image(self.x,self.y, image=img3))

            self.y=300
            self.x+=100
            self.listeEnnemies.append(filleEnnemies)

    def tire(self,canva):
    #Fait tirer des enemis aléatoirement
        
        for i in range(len(self.listeEnnemies)): #Vérifie la présence des ennemies capable de tirer (les ennemies en 3ème ligne)
            if self.listeEnnemies[i]!=[]:
                E=self.listeEnnemies[i][-1]
                prob=random()
                if prob<0.01: #Avec 1% de chance a chaque rafréchissement, fait tirer les ennemies
                    Ennemi.shotsE.append(CP.TirEnnemi(canva,E))
            
    def move(self,canva,speed,sens):
    #Fonction qui fait bougé les ennemies | Reçois: le canvas ou sont les ennemies, la vitesse des ennemies et le sens de déplacement des ennemies | Renvoit : le sens et la vitesse possiblement modifiés
    
        g=0
        d=0

        for i in self.listeEnnemies: #Permet d'obtenir le premier ennemies à gauche pour avoir le bord gauche du groupe
            for j in i :
                if j!=0 and g==0:
                    Eg=j
                    r=1

        for i in list(reversed(self.listeEnnemies)): #Permet d'obtenir le premier ennemies à draoite pour avoir le bord droit du groupe
            for j in i:
                if j!=0 and d==0:
                    Ed=j
                    m=1


        xd1,yd,xd2,yd=canva.bbox(Ed) #Permet d'obtenir la coordonnée extreme droite du groupe d'ennemies
        xg1,yg,xg2,yg=canva.bbox(Eg) #Permet d'obtenir la coordonnée extrême gauche du groupe d'ennemies

        if xd2+speed>=900 and sens=="d": #Change le sens de déplacement, augmente la vitesse et abaisse la hauteur des ennemies, s'ils sortent de la zone de jeu
            for i in self.listeEnnemies:
                for j in i:
                    canva.move(j,0,10)
            speed+=0.25
            sens="g"
            return sens,speed

        if xg1-speed<=0 and sens=="g": #Change le sens de déplacement, augmente la vitesse et abaisse la hauteur des ennemies, s'ils sortent de la zone de jeu
            for i in self.listeEnnemies:
                for j in i:
                    canva.move(j,0,10)
            speed+=0.25
            sens="d"
            return sens,speed

        for i in self.listeEnnemies: #Déplace les ennemies à la vitesse définie
            for j in i:
                x1,y1,x2,y2=canva.bbox(j)
                if x2+speed<900 and sens=="d":
                    canva.move(j,speed,0)
                elif x1-speed>0 and sens=="g":
                    canva.move(j,-speed,0)

        return sens,speed
    
    def Boss (self, boss, canva):
    #Fait apparaitre le boss
        
        self.boss=canva.create_image(450,100, image=boss)

    def BossMouv(self,canva,speed,sens):
    #Gère les déplacement du boss | Reçoit : le canva, la vitesse du boss et le sens de déplacement du boss | Renvoit : le sens et la vitesse possiblement modifiés
        
        x1,y1,x2,y2=canva.bbox(self.boss)

        if x2+speed>=900 and sens=="d": #Change le sens de déplacement du boss, s'il sort de la zone de jeu
            sens="g"
            return sens,speed

        if x1-speed<=0 and sens=="g": #Change le sens de déplacement du boss, s'il sort de la zone de jeu
            sens="d"
            return sens,speed

        if x2+speed<900 and sens=="d": #Déplace le boss à la vitesse définie
            canva.move(self.boss,speed,0)
        elif x1-speed>0 and sens=="g":
            canva.move(self.boss,-speed,0)

        return sens,speed





class Joueur():
#Permet de s'occuper du vaisseau du joueur

    theJoueur=[]    #Tableau qui contiendra le vaisseau du joueur

    def __init__(self, root, x, y):
    #Fait apparaitre le joueur | Reçoit : la fenêtre etles coordonnéespour positioner le joueur

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

        

    #Fonction rattachées au touches du claviers par bindPlayer (module méta), permet de savoir quelle direction le joueur essaye d'aller | Reçoit : les information du clavier et le canva
    def vaRightRelease(self, event, canva): 
        self.vaRightBool=False
    def vaRightPress(self, event, canva):
        self.vaRightBool=True
    def vaLeftRelease(self, event, canva):
        self.vaLeftBool=False
    def vaLeftPress(self, event, canva):
        self.vaLeftBool=True

    def vaRight(self, canva):
    #Déplace le joueur vers la droite | Reçoit : le canva
       
        x1,y1,x2,y2=canva.bbox(Joueur.theJoueur[0])
        if x2+10<900:
            canva.move(Joueur.theJoueur[0],10,0)
            self.x+=10

    def vaLeft(self, canva):
    #déplace le joueur vers la gauche | Reçoit : le canva
        
        x1,y1,x2,y2=canva.bbox(Joueur.theJoueur[0])
        if x1-10>0:
            canva.move(Joueur.theJoueur[0],-10,0)
            self.x-=10
            
    def tir(self, event,canva,ennemi,scoreVar):
    #Tir un projectile du joueur | Recoit : le canva, l'objet ennemie et le score du joueur
        
        if self.shots ==[]:
            self.shots.append(CP.TirAllie(canva,self,ennemi,scoreVar)) #Crée le tir du joueur et donne les information nécessaire a modifier en cas de touche 
