import pygame
import math
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
RELOJ = pygame.time.Clock()
#TODO hacer que el triangulo se mueva con la tecla
if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        puntos=[[100,200],[310,200],[200,350]]
        transformada=[]
        #captura todos los eventos
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print(puntos)
                    indice = 0
                    for i in puntos:
                        i[0] += 60
                    print(puntos)
        ventana.fill([0,0,0])
        pygame.draw.polygon(ventana,[255,255,255],puntos)
        for i in puntos:
            punto=mi_lib.transformada_r2(i,ORIGEN)
            transformada.append(punto)
        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.draw.polygon(ventana,[255,255,255],transformada)
        pygame.display.flip()
        RELOJ.tick(60)
