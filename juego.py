import pygame
import const
from jugador import Jugador
if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode([const.ANCHO,const.ALTO])
    animal = pygame.image.load('sprites.png')
    clock = pygame.time.Clock()
    matriz = []
    cont=0
    for x in range(8):
        row = []
        for c in range(12):
            square = animal.subsurface(32*c,32*x,32,32)
            row.append(square)
        matriz.append(row)

    game = False

    player = Jugador([0,0],matriz)
    players = pygame.sprite.Group()
    players.add(player)

    while(not game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player.acelerar(0,5,0)
                if event.key == pygame.K_UP:
                    player.acelerar(0,-5,3)
                if event.key == pygame.K_RIGHT:
                    player.acelerar(5,0,2)
                if event.key == pygame.K_LEFT:
                    player.acelerar(-5,0,1)
            if event.type == pygame.KEYUP:
                player.frenar()
        players.update()
        window.fill(const.NEGRO)
        players.draw(window)
        pygame.display.flip()
        clock.tick(10)
