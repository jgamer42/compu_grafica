import pygame
#from models import Const
import Const

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos,limites):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(Const.BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y= (limites[0]-self.rect.height) - 10
        self.velx=0
        self.vely=0
        self.limites=limites
        #self.vely=0
        self.colisiones=None

    def RetPos(self):
        x=self.rect.x
        y=self.rect.y - 20
        return [x,y]

    def update(self):
        self.rect.x+=self.velx
        
        if self.rect.y < 0-self.rect.height:
                self.rect.y=self.limites[1]

        if self.rect.y > self.limites[1]:
            self.rect.y=0-self.rect.height+10

        if self.rect.x >= self.limites[0]-150:
            self.velx=0
            self.rect.x = self.limites[0]-149
            Const.f_velx=-5
        else:
            Const.f_velx= 0
        if self.rect.x <= 0:
            self.rect.x=0
            self.velx=0
        ls_col = pygame.sprite.spritecollide(self,self.colisiones,False)
        for i in ls_col:
            if self.velx >0:
                if self.rect.right > i.rect.left:
                    self.rect.right=i.rect.left
                    self.velx=0
            else:
                if self.rect.left < i.rect.right:
                    self.rect.left=i.rect.right
                    self.velx=0      
        self.rect.y+=self.vely

        ls_col = pygame.sprite.spritecollide(self,self.colisiones,False)
        for i in ls_col:
            if self.vely > 0:
                if self.rect.bottom > i.rect.top:
                    self.rect.bottom = i.rect.top
                    self.vely=0
            else:
                if self.rect.top < i.rect.bottom:
                        self.rect.top = i.rect.bottom
                        self.vely=0
                        
    def acelerar(self,x,y):
        self.velx=0
        self.vely=0
        self.velx += x
        self.vely += y

    def frenar(self):
        self.velx=0
        self.vely=0
        Const.f_velx=0
