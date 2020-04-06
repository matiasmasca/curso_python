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

# dibujar un polígono verde sobre la superficie
pygame.draw.polygon(superficieVentana, ROJO, ((146, 0), (291, 106), (236,
277), (56, 277), (0, 106)), 0)

pygame.draw.polygon(superficieVentana, VERDE, ((246, 0), (391, 106), (336, 277), (156, 277), (100, 106)), 10)

"""
Un polígono es una forma cuyos múltiples lados son líneas rectas.

La función pygame.draw.polygon() puede dibujar cualquier forma de polígono que le pases.
Los parámetros, en orden, son:
- El objeto Surface sobre el que se dibujará el polígono.
- El color del polígono.
- Una tupla de tuplas que representa las coordenadas XY de los puntos a dibujar en orden.
La última tupla se conectará automáticamente con la primera para cerrar la forma.
- Opcionalmente, un entero para el ancho de las líneas del polígono. Sin esto, el polígono
será rellenado del color de la línea.
"""


# dibujar la ventana sobre la pantalla
pygame.display.update()

# ejecutar el bucle del juego
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
