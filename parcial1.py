import pygame
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,400)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
#punto incial
p0c = [0,0]
#punto 1 de la cara frontal 1
f1p1c = mi_lib.transformada_polar_cartesiana([50,30])
f1p1p = mi_lib.transformada_r2(f1p1c,ORIGEN)
#punto 2 de la cara frontal 1
f1p2c = mi_lib.transformada_polar_cartesiana([150,30])
f1p2p = mi_lib.transformada_r2(f1p2c,ORIGEN)
#punto 3 de la cara frontal 1
f1p3c = mi_lib.transformada_desplazamiento(f1p2c,0,50)
f1p3p = mi_lib.transformada_r2(f1p3c,ORIGEN)
f1p4c = mi_lib.transformada_polar_cartesiana([50,210])
f1p4p = mi_lib.transformada_r2(f1p4c,f1p3p)
#cara frontal 1
frontal_1 = [f1p1p,f1p2p,f1p3p,f1p4p]


#punto 1 cara frontal 2
f2p1c = mi_lib.transformada_polar_cartesiana([50,150])
f2p1p = mi_lib.transformada_r2(f2p1c,ORIGEN)
#punto 2 cara frontal 2
f2p2c = mi_lib.transformada_polar_cartesiana([50,150])
f2p2p = mi_lib.transformada_r2(f2p2c,f1p1p)
#punto 3 cara frontal 2
f2p3c = mi_lib.transformada_polar_cartesiana([50,150])
f2p3p = mi_lib.transformada_r2(f2p3c,f1p4p)
#punto 4 cara frontal 2
f2p4c = mi_lib.transformada_polar_cartesiana([50,150])
f2p4p = mi_lib.transformada_r2(f2p3c,f1p3p)
#punto 5 cara frontal 2
f2p5c = [0,50]
f2p5p = mi_lib.transformada_r2(f2p5c,f2p4p)
#punto 6 cara frontal 2
f2p6c = [0,50]
f2p6p = mi_lib.transformada_r2(f2p5c,f2p3p)
frontal_2 = [f2p1p,f2p2p,f2p3p,f2p4p,f2p5p,f2p6p]

#punto 1 cara frontal 3
f3p1c = mi_lib.transformada_polar_cartesiana([50,150])
f3p1p = mi_lib.transformada_r2(f3p1c,f2p1p)
#punto 2 cara frontal 3
f3p2p = mi_lib.transformada_desplazamiento(f3p1p,0,-50)
#punto 3 cara frontal 3
f3p3c = mi_lib.transformada_polar_cartesiana([50,150])
f3p3p = mi_lib.transformada_r2(f3p3c,f2p6p)
#punto 4 cara frontal 3
f3p4c = mi_lib.transformada_polar_cartesiana([50,30])
f3p4p = mi_lib.transformada_r2(f3p4c,f3p3p)
#punto 5 cara frontal 3
f3p5p = mi_lib.transformada_desplazamiento(f3p4p,0,-50)
#punto 6 cara frontal 3
f3p6p = mi_lib.transformada_desplazamiento(f3p3p,0,-50)
frontal_3=[f3p1p,f3p3p,f3p4p,f3p5p,f3p6p,f3p2p]

#punto 1 cara superior 3
s3p1c = mi_lib.transformada_polar_cartesiana([50,150])
s3p1p = mi_lib.transformada_r2(s3p1c,f3p6p)
#punto 2 cara superior 3
s3p2p = mi_lib.transformada_r2(s3p1c,f3p5p)
superior_3 = [f3p6p,f3p5p,s3p2p,s3p1p]
superior_2 = [f2p6p,f2p5p,f3p4p,f3p3p]
superior_1 = [f1p4p,f1p3p,f2p4p,f2p3p]

#punto 1 lateral
l1p1c  = mi_lib.transformada_polar_cartesiana([50,150])
l1p1p = mi_lib.transformada_r2(l1p1c,f3p2p)
#punto 2 lateral
l1p2p = mi_lib.transformada_desplazamiento(l1p1p,0,50)
lateral_1 = [f3p1p,l1p2p,l1p1p,f3p2p]
lateral_2 = [f1p1p,f1p4p,f2p3p,f2p2p]
lateral_3 = [f2p1p,f2p6p,f3p3p,f3p1p]
lateral_4 = [f3p2p,f3p6p,s3p1p,l1p1p]


vista_superior = [[0,150],[150,150],[150,50],[0,50],[50,50],[50,0],[150,0],[150,50],[0,50]]
vista_superior_pantalla = []
for i in vista_superior:
    aux = mi_lib.transformada_r2(i,[50,ALTO-50])
    vista_superior_pantalla.append(aux)

vista_frontal = [[0,0],[0,50],[100,150],[150,150],[150,0]]
vista_frontal_pantalla = []
for i in vista_frontal:
    aux = mi_lib.transformada_r2(i,[250,ALTO-50])
    vista_frontal_pantalla.append(aux)

vista_lateral = [[0,0],[0,150],[50,150],[50,0],[50,100],[100,100],[100,0],[150,0],[150,50],[100,50],[100,0]]
vista_lateral_pantalla=[]
for i in vista_lateral:
    aux = mi_lib.transformada_r2(i,[450,ALTO-50])
    vista_lateral_pantalla.append(aux)

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                frontal_1 = mi_lib.escalamiento_punto_fijo(frontal_1,0.2)
                frontal_2 = mi_lib.escalamiento_punto_fijo(frontal_2,0.2)
                frontal_3 = mi_lib.escalamiento_punto_fijo(frontal_3,0.2)
                superior_1 = mi_lib.escalamiento_punto_fijo(superior_1,0.2)
                superior_2 = mi_lib.escalamiento_punto_fijo(superior_2,0.2)
                superior_3 = mi_lib.escalamiento_punto_fijo(superior_3,0.2)
                lateral_1 = mi_lib.escalamiento_punto_fijo(lateral_1,0.2)
                lateral_2 = mi_lib.escalamiento_punto_fijo(lateral_2,0.2)
                lateral_3 = mi_lib.escalamiento_punto_fijo(lateral_3,0.2)
                lateral_4 = mi_lib.escalamiento_punto_fijo(lateral_4,0.2)
                ventana.fill([0,0,0])
        pygame.draw.polygon(ventana,[255,255,255],frontal_1)
        pygame.draw.polygon(ventana,[255,255,255],frontal_2)
        pygame.draw.polygon(ventana,[255,255,255],frontal_3)
        pygame.draw.polygon(ventana,[255,240,9],superior_1)
        pygame.draw.polygon(ventana,[255,240,9],superior_2)
        pygame.draw.polygon(ventana,[255,240,9],superior_3)
        pygame.draw.polygon(ventana,[255,1,1],lateral_1)
        pygame.draw.polygon(ventana,[249,190,87],lateral_2)
        pygame.draw.polygon(ventana,[249,190,87],lateral_3)
        pygame.draw.polygon(ventana,[249,190,87],lateral_4)
        pygame.draw.polygon(ventana,[255,240,9],vista_superior_pantalla)
        pygame.draw.polygon(ventana,[255,255,255],vista_frontal_pantalla)
        pygame.draw.polygon(ventana,[255,1,1],vista_lateral_pantalla)
        pygame.display.flip()
