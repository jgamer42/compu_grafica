import pygame
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
puntos = [[100,50],[200,50],[200,100]]
puntos=[[50,50],[150,150],[150,50]]
puntos_pantalla=[]
x = 0
for i in puntos:
    punto = mi_lib.transformada_r2(i,ORIGEN)
    puntos_pantalla.append(punto)
if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        puntos_dibujar = []
        #captura todos los eventos
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    aux_punto=[]
                    puntos_pantalla=[]
                    for i in puntos:
                        aux=mi_lib.transformada_desplazamiento(i,10,0)
                        aux_dibujar = mi_lib.transformada_r2(aux,ORIGEN)
                        aux_punto.append(aux)
                        puntos_pantalla.append(aux_dibujar)
                    puntos = []
                    puntos = aux_punto
                    ventana.fill([0,0,0])
                if event.key == pygame.K_LEFT:
                    aux_punto=[]
                    puntos_pantalla=[]
                    for i in puntos:
                        aux=mi_lib.transformada_desplazamiento(i,-10,0)
                        aux_dibujar = mi_lib.transformada_r2(aux,ORIGEN)
                        aux_punto.append(aux)
                        puntos_pantalla.append(aux_dibujar)
                    puntos = []
                    puntos = aux_punto
                    ventana.fill([0,0,0])
                if event.key == pygame.K_UP:
                    aux_punto=[]
                    puntos_pantalla=[]
                    for i in puntos:
                        aux=mi_lib.transformada_desplazamiento(i,0,10)
                        aux_dibujar = mi_lib.transformada_r2(aux,ORIGEN)
                        aux_punto.append(aux)
                        puntos_pantalla.append(aux_dibujar)
                    puntos = []
                    puntos = aux_punto
                    ventana.fill([0,0,0])
                if event.key == pygame.K_DOWN:
                    aux_punto=[]
                    puntos_pantalla=[]
                    for i in puntos:
                        aux=mi_lib.transformada_desplazamiento(i,0,-10)
                        aux_dibujar = mi_lib.transformada_r2(aux,ORIGEN)
                        aux_punto.append(aux)
                        puntos_pantalla.append(aux_dibujar)
                    puntos = []
                    puntos = aux_punto
                    ventana.fill([0,0,0])
        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.draw.polygon(ventana,[255,255,255],puntos_pantalla,2)
        pygame.display.flip()
