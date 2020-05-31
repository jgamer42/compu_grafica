import pygame
#from models import Const
import const

class Raton(pygame.sprite.Sprite):
    def __init__(self, pos,animations):
        pygame.sprite.Sprite.__init__(self)
        self.velx=0
        self.vely=0
        self.animations = animations
        self.cont = 9
        self.dir = 0
        self.image = self.animations[self.dir][self.cont]
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.radius = 50
    def RetPos(self):
        x=self.rect.x
        y=self.rect.y
        return [x,y]

    def update(self):
        if(self.velx != self.vely):
            self.animate()
        self.scroll()
        self.rect.x += self.velx
        self.rect.y += self.vely

    def animate(self):
        if(self.cont < 11):
            self.cont =self.cont + 1
        else:
            self.cont = 9
        self.image = self.animations[self.dir][self.cont]
    
    def scroll(self):
        if (self.rect.x < 0-self.rect.width):
            self.rect.x = const.ANCHO

        if (self.rect.x > const.ANCHO):
            self.rect.x = 0-self.rect.width

        if(self.rect.y < 0-self.rect.height):
            self.rect.y = const.ALTO

        if(self.rect.y > const.ALTO):
            self.rect.y = 0-self.rect.height