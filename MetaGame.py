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
import ClasseProjectiles as CP
import GameElements as GE
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
        print(GE.Ennemi.shotsE)
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
        self.freamHeart1 = tk.Frame(self.freamHeartContain, bg = "black")
        self.freamHeart1.pack(side = 'left')

        self.freamHeart2 = tk.Frame(self.freamHeartContain, bg = "black")
        self.freamHeart2.pack(side = 'left')

        self.freamHeart3 = tk.Frame(self.freamHeartContain, bg = "black")
        self.freamHeart3.pack(side = 'right')
        
        #Inssertion des image du coeur dans les frames
        self.Heart1 = tk.Canvas(self.freamHeart1, height = 180, width = 180, bg = "black", highlightthickness = 0)
        self.Heart1.create_image(0, 0, anchor = 'nw', image = self.heartimg)
        self.Heart1.pack(side = "left")
        
        self.Heart2 = tk.Canvas(self.freamHeart2, height = 180, width = 180, bg = "black", highlightthickness = 0)
        self.Heart2.create_image(0, 0, anchor = 'nw', image = self.heartimg)
        self.Heart2.pack(side = "top")
        
        self.Heart3 = tk.Canvas(self.freamHeart3, height = 180, width = 180, bg = "black", highlightthickness = 0)
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
        
        GE.Joueur.theJoueur=[]
        GE.Ennemi.shotsE=[]
        GE.Obstacle.listeobstacle=[]
        
        #Fonction qui lance une partie
        self.startPartie()
        arestart=True
    def gameStart(self): #Fonction qui enclanche la partie | Lance : Fonction qui associe les touches du clavier à des actions et la fonction qui rafréchit en continue du jeu
        
        #Objet utilisés dans les fonctions
        obstacl=GE.Obstacle(self,75,700) #Obstacles protégant le joueur
        player=GE.Joueur(self,450,830) #Elément joeur
        ennemi=GE.Ennemi(self,50,300, self.img1,self.img2,self.img3,self.img5,self.img6) #Différents ennemies utilisés

        self.bindPlayer(player,ennemi,self.scoreVar) #Fonction qui associe les touches du clavier à des actions
        self.gameLoop(player,ennemi,obstacl,1,"d") #Fonction qui rafréchit en continue du jeu

    def gameEnd(self): #Fonction de fin de partie

        #Déstruction de la frame de jeu 
        self.frameGame.destroy()

        #Création de la frame de fin de partie
        self.frameGame = tk.Frame(bg="black")

        #Différentiation entre la victoire et la défaite
        if self.vie != 0:
            self.fin = tk.Label(self.frameGame, text = "You win", fg = "green", bg = "black", font = ("Helvetica", 50))

        if self.vie == 0:
            self.fin = tk.Label(self.frameGame, text = "You lose", fg = "green", bg = "black", font = ("Helvetica", 50))

        self.fin.pack(side = "top")

        #Affichage du score final
        self.scorefin = tk.Label(self.frameGame, text = "Your score is " + str(self.scoreVar), fg = "green", bg = "black", font = ("Helvetica", 50))
        self.scorefin.pack(side = "top")

        #Boutton rejouer
        self.bRejouer = tk.Button(self.frameGame, text = "RESTART", font = ("Helvetica", 50), fg = "green", bg = "black", activebackground = 'green', activeforeground = 'white', highlightcolor = "white", highlightthickness = 4, relief = "flat", highlightbackground = "green", command = self.rejouer)
        self.bRejouer.pack(anchor = "s", expand = "yes")

        #Boutton pour quitter
        self.bQuitter = tk.Button(self.frameGame, text = "QUIT", font = ("Helvetica",50), fg = "green", bg = "black", activebackground = 'green', activeforeground = 'white', highlightcolor = "white", highlightthickness = 4, relief = "flat", highlightbackground = "green", command = self.root.destroy)
        self.bQuitter.pack(anchor = "s", expand = "yes")

        self.frameGame.pack(fill = "both", expand = "yes")

    def gameLoop(self,player,ennemi,obstacl,speed,sens):

        if ennemi.bossvie==0:
            self.gameEnd()
        elif self.vie==0:
            self.gameEnd()
        

        if player.shots != []:
            for shoot in player.shots:
                self.scoreVar=shoot.update(self.canvaGame,ennemi,self.scoreVar)

        if player.vaRightBool ==True:
            player.vaRight(self.canvaGame)
        if player.vaLeftBool ==True:
            player.vaLeft(self.canvaGame)

        for i in ennemi.listeEnnemies:
            if i==[]:
                ennemi.listeEnnemies.pop( ennemi.listeEnnemies.index(i))
                speed+=0.5

        if  ennemi.listeEnnemies!=[]:
            sens,speed=ennemi.move(self.canvaGame,speed,sens)
            ennemi.tire(self.canvaGame)
            if GE.Ennemi.shotsE != []:
                for shoot in GE.Ennemi.shotsE:
                    self.vie=shoot.updateE(self.canvaGame,self.vie,self.freamHeart1,self.freamHeart2,self.freamHeart3)
            self.scoreStr.set(str(self.scoreVar))

        elif ennemi.boss==0 and ennemi.listeEnnemies==[]:
            speed=10
            ennemi.Boss(self.img4,self.canvaGame)
            if GE.Ennemi.shotsE != []:
                for shoot in GE.Ennemi.shotsE:
                    self.vie=shoot.updateE(self.canvaGame,self.vie,self.freamHeart1,self.freamHeart2,self.freamHeart3)
 

        else:
            if GE.Ennemi.shotsE != []:
                for shoot in GE.Ennemi.shotsE:
                    self.vie=shoot.updateE(self.canvaGame,self.vie,self.freamHeart1,self.freamHeart2,self.freamHeart3)
            sens,speed=ennemi.BossMouv(self.canvaGame,speed,sens)

            if self.rafaleNb<=40 and self.rafale=="yes":
                self.rafaleNb+=1              
                GE.Ennemi.shotsE.append(CP.TireE(self.canvaGame,ennemi.boss))

            elif self.rafaleNb>40 and self.rafale=="yes":
                self.rafale="no"
                self.rafaleNb=0

            elif self.rafaleNb<=40 and self.rafale=="no":
                self.rafaleNb+=1

            elif self.rafaleNb>40 and self.rafale=="no":
                self.rafale="yes"
                self.rafaleNb=0

            if GE.Ennemi.shotsE != []:
                for shoot in GE.Ennemi.shotsE:
                    self.vie=shoot.updateE(self.canvaGame,self.vie,self.freamHeart1,self.freamHeart2,self.freamHeart3)
        if ennemi.bossvie!=0 and self.vie!=0 :
            self.canvaGame.after(16,lambda : self.gameLoop(player,ennemi,obstacl,speed,sens))
        elif self.vie==0:
            self.gameEnd()



