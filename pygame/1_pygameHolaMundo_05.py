import pygame, sys
from pygame.locals import *

# configurar pygame
pygame.init()

# configurar la ventana
superficieVentana = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('¡Hola mundo!')

# configurar los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# pintar un fondo blanco sobre la ventana
superficieVentana.fill(BLANCO)

# dibujar algunas líneas azules sobre la superficie
pygame.draw.line(superficieVentana, NEGRO, (60, 60), (120, 60), 4)
pygame.draw.line(superficieVentana, ROJO, (120, 60), (60, 120))
pygame.draw.line(superficieVentana, VERDE, (60, 120), (220, 120), 10)

"""
Los parámetros, en orden, son:
- El objeto Surface sobre el que se dibujará la línea.
- El color de la línea.
- Una tupla de dos enteros para las coordenadas XY de un extremo de la línea.
- Una tupla de dos enteros para las coordenadas XY del otro extremo de la línea.
- Opcionalmente, un entero para el ancho de la línea. Por defecto 1.

"""



# dibujar la ventana sobre la pantalla
pygame.display.update()

# ejecutar el bucle del juego
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
