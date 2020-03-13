import pygame
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
puntos = mi_lib.figura_pitagorica(100,6)
print(puntos)
puntos_pantalla=[]
for i in puntos:
    print(i)
    punto_aux = mi_lib.transformada_r2(i,ORIGEN)
    puntos_pantalla.append(punto_aux)

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.draw.polygon(ventana,[255,255,255],puntos_pantalla,1)
        pygame.display.flip()
