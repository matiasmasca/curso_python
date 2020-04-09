#!/usr/bin/python
import pygame, os, sys
from pygame.locals import *

# Moviendo la paleta

pygame.init()
cuadros_por_segundo = pygame.time.Clock()
superficieVentana = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bricks')

black = pygame.Color(0, 0, 0)

# Crear paleta jugador
paleta = pygame.image.load('bat.png') # tiene 55 pixeles de ancho
paletaRect = paleta.get_rect() # define un rectangulo que sirve para los calculos.
jugadorY = 540 # como el jugador solo se mueve de izquierda a derecha, fijamos su posición en la Y (altura)
mousex, mousey = (0, jugadorY)
paletaRect.topleft = (355, jugadorY) # hubico la paleta

# Crear pelota
# Crear ladrillo

while True:
    # pintamos todo de negro
    superficieVentana.fill(black)

    # dibujar ladrillo
    # dibujar paleta y pelota
    superficieVentana.blit(paleta, paletaRect)

    # Eventos
    """
    DETECTAR EL MOVIMIENTO DEL MOUSE.
    El sistema operativo informa al programa donde se encuentra el mouse.
    Desde Pygame usamos el evento "MOUSEMOTION", este tiene un parametro llamado 'pos' que tiene una tupla con las coordenadas X e Y de la posición del mouse.
    """
    for event in pygame.event.get():
        # imprime en la consola el evento
        # print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            print(event.pos) # veamos donde esta el mouse
            """
            # Movamos la paleta usando las coordenadas del mouse
            mousex, mousey = event.pos #asignación multiple, se guarda en mousex lo que este en la x de pos (x, y) y en mousey lo que este en la y.
            if (mousex < 800 - 55): # siempre que el mouse este dentro del ancho de la pantalla restando el tamaño de la paleta
                paletaRect.topleft = (mousex, jugadorY)
            else:
                paletaRect.topleft = (800 - 55, jugadorY)
            """
    # Logiga principal del juego
    # Deteccion de coliciones

    pygame.display.update()
    cuadros_por_segundo.tick(30)


# Basado en los ejemplos de Sloan Kelly
