import pygame, sys, time
from pygame.locals import *

def colision_rectangulo(objeto_1, objeto_2):
   # print(objeto_2.right)
   if ( objeto_1.left == objeto_2.right ):
          print("hay colision")
          return True
   else:
      return False



# Establece pygame
pygame.init()

# Setup juego
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
BLANCO = (255, 255, 255)

rectangulo = pygame.Rect(500, 150, 60, 60)

rectangulo_2 = pygame.Rect(300, 150, 60, 60)

direccion = 'DERECHA'


# Crear paleta jugador
# jugador_img = pygame.image.load('enemy.png') # tiene 55 pixeles de ancho
# jugadorRect = jugador_img.get_rect() # define un rectangulo que sirve para los calculos.
# jugadorRect.topleft = (155, 150) # hubico la jugador



# Corre el ciclo de juego
while True:
# Busca un evento
  for evento in pygame.event.get():
    if evento.type == QUIT:
      pygame.quit()
      sys.exit()

  # Dibuja el fondo negro sobre la superficie
  superficieVentana.fill(NEGRO)

  # superficieVentana.blit(jugador_img, jugadorRect) # jugador
  # Detectar si toco el borde! - primera colision
 # print(rectangulo.left)
  # print(direccion + " " + str(rectangulo.left))
  if direccion == 'DERECHA':
    if rectangulo.left < ANCHOVENTANA - 60:
      rectangulo.left += 1
    else:
      direccion = 'IZQUIERDA'

  if direccion == 'IZQUIERDA':
    if rectangulo.left > 0:
      rectangulo.left -= 1
    else:
      direccion = 'DERECHA'

  if colision_rectangulo(rectangulo, rectangulo_2):
    direccion = "ARRIBA"

  # Dibuja el bloque en la superficie
  pygame.draw.rect(superficieVentana, AZUL, rectangulo)

  pygame.draw.rect(superficieVentana, VERDE, rectangulo_2)
  # Dibuja la ventana en la pantalla
  pygame.display.update()
  # time.sleep(0.02)



