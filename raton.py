import pygame 
ANCHO = 600
ALTO = 800
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
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

class Generador (pygame.sprite.Sprite):
    def __init__(self,pos,color = ROJO):
        super().__init__()
        self.image = pygame.Surface([100,100])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.click = False
        self.tipo = 0

    def update(self):
        if(self.click):
            self.rect.center = pygame.mouse.get_pos()

class Cuadro2 (pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.click = False
        self.velx = 5
    def update(self):
        if(self.click):
            self.rect.center = pygame.mouse.get_pos()
        else:
            self.rect.x += self.velx



if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    reloj = pygame.time.Clock()
    fin = False
    cuadros = pygame.sprite.Group()
    generadores = pygame.sprite.Group()
    generador = Generador([100,100])
    generador2 = Generador([210,100],AZUL)
    generador2.tipo = 1
    generadores.add(generador)
    generadores.add(generador2)
    while(not fin):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for generador in generadores:
                    if(generador.rect.collidepoint(event.pos)):
                        if(generador.tipo == 0):
                            cuadro = Cuadro(event.pos)
                            cuadros.add(cuadro)
                        elif(generador.tipo == 1):
                            cuadro = Cuadro2(event.pos)
                            cuadros.add(cuadro)
                for cuadro in cuadros:
                    if(cuadro.rect.collidepoint(event.pos)):
                        cuadro.click = True
            if event.type == pygame.MOUSEBUTTONUP:
                for cuadro in cuadros:
                    cuadro.click = False
        
        cuadros.update()
        generadores.update()
        ventana.fill(NEGRO)
        generadores.draw(ventana)
        cuadros.draw(ventana)
        pygame.display.flip()
        reloj.tick(30)