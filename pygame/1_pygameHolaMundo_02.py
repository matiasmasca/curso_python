import pygame, sys
from pygame.locals import *

# configurar pygame
pygame.init()

# configurar la ventana
superficieVentana = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('¡Hola mundo!')

# configurar los colores. RGB.
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


# pintar un fondo blanco sobre la ventana
 superficieVentana.fill((255, 255, 255))
# superficieVentana.fill((220, 107, 34))

"""
Queremos llenar toda la superficie almacenada en superficieVentana con el color blanco. La función fill() cubrirá completamente la superficie
con el color que le pases como parámetro.
"""

"""
Hay tres colores primarios de luz: Rojo, Verde y Azul. Combinando diferentes cantidades de estos tres colores
(que es lo que hace tu pantalla hace) puedes formar cualquier otro color. En Pygame, las estructuras de datos que representan
un color son tuplas de tres enteros. Se las llama valores de Color RVA (en inglés, RGB por red, green, blue).
Mira algunos colores que podes formar en https://htmlcolorcodes.com/
"""

"""
Algo importante a saber acerca de Pygame es que la ventana en la pantalla no cambiará cuando llames a un método o a cualquiera de las otras
funciones de dibujo. Éstas cambiarán al objeto Surface, pero el objeto Surface no será dibujado en la pantalla hasta que se llame a la función
pygame.display.update() .
Por una cuestion de eficiencia, más rápido cambiar en memoria que en pantalla.
"""


# dibujar la ventana sobre la pantalla
pygame.display.update()

# ejecutar el bucle del juego
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
