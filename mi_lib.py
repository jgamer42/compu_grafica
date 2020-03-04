import pygame
NEGRO = [0,0,0]
VERDE = [0,255,0]
MATRIZ_ESCALAMIENTO = [[1,0,0],
                       [0,1,0],
                       [0,0,1]]
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

#NOTE funcion para transformar de coordenada pantalla a coordenada cartesiana
# entradas: punto a dibujar, origen del plano
# proceso: realiza la transformacion lineal del punto de pantalla a cartesiano
# salida: el punto transformado a la coordenada cartesiana
def transformada_pantalla(pos,origen):
    x = pos[0] - origen[0]
    pos[1] = pos[1] * (-1)
    y = pos[1] + origen[1]
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

#NOTE funcion para hallar la pendiente entre dos puntos
# entradas: punto inicial , punto final
# proceso: calcular la pendiente
# salida: pendiente de la recta
def pendiente(p1,p2):
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    return (m)

#NOTE funcion para hallar la constante de desplazamiento entre dos puntos
# entradas: punto inicial , punto final, pendiente
# proceso: calculo de la constante de desplazamiento
# salida: constante de desplazamiento
def desplazamiento(p1,p2,m):
    b = p2[0] + m*p1[0]
    return(b)

#NOTE funcion para aplicar la transformada de escalamiento a una lista de puntos
# entradas: lista de puntos , escala
# proceso: cacula los puntos escalados
# salida: nuevos puntos escalados
def transformada_escalamiento(puntos,escala):
    salida = []
    x = MATRIZ_ESCALAMIENTO[0][0] * escala[0]
    y = MATRIZ_ESCALAMIENTO[1][1] * escala[1]
    for p in puntos:
        a = p[0] * x
        b = p[1] * y
        aux = [int(a),int(b)]
        salida.append(aux)
    return(salida)
