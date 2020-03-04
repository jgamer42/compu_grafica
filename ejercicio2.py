#TODO recibir dos puntos y dibujar una recta que cruce
#por ambos puntos
import pygame
import math
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
puntos = []
RELOJ = pygame.time.Clock()
if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        #captura todos los eventos
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(puntos) == 2:
                    m = mi_lib.pendiente(puntos[0],puntos[1])
                    b = mi_lib.desplazamiento(puntos[0],puntos[1],m)
                    while x < LIMITES[1]:
                        y = int(m*x) + b
                        punto = [x,y]
                        x += 10
                        pygame.draw.circle(ventana,[255,255,255],punto,2)
                        print(punto)
                    puntos = []
                else:
                    punto = mi_lib.transformada_r2(list(event.pos),ORIGEN)
                    puntos.append(punto)

        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.display.flip()
