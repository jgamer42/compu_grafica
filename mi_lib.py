import pygame
import math
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
    aux = pos[1] * (-1)
    y = origen[1] + aux
    punto = [x,y]
    return punto

#NOTE funcion para transformar de coordenada pantalla a coordenada cartesiana
# entradas: punto a dibujar, origen del plano
# proceso: realiza la transformacion lineal del punto de pantalla a cartesiano
# salida: el punto transformado a la coordenada cartesiana
def transformada_pantalla(pos,origen):
    x = pos[0] - origen[0]
    aux = pos[1] * (-1)
    y = aux + origen[1]
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

#NOTE funcion para rotar una figura en sentido horario
# entradas: lista de puntos , angulo
# proceso: cacula la los puntos con la rotacion
# salida: nuevos puntos rotados
def rotacion_anti_horaria(puntos,angulo):
    radianes = math.radians(angulo)
    salida = []
    for i in puntos:
        x_rotada = (i[0]*(math.cos(radianes))) + (i[1]*(math.sin(radianes)))
        y_rotada = (-i[0]*(math.sin(radianes))) + (i[1]*(math.cos(radianes)))
        punto_rotado=[int(x_rotada),int(y_rotada)]
        salida.append(punto_rotado)
    return (salida)

#NOTE funcion para desplazar puntos
# entradas: punto, desplazamiento x, desplazamiento y
# proceso: cacula la los puntos con el desplazamiento
# salida: nuevos puntos desplazado
def transformada_desplazamiento(punto,tx,ty):
    x_d = punto[0] + tx
    y_d = punto[1] + ty
    return ([x_d,y_d])

#NOTE funcion para escalar respecto a un punto fijo
# entradas: figura, escalamiento
# proceso: desplazar al orgien, escalar, desplazar al punto inicial
# salida: nuevos puntos escalados
def escalamiento_punto_fijo(puntos,escalamiento,punto_fijo=None):
    if(punto_fijo==None):
        punto_fijo=puntos[0]
    salida = []
    Traslacion = [-punto_fijo[0],-punto_fijo[1]]
    for i in puntos:
        pt = transformada_desplazamiento(i,Traslacion[0],Traslacion[1])
        pe = transformada_escalamiento([pt],[escalamiento,escalamiento])
        po = transformada_desplazamiento(pe[0],punto_fijo[0],punto_fijo[1])
        salida.append(po)
    return(salida)


#NOTE funcion para transformar un punto de coordenadas polares a cartesianas
#entradas: punto a transformar
#proceso: aplica la transformacio normal(ver formula)
#salida: punto transformado
def transformada_polar_cartesiana(punto):
    angulo = math.radians(punto[1])
    x = int(punto[0] * math.cos(angulo))
    y = int(punto[0] * math.sin(angulo))
    salida = [x,y]
    return (salida)

#NOTE funcion para dibujar un cardiode
#entradas: a,b constantes de la ecuacion (ver mate 2)
#proceso: recorre con todos los angulos de 0 a 360, calcula r
#           respecto a la formula, convierte a cartesiano y lo agrega
#           a los puntos de la figura
#salidas: puntos de la figura en cartesiano
def cardiode(a,b):
    angulo = 0
    figura = []
    while angulo <= 360:
        angulo_rad = math.radians(angulo)
        r = a + b*math.cos(angulo_rad)
        punto = [r,angulo]
        cartesiano = transformada_polar_cartesiana(punto)
        figura.append(cartesiano)
        angulo += 1
    return (figura)

def figura_pitagorica(radio,lados):
    mod_angulo = 360/lados
    angulo = 0
    figura = []
    while angulo <= (360-mod_angulo):
        punto = transformada_polar_cartesiana([radio,angulo])
        figura.append(punto)
        angulo = angulo + mod_angulo
    return(figura)

#TODO rotacion punto fijo , rotacion rotacion anti horaria
