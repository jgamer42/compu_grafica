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
    j=Jugador([300,200])
    jugadores.add(j)
    rivales=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas_rival=pygame.sprite.Group()
    n=10
    puntos=0
    for i in range(n):
        x=random.randrange((Const.ANCHO-50))
        y=random.randrange((Const.ALTO-150))
        velx=5
        temp=random.randrange(40,100)
        r=Rival([x,y],temp,velx,0)
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
        ls_col=pygame.sprite.spritecollide(j,rivales,False)
        for r in ls_col:
            puntos -= 10
            print(puntos)

        #NOTE Limpieza de memoria
        for b in balas:
            #colision proyectil
            ls_r = pygame.sprite.spritecollide(b,rivales,True)
            if b.rect.y < -50:
                balas.remove(b)
            #modificador de balas
            for r in ls_r:
                balas.remove(b)

        for b in balas_rival:
            ls_r = pygame.sprite.spritecollide(b,jugadores,True)
            if b.rect.y > Const.ALTO:
                balas_rival.remove(b)

        #NOTE control rivales
        for r in rivales:
            if(r.temp<0):
                pos=r.get_pos()
                b = Bala(pos,10,0,Const.AMARILLO)
                r.temp = random.randrange(40,100)
                balas_rival.add(b)

        #NOTE Refresco
        jugadores.update()
        rivales.update()
        balas.update()
        balas_rival.update()
        ventana.fill(Const.NEGRO)
        jugadores.draw(ventana)
        rivales.draw(ventana)
        balas.draw(ventana)
        balas_rival.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
