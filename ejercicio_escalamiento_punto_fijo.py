import pygame
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
puntos = [[50,50],[150,100],[150,150]]
puntos_pantalla=[]
x = 0
for i in puntos:
    punto = mi_lib.transformada_r2(i,ORIGEN)
    puntos_pantalla.append(punto)

aux_pantalla=[]
puntos=mi_lib.escalamiento_punto_fijo(puntos,2)
for i in puntos:
    punto = mi_lib.transformada_r2(i,ORIGEN)
    aux_pantalla.append(punto)

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
        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.draw.polygon(ventana,[255,255,255],puntos_pantalla,2)
        pygame.draw.polygon(ventana,[255,255,255],aux_pantalla,2)
        pygame.display.flip()
