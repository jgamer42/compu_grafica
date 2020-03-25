import pygame
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (300,300)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
posx = 300
posy = 300
velx = 0
vely = 0
reloj = pygame.time.Clock()
if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    pelota = pygame.image.load('pelota.png')
    print(pelota.get_rect())

    while True:
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velx = 5
                    vely = 0
                if event.key == pygame.K_LEFT:
                    velx = -5
                    vely = 0
                if event.key == pygame.K_UP:
                    vely = -5
                    velx = 0
                if event.key == pygame.K_DOWN:
                    vely = 5
                    velx = 0
                if event.key == pygame.K_SPACE:
                    vely = 0
                    velx = 0
        ventana.fill([0,0,0])
        ventana.blit(pelota,[posx,posy])
        pygame.display.flip()
        if(posx > ANCHO-32):
            posx = 0
        if(posx < 0):
            posx = ANCHO-32
        if(posy < 0):
            posy = ALTO-32
        if(posy > ALTO-32):
            posy = 0
        posx += velx
        posy += vely
        reloj.tick(90)
