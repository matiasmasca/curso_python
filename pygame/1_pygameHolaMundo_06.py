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

# dibujar un círculo azul sobre la superficie
pygame.draw.circle(superficieVentana, NEGRO, (30, 30), 30, 0)

"""
Para dibujar un Circulo, los parámetros son:
- El objeto Surface sobre el que se dibujará el círculo.
- El color del círculo.
- Una tupla de dos enteros para las coordenadas XY del centro del círculo.
- Un entero para el radio (es decir, el tamaño) del círculo.
- Opcionalmente, un entero para el ancho. Un ancho de 0 significa que el círculo será
rellenado.
"""

# dibujar una elipse roja sobre la superficie
pygame.draw.ellipse(superficieVentana, (255, 10, 10), (300, 250, 40, 80), 5)

pygame.draw.ellipse(superficieVentana, AZUL, (150, 190, 40, 80), 0)

"""
Para dibujar un elipse, los parámetros son:
- El objeto Surface sobre el que se dibujará la elipse.
- El color de la elipse.
- Una tupla de cuatro enteros para los bordes izquierdo y superior, ancho y altura de la elipse.
- Opcionalmente, un entero para el ancho. Un ancho de 0 significa que la elipse será rellenada.

"""


# dibujar la ventana sobre la pantalla
pygame.display.update()

# ejecutar el bucle del juego
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
