import pygame
#from models import Const
import Const

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos,lista_col):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(Const.BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.colisiones = lista_col

    def RetPos(self):
        x=self.rect.x
        return [x,self.rect.y]

    def update(self):
        self.rect.x+=self.velx
        lista_col = pygame.sprite.spritecollide(self,self.colisiones,False)
        for i in lista_col:
            print("hola")
            if self.velx != 0:
                self.velx = 0
            if self.vely != 0:
                self.vely = 0
        
        self.rect.y+=self.vely
        self.scroll()
        self.gravedad()
        if self.rect.bottom > Const.ANCHO:
            self.rect.bottom = Const.ALTO
            self.vely = 0

    def gravedad(self):
        if self.vely == 0:
            self.vely = Const.GRAVEDAD
        else:
            self.vely += Const.GRAVEDAD

    def frenar(self):
        self.velx=0

    def acelerar(self,x,y):
        self.velx = 0
        self.vely = 0
        self.velx += x
        self.vely += y

    def scroll(self):
        if(self.rect.right < 0):
            self.rect.x = Const.ANCHO
        if(self.rect.left > Const.ANCHO):
            self.rect.x = 0