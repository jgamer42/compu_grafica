import pygame
import sys
ANCHO = 1000
ALTO = 1000
def dibujar_patron(v,punto):
    #cudrado externo
    pygame.draw.line(v,[255,255,255],punto,(punto[0]+15,punto[1]),2)
    pygame.draw.line(v,[255,255,255],(punto[0]+15,punto[1]),(punto[0]+15,punto[1]+15),2)
    pygame.draw.line(v,[255,255,255],(punto[0]+15,punto[1]+15),(punto[0],punto[1]+15),2)
    #cuadrado interno
    pygame.draw.line(v,[255,255,255],(punto[0],punto[1]+15),(punto[0],punto[1]+5),2)
    pygame.draw.line(v,[255,255,255],(punto[0],punto[1]+5),(punto[0]+10,punto[1]+5),2)
    pygame.draw.line(v,[255,255,255],(punto[0]+10,punto[1]+5),(punto[0]+10,punto[1]+10),2)
    pygame.draw.line(v,[255,255,255],(punto[0]+10,punto[1]+10),(punto[0]+5,punto[1]+10),2)

def borde(v):
    i = 0
    while i < ANCHO-15:
        dibujar_patron(v,(i,ALTO-20))
        dibujar_patron(v,(i,0))
        dibujar_patron(v,(0,i))
        dibujar_patron(v,(ANCHO-20,i))
        i += 20
if __name__ == '__main__':
    figuras = []
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        borde(ventana)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
