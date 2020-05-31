import pygame
import const
class Bloque(pygame.sprite.Sprite):
    def __init__(self,pos,dim):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dim)
        self.image.fill(const.BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.hit_radio_bot = self.rect.bottom - const.HIT_RANGE
        self.hit_radio_top = self.rect.bottom + const.HIT_RANGE

    def update(self):
        self.rect.x = self.rect.x + self.velx