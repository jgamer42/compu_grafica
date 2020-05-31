import pygame
import random
import Const
from jugador import Jugador
from bloque import Bloque
if __name__ == '__main__':
    pygame.init()

    #NOTE Definicion de variables
    ventana=pygame.display.set_mode([Const.ANCHO,Const.ALTO])
    fondo = pygame.image.load("fondo.jpg")
    info = fondo.get_rect()
    jugadores=pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    j=Jugador([300,200],[Const.ANCHO,Const.ALTO])
    jugadores.add(j)
    b=Bloque([200,200],200,120)
    bloques.add(b)
    j.colisiones=bloques
    #variables del fondo
    f_posx=0
    f_posy=0
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
                if event.key == pygame.K_SPACE:
                    j.frenar()
        #Control
        #NOTE Colision
        #NOTE Limpieza de memoria
        #NOTE Refresco
        f_posx= Const.f_velx + f_posx
        jugadores.update()
        bloques.update()
        ventana.blit(fondo,[f_posx,f_posy])
        jugadores.draw(ventana)
        bloques.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
