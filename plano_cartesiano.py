import pygame
from mi_lib import *
import sys
ANCHO = 600
ALTO = 600
if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    puntos = []
    #ciclo principal
    while True:
        #captura todos los eventos
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #captura el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(puntos) < 3:
                    if len(puntos) == 0:
                        ventana.fill([0,0,0])
                        origen_x = event.pos[0]
                        origen_y = event.pos[1]
                        dibujar_plano(origen_x,origen_y,ANCHO,ALTO,ventana)
                    puntos.append(event.pos)
                if len(puntos) == 3:
                    ventana.fill([0,0,0])
                    dibujar_plano(origen_x,origen_y,ANCHO,ALTO,ventana)
                    dibujar_triangulo(ventana,puntos)
        pygame.display.flip()
