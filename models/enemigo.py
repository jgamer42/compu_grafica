import pygame
from models import Const

class Rival(pygame.sprite.Sprite):

    def __init__(self, pos,temp,velx,vely):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(Const.VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=velx
        self.vely=vely
        self.temp=temp

    def update(self):
        self.temp = self.temp - 1
        self.rect.x += self.velx
        if(self.rect.x > Const.ANCHO - self.rect.width):
            self.rect.x = Const.ANCHO -self.rect.width
            self.velx = -1 * self.velx
        if(self.rect.x < 0-self.rect.width):
            self.rect.x = 0-self.rect.width
            self.velx = -1 * self.velx

    def get_pos(self):
        x = self.rect.x + 20
        y = self.rect.bottom
        return([x,y])
