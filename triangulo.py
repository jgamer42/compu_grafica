import pygame
import sys
ANCHO = 500
ALTO = 500
def dibujar_triangulo(p1,v,f):
    pygame.draw.line(v,[255,255,255],p1,(p1[0],p1[1]+50),2)
    pygame.draw.line(v,[255,255,255],(p1[0],p1[1]+50),(p1[0]+25,p1[1]+25),2)
    pygame.draw.line(v,[255,255,255],p1,(p1[0]+25,p1[1]+25),2)
    t = (p1,(p1[0],p1[1]+50),(p1[0]+25,p1[1]+25))
    f.append(t)

def integrador(v,f1,f2):
    pygame.draw.line(v,[255,255,255],f1[0],f2[0])
    pygame.draw.line(v,[255,255,255],f1[1],f2[1])
    pygame.draw.line(v,[255,255,255],f1[2],f2[2])
if __name__ == '__main__':
    figuras = []
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                dibujar_triangulo(event.pos,ventana,figuras)
                if len(figuras) >= 2:
                    figura1 = figuras[len(figuras)-2]
                    figura2 = figuras[len(figuras)-1]
                    integrador(ventana,figura1,figura2)
        pygame.display.flip()
