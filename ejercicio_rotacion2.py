import pygame
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
grados = 15
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
                pygame.draw.line(ventana,[255,255,255],ORIGEN,list(event.pos),2)
                punto_fijo = mi_lib.transformada_pantalla(list(event.pos),ORIGEN)
                while grados <= 360:
                    aux = []
                    aux.append(punto_fijo)
                    punto = mi_lib.rotacion_horaria(aux,grados)
                    punto = mi_lib.transformada_r2(punto[0],ORIGEN)
                    pygame.draw.line(ventana,[255,255,255],ORIGEN,punto,2)
                    grados += 2
        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.display.flip()
