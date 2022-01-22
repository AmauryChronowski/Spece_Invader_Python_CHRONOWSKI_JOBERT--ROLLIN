# -*- coding: utf-8 -*-

# Header

"""

Programme secondaire du projet SpaceInvader

Que fait ce programme : Comptient les classes de Tir du joueur et des ennemis:
                                - TirAllie
                                - TirEnnemi
                        (Les Projectiles)

Créateurs : Amaury CHRONOWSKI / Gabin JOBERT--ROLLIN

Date de réalisation: 15/11/2021 - 22/01/2022

Que reste-t-il à faire : -Amélioration des tir du boss pour les rendre plus imprévisible

"""
#Bibliothèques personelles
import GameElements as GE

class TirAllie():
#Classe pour s'occuper du tir du joueur

    def __init__(self,canva,person,ennemi,scorevar):
    #Crée un tir | Reçoit : le canva, l'objet ennemies nécessaire en cas de touche et le score à rafréchire en cas de touche
        
        self.person=person
        self.x=person.x
        self.y=person.y
        self.shot= canva.create_oval(person.x-5,person.y-10-person.imageHeight/2,person.x+5,person.y-person.imageHeight/2,fill='green') #Crée le projectile allié
        self.update(canva,ennemi,scorevar)
    
    def update(self,canva,ennemi,scoreVar):
    #Actualise la position du projectile | Reçoit : le canva, l'objet ennemies nécessaire en cas de touche et le score à rafréchire en cas de touche | Retourne : le score possiblement modifié
            
            if self.y<=900 and self.y>=0: #Vérifie que le projectile est encore dans la zone de jeu
                self.y-=15
                canva.move(self.shot,0,-15) #Fait bouger le projectile vres le haut
                x1,y1,x2,y2=canva.bbox(self.shot)

                a=canva.find_overlapping(x1,y1,x2,y2) #Détecte si quelque chose rentre en contacte du projectile
                b=a[0]

                if b!=self.shot and b in range(56,74): #Le projectile n'affecte que les ennemies

                    self.person.shots.pop()
                    canva.delete(self.shot) #Détruit le projectile
                    
                    k=0
                    for i in ennemi.listeEnnemies: #premmet d'attribuer le bon nombre de point à la bonne cible
                        u=0
                        for j in i:
                            if j==b:
                                if b in [58, 61, 64, 67, 70, 73]:
                                    scoreVar+=300

                                elif b in [57, 60, 63, 66, 69, 72]:
                                    scoreVar+=200

                                elif b in [56, 59, 62, 65, 68, 71]:
                                    scoreVar+=100

                                ennemi.listeEnnemies[k].pop(u) #Suprime le bon element de la bonne fille d'ennemie
                                canva.delete(b)  
                            else:
                                u+=1
                        k+=1

                elif b==ennemi.boss and ennemi.bossvie==3: #Gère le comporemant des tirs contre le boss quand il est pleine vie
                    ennemi.bossvie-=1
                    canva.delete(self.shot)
                    self.person.shots.pop()

                    x1,y1,x2,y2=canva.bbox(ennemi.boss)
                    x=(x2+x1)/2
                    y=(y2+y1)/2

                    canva.delete(ennemi.boss)
                    ennemi.boss=canva.create_image(x,100, image=ennemi.imgboss1) #Remplace la précedante image de boss par la suivante au même endroit

                elif b==ennemi.boss and ennemi.bossvie==2: #Gère le comporemant des tirs contre le boss quand il est en deuxieme phase
                    ennemi.bossvie-=1
                    canva.delete(self.shot)
                    self.person.shots.pop()

                    x1,y1,x2,y2=canva.bbox(ennemi.boss)
                    x=(x2+x1)/2
                    y=(y2+y1)/2

                    canva.delete(ennemi.boss)
                    ennemi.boss=canva.create_image(x,100, image=ennemi.imgboss2 ) #Remplace la précedante image de boss par la suivante au même endroit

                elif b==ennemi.boss and ennemi.bossvie==1: #Gere le comportemant du tir quand le boss meurt
                    ennemi.bossvie-=1
                    canva.delete(self.shot)
                    self.person.shots.pop() #Détruit le boss
                    scoreVar+=1000

            else: #Détruit le tir s'il y est en dehors de la zone de jeu
                canva.delete(self.shot)
                self.person.shots.pop()

            return scoreVar


class TirEnnemi():
#Classe pour s'occuper du tir des ennemies

    def __init__(self,canva,entity):
    #Crée un tir | Reçoit : le canva et l'ennemie qui tir

        self.shotE=0
        self.entity=entity
        self.x1,self.y1,self.x2,self.y2=canva.bbox(self.entity)
        self.x=(self.x1+self.x2)/2
        self.y=self.y1+60
        self.shotE= canva.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,fill='red') #Crée le tir ennemies

        
        
    def updateE(self,canva,vie,frame1,frame2,frame3):
    #Actualise la position des projectiles ennemi | Reçoit : le canva, la vie du joueur et les frame contenant les coeurs représentant la vie du joueur | Renvoit : la vie du joueur
        
        if self.y<=900 and self.y>=0 : #Vérifie que le tie est encore dans la zone de jeu
            self.y+=15
            canva.move(self.shotE,0,+15) #Déplace le tir vers le bas

            x1,y1,x2,y2=canva.bbox(self.shotE)
            a=canva.find_overlapping(x1,y1,x2,y2) #Détecte si quelque chose rentre en contacte du projectile
            b=a[0]
            
            if b!=self.shotE and b in range(55): #Détruit une brique d'obstacle si elle est touchée
                canva.delete(b) #Détruit la brique
                
                for shot in GE.Ennemi.shotsE:
                    if shot.shotE==self.shotE:
                        GE.Ennemi.shotsE.remove(shot) #Enleve le tir de la liste la qui a toucher la brique
                canva.delete(self.shotE)

                GE.Obstacle.listeobstacle[b//3-1].pop() #Enleve la brique de la pile de brique
                
            if b==GE.Joueur.theJoueur[0]: #Si le joueur est touché enlève une vie au compteur
                #Détruit les frames contenant les coeur une par une
                if vie == 3:
                    frame3.destroy()
                if vie == 2:
                    frame2.destroy()
                if vie == 1:
                    frame1.destroy()

                vie-=1 #Enleve une vie

                for shot in GE.Ennemi.shotsE: #Enleve le tir de la liste la qui a toucher le joueur
                    if shot.shotE==self.shotE:
                        GE.Ennemi.shotsE.remove(shot)
                canva.delete(self.shotE)

        return vie
