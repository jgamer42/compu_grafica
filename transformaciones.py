import pygame
import math
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
RELOJ = pygame.time.Clock()
p1 = 100
p2 = 310
p3 = 200
if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        puntos=[[p1,200],[p2,200],[p3,350]]
        transformada = []
        #captura todos los eventos
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ventana.fill([0,0,0])
                    p1 += 60
                    p2 += 60
                    p3 += 60
        #punto normal
        pygame.draw.polygon(ventana,[255,255,255],puntos)
        for i in puntos:
            punto=mi_lib.transformada_r2(i,ORIGEN)
            transformada.append(punto)
        #punto transformado
        pygame.draw.polygon(ventana,[255,255,255],transformada)
        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.display.flip()
        RELOJ.tick(60)
