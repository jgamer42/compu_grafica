import pygame
from mi_lib import *
import sys
ANCHO = 600
ALTO = 600
if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    puntos = []
    reloj = pygame.time.Clock()
    while True:
        #captura todos los eventos
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #captura el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                puntos.append(list(event.pos))
                if len(puntos)==4:
                    pygame.draw.polygon(ventana,VERDE,puntos,1)
                    while puntos[0][0] < ANCHO:
                        ventana.fill(NEGRO)
                        for i in puntos:
                            i[0] += 10
        pygame.draw.polygon(ventana,VERDE,puntos,1)
        pygame.display.flip()
        reloj.tick(60)
