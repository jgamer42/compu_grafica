#TODO capturar tres puntos y dibujar un triangulo y luego escalarlo cona la rueda del raton
import pygame
import math
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
RELOJ = pygame.time.Clock()
if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    escalamiento = 0.2
    puntos = []
    while True:
        #captura todos los eventos
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if len(puntos) < 3:
                        puntos.append(event.pos)
                if event.button == 4:
                    if len(puntos) < 3:
                        ventana.fill([0,0,0])
                    print("arriba")
                if event.button == 5:
                    if len(puntos) < 3:
                        ventana.fill([0,0,0])
                    print("abajo")
        pygame.draw.polygon(ventana,[255,255,255],puntos,1)
        escalados = mi_lib.transformada_escalamiento(puntos,(2,2))
        pygame.draw.polygon(ventana,[255,255,255],escalados,1)
        escalados = mi_lib.transformada_escalamiento(puntos,(0.5,0.5))
        pygame.draw.polygon(ventana,[255,255,255],escalados,1)
        pygame.display.flip()
