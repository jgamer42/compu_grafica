import pygame
def circulo (pos,v,color):
	pygame.draw.circle(v,color,pos,2)
alto = 450
ancho = 600
pygame.init()
ventana = pygame.display.set_mode([ancho,alto])
ac=[0,0,255]
bc=[255,255,255]
blanco=[]
azul=[]
#loop principal
fin = True
while fin:
	for event in pygame.event.get():
		#loop de fin
		if event.type == pygame.QUIT:
			fin = False 
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				circulo(list(event.pos),ventana,bc)
				blanco.append(list(event.pos))
				for i in blanco:
					if i[0]>0:
						while i[0] > 0:
							i[0] -= 10
							circulo(i,ventana,bc)
					else:
						circulo(i,ventana,bc)
			if event.button == 3:
				circulo(list(event.pos),ventana,ac)
				azul.append(list(event.pos))
				for i in azul:
					if i[0]<ancho:
						while i[0] < ancho:
							i[0] += 10
							circulo(i,ventana,ac)
					else:
						circulo(i,ventana,ac)

	pygame.display.flip()