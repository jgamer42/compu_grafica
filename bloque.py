import pygame
import const
import random
class Bloque(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(const.BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.temp = random.randrange(100)
        
    def  update(self):
        self.temp = self.temp-1