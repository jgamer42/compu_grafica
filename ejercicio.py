import pygame
import math
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
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
                pygame.draw.circle(ventana,[255,255,255],event.pos,2)
                print(event.pos)
                cartesiano = mi_lib.transformada_pantalla(list(event.pos),ORIGEN)
                print(cartesiano)
                revisar = mi_lib.transformada_r2(cartesiano,ORIGEN)
                print(revisar)
        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.display.flip()
