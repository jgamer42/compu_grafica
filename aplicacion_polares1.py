import pygame
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
figura = mi_lib.cardiode(75,100)
puntos_pantalla = []
for i in figura:
    punto=mi_lib.transformada_r2(i,ORIGEN)
    puntos_pantalla.append(punto)
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
