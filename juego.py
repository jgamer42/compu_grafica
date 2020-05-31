import pygame
import random
import Const
from jugador import Jugador
from bloque import Bloque
if __name__ == '__main__':
    pygame.init()
    jugadores = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    bloque = Bloque([200,400],50,50)
    bloques.add(bloque)
    jugador = Jugador([50,50],bloques)
    jugadores.add(jugador)
    clock = pygame.time.Clock()
    window = pygame.display.set_mode([Const.ANCHO,Const.ALTO])
    game = True
    while(game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jugador.acelerar(-5,0)
                if event.key == pygame.K_RIGHT:
                    jugador.acelerar(5,0)
                if event.key == pygame.K_SPACE:
                    jugador.acelerar(0,-10)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    jugador.frenar()
        jugadores.update()
        bloques.update()
        window.fill(Const.NEGRO)
        jugadores.draw(window)
        bloques.draw(window)
        pygame.display.flip()
        clock.tick(10)

