import pygame 
ANCHO = 600
ALTO = 800
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDER = [0,255,0]
AZUL = [0,0,255]
BLANCO = [255,255,255]

class Cuadro (pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.click = False
    def update(self):
        if(self.click):
            self.rect.center = pygame.mouse.get_pos()

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    reloj = pygame.time.Clock()
    fin = False
    cuadros = pygame.sprite.Group()
    cuadro = Cuadro([50,50])
    cuadros.add(cuadro)
    while(not fin):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(cuadro.rect.collidepoint(event.pos)):
                    cuadro.click = True
            if event.type == pygame.MOUSEBUTTONUP:
                cuadro.click = False
        cuadros.update()
        ventana.fill(NEGRO)
        cuadros.draw(ventana)
        pygame.display.flip()
        reloj.tick(30)