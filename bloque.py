import pygame
import Const

class Bloque(pygame.sprite.Sprite):
    def __init__(self,pos,d_an,d_al,color=Const.VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([d_an,d_al])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx=0

    def update(self):
        self.velx = Const.f_velx
        self.rect.x = self.rect.x + self.velx