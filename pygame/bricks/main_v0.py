#!/usr/bin/python
import pygame, os, sys
from pygame.locals import *

pygame.init()
cuadros_por_segundo = pygame.time.Clock()

# Un objeto pygame.time.Clock puede generar una pausa que sea adecuada para cualquier computadora.
# La línea que llama a cuadros_por_segundo.tick(30) dentro del bucle del juego. Esta llamada al método tick() del objeto Clock calcula la pausa adecuada para que el bucle ejecute unas 30 iteraciones por segundo, sin importar cuál sea la velocidad de la computadora.

mainSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bricks')

NEGRO = pygame.Color(0, 0, 0)

# Crear paleta jugador
# Crear pelota
# Crear ladrillo

while True:
    mainSurface.fill(NEGRO)
    # dibujar ladrillo
    # dibujar paleta y pelota
    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Logiga principal del juego
    # Deteccion de coliciones

    pygame.display.update()
    cuadros_por_segundo.tick(30)


# Basado en los ejemplos de Sloan Kelly
