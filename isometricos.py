import pygame
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
c1_1 = mi_lib.transformada_polar_cartesiana([150,30])
c1_2 = mi_lib.transformada_desplazamiento(c1_1,0,100)
aux = mi_lib.transformada_polar_cartesiana([100,30])
c1_3 = mi_lib.transformada_desplazamiento(aux,0,100)
c1_4 = mi_lib.transformada_desplazamiento(aux,0,50)

c2_1 = mi_lib.transformada_polar_cartesiana([150,150])
c2_2 = mi_lib.transformada_desplazamiento(c2_1,0,150)
aux = mi_lib.transformada_polar_cartesiana([100,150])
c2_3 = mi_lib.transformada_desplazamiento(aux,0,150)
c2_4 = mi_lib.transformada_desplazamiento(aux,0,50)

s1_1 = mi_lib.transformada_polar_cartesiana([100,30])
cs1_1 = mi_lib.transformada_r2([0,50],ORIGEN)
cs1_2 = mi_lib.transformada_r2(c1_4,ORIGEN)
cs1_4 = mi_lib.transformada_r2(c2_4,ORIGEN)
cs1_3 = mi_lib.transformada_r2(s1_1,cs1_4)

cs2_1 = mi_lib.transformada_r2(c1_2,ORIGEN)
s2_2 = mi_lib.transformada_polar_cartesiana([100,150])
cs2_2 = mi_lib.transformada_r2(s2_2,cs2_1)
cs2_4 = mi_lib.transformada_r2(c1_3,ORIGEN)
s2_3 = mi_lib.transformada_polar_cartesiana([100,150])
cs2_3 = mi_lib.transformada_r2(s2_3,cs2_4)

aux = mi_lib.transformada_pantalla(cs2_2,ORIGEN)
s3_1 = mi_lib.transformada_desplazamiento(aux,0,50)
cs3_1 = mi_lib.transformada_r2(s3_1,ORIGEN)
cs3_2 = mi_lib.transformada_r2(c2_3,ORIGEN)
cs3_3 = mi_lib.transformada_r2(c2_2,ORIGEN)
s3_4 = mi_lib.transformada_polar_cartesiana([150,30])
cs3_4 = mi_lib.transformada_r2(s3_4,cs3_3)



superior_1 = [cs1_1,cs1_2,cs1_3,cs1_4]
superior_2 = [cs2_1,cs2_2,cs2_3,cs2_4]
superior_3 = [cs3_1,cs3_2,cs3_3,cs3_4]
cara_1 = [[0,0],c1_1,c1_2,c1_3,c1_4,[0,50]]
cara_2 = [[0,0,],c2_1,c2_2,c2_3,c2_4,[0,50]]
pantalla_cara1 = []
pantalla_cara2 = []
for i in cara_1:
    punto = mi_lib.transformada_r2(i,ORIGEN)
    pantalla_cara1.append(punto)
for i in cara_2:
    punto = mi_lib.transformada_r2(i,ORIGEN)
    pantalla_cara2.append(punto)

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.draw.polygon(ventana,[255,255,255],pantalla_cara1,1)
        pygame.draw.polygon(ventana,[255,255,255],pantalla_cara2,1)
        pygame.draw.polygon(ventana,[255,255,255],superior_1,1)
        pygame.draw.polygon(ventana,[255,255,255],superior_2,1)
        pygame.draw.polygon(ventana,[255,255,255],superior_3,1)
        pygame.draw.line(ventana,[255,255,255],pantalla_cara1[0],pantalla_cara1[5],1)
        pygame.draw.line(ventana,[255,255,255],cs2_3,cs1_3 )
        pygame.draw.line(ventana,[255,255,255],cs3_1,cs2_2 )
        pygame.display.flip()
