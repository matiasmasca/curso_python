import pygame, sys, time
from pygame.locals import *

pygame.init()

# configurar una ventana
superficieVentana = pygame.display.set_mode((800,600),0, 32)

pygame.display.set_caption('¡Hola mundo en PyGame!')

# configurar los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
GRIS = (164, 164, 164)

fuenteBasica = pygame.font.SysFont('Dyuthi', 48)
texto = fuenteBasica.render('!Hola Mundo en PyGame!', True, NEGRO, 0)

textRect = texto.get_rect()
textRect.centerx = superficieVentana.get_rect().centerx
textRect.centery = superficieVentana.get_rect().centery


# pygame.draw.polygon(superficieVentana, AZUL, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
# pygame.draw.polygon(superficieVentana, VERDE, ((246, 0), (391, 106), (336, 277), (156, 277), (100, 106)), 10)

# pygame.draw.line(superficieVentana, NEGRO,(60,60),(120,60), 4)
# pygame.draw.line(superficieVentana, ROJO, (120, 60), (60, 120))
# pygame.draw.line(superficieVentana, VERDE, (60, 120), (220, 120), 10)

# pygame.draw.circle(superficieVentana, GRIS, (60,60), 30, 0)
# pygame.draw.ellipse(superficieVentana, AZUL, (150, 190, 40, 80),5)
# pygame.draw.ellipse(superficieVentana, ROJO, (300, 190, 40, 80))

# pygame.draw.rect(superficieVentana, VERDE, (10,10, 340, 50))
# pygame.draw.rect(superficieVentana, ROJO, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
# superficieVentana.blit(texto, textRect)

superficieVentana.fill(BLANCO)

#pygame.draw.rect(superficieVentana, VERDE, (0, 0, 340, 50))
# pygame.draw.rect(superficieVentana, ROJO, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))



# dibujar la ventana sobre la pantalla
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.draw.rect(superficieVentana, ROJO, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

  superficieVentana.blit(texto, textRect)
  textRect.left += 1
  pygame.display.update()
  time.sleep(0.10)

