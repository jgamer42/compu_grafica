import pygame
import random
from models import Const
from models.jugador import Jugador
from models.bala import Bala
from models.enemigo import Rival

if __name__ == '__main__':
    pygame.init()
    #NOTE Definicion de variables
    ventana=pygame.display.set_mode([Const.ANCHO,Const.ALTO])
    #NOTE previo
    fuente_previa = pygame.font.Font(None,46)
    fin=False
    fin_previo =False
    musica = pygame.mixer.Sound('musica1.ogg')
    musica.play(3,500)
    while (not fin) and (not fin_previo):
        #NOTE Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                fin_previo=True
        titulo = fuente_previa.render("juego de prueba",True,Const.BLANCO)
        ventana.blit(titulo,[350,350])
        pygame.display.flip()
    musica.stop()
    #NOTE seccion de juego
    jugadores=pygame.sprite.Group()
    j=Jugador([300,200])
    jugadores.add(j)
    rivales=pygame.sprite.Group()
    balas_jugador=pygame.sprite.Group()
    balas_rival=pygame.sprite.Group()
    n=10
    puntos=0
    letras_gui = pygame.font.Font(None,32)
    sonido_disp = pygame.mixer.Sound('efecto_balas.wav')
    for i in range(n):
        x=random.randrange((Const.ANCHO-50))
        y=random.randrange((Const.ALTO-150))
        velx=5
        temp=random.randrange(40,100)
        r=Rival([x,y],temp,velx,0)
        rivales.add(r)
    reloj=pygame.time.Clock()
    fin_juego =False
    #NOTE Ciclo principal del juego
    while (not fin) and (not fin_juego):
        #NOTE Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.acelerar(5,0)
                if event.key == pygame.K_LEFT:
                    j.acelerar(-5,0)
                if event.key == pygame.K_UP:
                    j.acelerar(0,-5)
                if event.key == pygame.K_DOWN:
                    j.acelerar(0,5)
                if event.key == pygame.K_z:
                    sonido_disp.play(0,500)
                    p=j.RetPos()
                    b=Bala(p,-10,0)
                    balas_jugador.add(b)
                if event.key == pygame.K_SPACE:
                    j.frenar()
        #Control

        #NOTE Colision
        ls_col=pygame.sprite.spritecollide(j,rivales,False)
        for r in ls_col:
            puntos -= 10
            print(puntos)

        #NOTE Limpieza de memoria
        #gestion balas jugador
        for b in balas_jugador:
            #colision proyectil
            ls_r = pygame.sprite.spritecollide(b,rivales,True)
            if b.rect.y < -50:
                balas_jugador.remove(b)
            #limpia las valas
            for r in ls_r:
                balas_jugador.remove(b)
        #gestion balas rival
        for b in balas_rival:
            ls_r = pygame.sprite.spritecollide(b,jugadores,False)
            if (b.rect.y > Const.ALTO):
                balas_rival.remove(b)
            contacto=True
            for j in ls_r:
                if contacto:
                    balas_rival.remove(b)
                    j.vida -= 1
                    contacto=False
        for j in jugadores:
            if j.vida<0:
                fin_juego = True

        #NOTE control rivales
        for r in rivales:
            if(r.temp<0):
                pos=r.get_pos()
                b = Bala(pos,10,0,Const.AMARILLO)
                r.temp = random.randrange(40,100)
                balas_rival.add(b)

        #NOTE Refresco
        #curso normal del juego
        gui_puntos=letras_gui.render('vidas: %d'%(j.vida),True,Const.BLANCO)
        jugadores.update()
        rivales.update()
        balas_jugador.update()
        balas_rival.update()
        ventana.fill(Const.NEGRO)
        ventana.blit(gui_puntos,[20,20])
        jugadores.draw(ventana)
        rivales.draw(ventana)
        balas_jugador.draw(ventana)
        balas_rival.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)


    #NOTE seccion pos juego
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        ventana.fill(Const.NEGRO)
        fuente=pygame.font.Font(None,36)
        mensaje=fuente.render("fin de juego :c",True,Const.BLANCO)
        ventana.blit(mensaje,[300,300])
        pygame.display.flip()