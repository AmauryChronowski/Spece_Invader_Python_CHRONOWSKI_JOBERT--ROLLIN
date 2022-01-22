import MetaGame as SpInv
import GameElements as GE

class TirShot():
    def __init__(self,canva,person,ennemi,scorevar):
        self.person=person
        self.x=person.x
        self.y=person.y
        self.shot= canva.create_oval(person.x-5,person.y-10-person.imageHeight/2,person.x+5,person.y-person.imageHeight/2,fill='green')
        self.update(canva,ennemi,scorevar)
    
    def update(self,canva,ennemi,scoreVar):
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
                                    scoreVar+=300

                                elif b in [57, 60, 63, 66, 69, 72]:
                                    scoreVar+=200

                                elif b in [56, 59, 62, 65, 68, 71]:
                                    scoreVar+=100

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
                    scoreVar+=1000

            else:
                canva.delete(self.shot)
                self.person.shots.pop()

            return scoreVar


class TireE():
    def __init__(self,canva,entity):
        self.shotE=0
        self.entity=entity
        self.x1,self.y1,self.x2,self.y2=canva.bbox(self.entity)
        self.x=(self.x1+self.x2)/2
        self.y=self.y1+60
        self.shotE= canva.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,fill='red')

        
        
    def updateE(self,canva,vie,frame1,frame2,frame3):
        
        if self.y<=900 and self.y>=0 :
            self.y+=15
            canva.move(self.shotE,0,+15)
            x1,y1,x2,y2=canva.bbox(self.shotE)
            a=canva.find_overlapping(x1,y1,x2,y2)
            b=a[0]
            
            if b!=self.shotE and b in range(55):
                canva.delete(b)
                
                for shot in GE.Ennemi.shotsE:
                    if shot.shotE==self.shotE:
                        GE.Ennemi.shotsE.remove(shot)
                
                canva.delete(self.shotE)
                GE.Obstacle.listeobstacle[b//3-1].pop()
                
            if b==GE.Joueur.theJoueur[0]:
                if vie == 3:
                    frame3.destroy()
                if vie == 2:
                    frame2.destroy()
                if vie == 1:
                    frame1.destroy()              
                vie-=1
                for shot in GE.Ennemi.shotsE:
                    if shot.shotE==self.shotE:
                        GE.Ennemi.shotsE.remove(shot)
                canva.delete(self.shotE)
        return vie     
