import pygame, sys, time
from pygame.locals import *

# Establece pygame
pygame.init()

# Establece la ventana
ANCHOVENTANA = 800
ALTOVENTANA = 600
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0,32)
pygame.display.set_caption('Animación')

# Establece los colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

rectangulo = pygame.Rect(500, 150, 60, 60)

direccion = 'DERECHA'


# Corre el ciclo de juego
while True:
# Busca un evento
  for evento in pygame.event.get():
    if evento.type == QUIT:
      pygame.quit()
      sys.exit()

  # Dibuja el fondo negro sobre la superficie
  superficieVentana.fill(NEGRO)

  # Detectar si toco el borde! - primera colision
 # print(rectangulo.left)
  print(direccion + " " + str(rectangulo.left))

  if direccion == 'DERECHA':
    if rectangulo.left + 60 < ANCHOVENTANA:
      rectangulo.left += 2
    else:
      direccion = 'IZQUIERDA'

  if direccion == 'IZQUIERDA':
    if rectangulo.left > 0:
      rectangulo.left -= 2
    else:
      direccion = 'DERECHA'

  # rectangulo.top += 2

  # Dibuja el bloque en la superficie
  pygame.draw.rect(superficieVentana, ROJO, rectangulo)

  # Dibuja la ventana en la pantalla
  pygame.display.update()
  time.sleep(0.02)
