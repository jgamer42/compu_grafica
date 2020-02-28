import pygame

pygame.init()
ventana = pygame.display.set_mode([600,450])
#loop principal
fin = True
y = 0
while fin:
	for event in pygame.event.get():
		#loop de fin
		if event.type == pygame.QUIT:
			fin = False
		#teclas
		if event.type == pygame.KEYDOWN:
		 	if event.key == pygame.K_DOWN:
		 		y += 10
		 	if event.key == pygame.K_UP:
		 		y -= 10
	ventana.fill([0,0,0])
	pygame.draw.line(ventana, [255,255,255],[50,y],[100,y],5)
	pygame.display.flip() 