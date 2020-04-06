
import pygame, sys # incorporamos pygame (ya que no viene con python) y librerias del sistema
from pygame.locals import * # Este módulo contiene muchas variables constantes que usarás con Pygame, tales como QUIT

# configurar pygame
pygame.init() # Esto realiza los pasos necesarios para la inicialización de Pygame.
# crea una pantalla oculta. Pero debemos definir algunas cosas de esa pantalla antes de mostrarla

# configurar la ventana
superficieVentana = pygame.display.set_mode((500, 400), 0, 32)
# pygame.display.set_mode (resolución = (0,0), indicadores = 0, profundidad = 0)
# Resolución: Para crear una ventana de 500 píxeles de ancho por 400 píxeles de alto, se usa la tupla (500, 400). Un pixel es un punto en la pantalla que se puede prender o apagar.
# indicadores: opciones adicionales que cambian el tipo de ventana. flags = pygame.FULLSCREEN | pygame.OPENGL
# Profundidad: cantidad de bits utilizados para el color
# Pygame actualmente solo puede manejar una única ventana a la vez.

# La función set_mode() devuelve un objeto pygame.Surface //surfis//, que representa la ventana

pygame.display.set_caption('¡Hola mundo en PyGame!')


# ejecutar el "bucle del juego"
# En este programa, todas las líneas de código en el bucle de juego se ejecutan alrededor de cien veces por segundo.
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

# QUIT viene del modulo importado pygame.locals
# Si el evento QUIT se ha generado, el programa debe llamar a ambas funciones pygame.quit() y sys.exit() .



"""
Si se cuelga en Linux
$ ps -ef | grep python
$ kill -9 2430


o
pkill -9 -f script.py

"""
