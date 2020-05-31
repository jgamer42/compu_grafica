import pygame
import random
from models import Const
from models.jugador import Jugador
from models.bala import Bala
from models.enemigo import Rival
if __name__ == '__main__':
    pygame.init()

    #NOTE Definicion de variables
    ventana=pygame.display.set_mode([Const.ANCHO,Const.ALTO])
    jugadores=pygame.sprite.Group()
    j=Jugador([300,200],[Const.ANCHO,Const.ALTO])
    jugadores.add(j)
    rivales=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    n=10
    puntos=0
    for i in range(n):
        x=random.randrange((Const.ANCHO-50))
        y=random.randrange((Const.ALTO-150))
        r=Rival([x,y])
        rivales.add(r)
    reloj=pygame.time.Clock()
    fin=False
    #NOTE Ciclo principal
    while not fin:
        #NOTE Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.acelerar(5,0)
                if event.key == pygame.K_LEFT:
                    j.acelerar(-5,0)
                if event.key == pygame.K_UP:
                    j.acelerar(0,-5)
                if event.key == pygame.K_DOWN:
                    j.acelerar(0,5)
                if event.key == pygame.K_z:
                    p=j.RetPos()
                    b=Bala(p,-10,0)
                    balas.add(b)
                if event.key == pygame.K_SPACE:
                    j.frenar()
        #Control

        #NOTE Colision
        ls_col=pygame.sprite.spritecollide(j,rivales,True)
        for r in ls_col:
            puntos += 1
            print(puntos)

        #NOTE Limpieza de memoria
        for b in balas:
            if b.rect.y < -50:
                balas.remove(b)
        #NOTE Refresco
        jugadores.update()
        rivales.update()
        balas.update()
        ventana.fill(Const.NEGRO)
        jugadores.draw(ventana)
        rivales.draw(ventana)
        balas.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
