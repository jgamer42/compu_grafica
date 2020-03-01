import pygame
NEGRO = [0,0,0]
VERDE = [0,255,0]
#NOTE funcion para dibujar un plano cartesiano
# entradas: punto de origen del plano,tamaño de la pantalla,ventana a dibujar
# proceso: dibuja un plano cartesiano
# salida: no posee salidas
def dibujar_plano(origen,pantalla,ventana):
    pygame.draw.line(ventana, [255,255,255],(0,origen[1]),(pantalla[0],origen[1]),2)
    pygame.draw.line(ventana, [255,255,255],(origen[0],0),(origen[0],pantalla[1]),2)

#NOTE funcion para dibujar puntos respecto a un origen
# entradas: ventana en cual va a dibujar, punto a dibujar, origen del plano
# proceso: realiza la transformacion lineal del punto de cartesiano a pantalla
# salida: no posee salidas
def dibujo_en_plano(ventana,pos,origen):
    x = origen[0] + pos[0]
    pos[1] = pos[1] * (-1)
    y = origen[1] + pos[1]
    pygame.draw.circle(ventana,[255,255,255],[x,y],2)

#NOTE funcion para dibujar puntos respecto a un origen
# entradas: punto a dibujar, origen del plano
# proceso: realiza la transformacion lineal del punto de cartesiano a pantalla
# salida: el punto transformado a la coordenada en pantalla
def transformada_r2(pos,origen):
    x = origen[0] + pos[0]
    pos[1] = pos[1] * (-1)
    y = origen[1] + pos[1]
    punto = [x,y]
    return punto

#NOTE funcion para unir triangulos entre si por medio de puntos comunes
# entradas: ventana, puntos del primer triangulo, puntos del segundo triangulo
# proceso: dibujar lineas entre puntos comunes
# salida: ninguna
def integrador(v,f1,f2):
    pygame.draw.line(v,[255,255,255],f1[0],f2[0])
    pygame.draw.line(v,[255,255,255],f1[1],f2[1])
    pygame.draw.line(v,[255,255,255],f1[2],f2[2])
