import pygame
from models import Const

class Bala(pygame.sprite.Sprite):
    def __init__(self, pos,vely,velx,color=Const.ROJO):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,30])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vely = vely
        self.velx = velx

    def update(self):
        self.rect.y+=self.vely
