import pygame
#from models import Const
import const

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos,animations):
        pygame.sprite.Sprite.__init__(self)
        self.velx=0
        self.vely=0
        self.animations = animations
        self.cont = 0
        self.action = 1
        self.image = self.animations[self.action][self.cont]
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]


    def update(self):
        self.animate()
        self.scroll()
        self.rect.x += self.velx
        self.rect.y = self.rect.y + self.vely
    
    def animate(self):
        if(self.action == 1):
            self.idle_animation()
        elif(self.action == 2):
            self.hit_animation()

    def scroll(self):
        if (self.rect.x < 0-self.rect.width):
            self.rect.x = const.ANCHO

        if (self.rect.x > const.ANCHO):
            self.rect.x = 0-self.rect.width

        if(self.rect.bottom < const.LIMY + 50):
            self.vely=0
            self.rect.y= self.rect.y + 1

        if(self.rect.bottom >= const.ALTO):
            self.vely=0
            self.rect.y = self.rect.y-1

    def acelerar(self,x,y):
        self.velx=0
        self.vely=0
        self.velx += x
        self.vely += y

    def frenar(self):
        self.velx=0
        self.vely=0

    def hit_animation(self):
        if(self.cont < 2):
            self.cont =self.cont + 1
        else:
            self.cont = 0
            self.action=1
        self.image = self.animations[self.action][self.cont]

    def idle_animation(self):
        if(self.cont < 3):
                self.cont = self.cont + 1
        else:
            self.cont = 0
            self.action = 1
        self.image = self.animations[self.action][self.cont]
    
    def swap_animation(self,action):
        self.action = action

    def review_combo(self,combo):
        if(len(combo) >= 3):
            if combo == "ccc":
                print("ey")
            else:
                combo = ""
