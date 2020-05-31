import pygame
import const
from jugador import Jugador
from bloque import Bloque
if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode([const.ANCHO,const.ALTO])
    ken = pygame.image.load('ken.png')
    clock = pygame.time.Clock()
    matriz = []
    cont=0
    combo = ""
    for x in range(10):
        row = []
        for c in range(7):
            square = ken.subsurface(70*c,80*x,70,80)
            row.append(square)
        matriz.append(row)

    game = False
    block = Bloque([50,400],[40,60])
    blocks = pygame.sprite.Group()
    blocks.add(block)

    player = Jugador([0,500],matriz)
    players = pygame.sprite.Group()
    players.add(player)
    while(not game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player.acelerar(0,5)
                    player.swap_animation(1)
                if event.key == pygame.K_UP:
                    player.acelerar(0,-5)
                    player.swap_animation(1)
                if event.key == pygame.K_RIGHT:
                    player.acelerar(5,0)
                    player.swap_animation(1)
                if event.key == pygame.K_LEFT:
                    player.acelerar(-5,0)
                    player.swap_animation(1)
                if event.key == pygame.K_c:
                    player.swap_animation(2)
                    combo=combo + 'c'
            if event.type == pygame.KEYUP:
                player.frenar()

        ls_colision = pygame.sprite.spritecollide(player,blocks,False)
        for col in ls_colision:
            if (player.action == 2) and ( col.hit_radio_bot < player.rect.bottom < col.hit_radio_top):
                col.velx = 5
        for b in blocks:
            if (b.velx > 0):
                b.velx = b.velx -1


        player.review_combo(combo) 
        players.update()
        blocks.update()
        window.fill(const.NEGRO)
        pygame.draw.line(window,const.BLANCO,[0,const.LIMY],[const.ANCHO,const.LIMY])
        players.draw(window)
        blocks.draw(window)
        pygame.display.flip()
        clock.tick(10)
