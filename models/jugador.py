import pygame
from models import Const

class Jugador(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(Const.BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y= (Const.ANCHO-self.rect.height) - 10
        self.velx=0
        self.vely=0
        self.vida=0

    def RetPos(self):
        x=self.rect.x
        y=self.rect.y - 20
        return [x,y]

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        #scrolling
        if self.rect.x > Const.ANCHO:
            self.rect.x=0-self.rect.width+10
        if self.rect.x < 0-self.rect.width:
            self.rect.x=Const.ANCHO
        if self.rect.y < 0-self.rect.height:
            self.rect.y=Const.ALTO
        if self.rect.y > Const.ALTO:
            self.rect.y=0-self.rect.height+10

    def acelerar(self,x,y):
        self.velx=0
        self.vely=0
        self.velx += x
        self.vely += y

    def frenar(self):
        self.velx=0
        self.vely=0
