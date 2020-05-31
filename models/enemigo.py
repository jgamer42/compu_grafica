import pygame
from models import Const

class Rival(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(Const.VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        pass
