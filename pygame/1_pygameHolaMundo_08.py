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

# obtener un arreglo de píxeles de la superficie
arregloDePíxeles = pygame.PixelArray(superficieVentana)
arregloDePíxeles[480][380] = ROJO
arregloDePíxeles[479][380] = ROJO
arregloDePíxeles[478][380] = ROJO
arregloDePíxeles[477][380] = ROJO
del arregloDePíxeles

"""
crea un objeto pygame.PixelArray (llamado objeto PixelArray por brevedad). El
objeto PixelArray es una lista de listas de tuplas de colores que representa el objeto Surface que le
pasas.

La línea 19 pasa superficieVentana a pygame.PixelArray(), de modo que asignar ROJO a
arregloDePíxeles[480][380] en la línea 20 cambiará el color del píxel en las coordenadas
(480, 380) a rojo. Pygame modificará automáticamente el objeto superficieVentana con
este cambio.
El primer índice en el objeto PixelArray es para la coordenada X. El segundo índice es para la
coordenada Y. Los objetos PixelArray facilitan cambiar el color de píxeles individuales a un
color específico.

Crear un objeto PixelArray a partir de un objeto Surface bloquea al objeto Surface. Esto significa
que no puede llamarse a la función blit() sobre ese objeto Surface.
Para desbloquear el objeto Surface, debes borrar el objeto PixelArray con el operador del.
"""



# dibujar la ventana sobre la pantalla
pygame.display.update()

# ejecutar el bucle del juego
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
