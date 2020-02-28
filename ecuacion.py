import pygame
import math
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = [300,300]
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
if __name__ == "__main__":
    print(LIMITES)
    x=-200
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        while x < LIMITES[1]:
            y = 10*x + 15
            punto = [x,y]
            l=mi_lib.transformada_r2(punto,ORIGEN)
            pygame.draw.circle(ventana,[255,255,255],l,2)
            x += 1
        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.display.flip()
