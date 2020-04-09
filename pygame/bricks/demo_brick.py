#!/usr/bin/python
import pygame, os, sys
from pygame.locals import *

# Pegandole a la pelota con la paleta
pygame.init()

def ladrillo():
  ladrillo = pygame.image.load('brick.png')
  return ladrillo

def crear_ladrillos(filas = 5, columnas = 5):
  ancho = ladrillo.get_width() # ancho
  alto = ladrillo.get_height()  # alto
  for fila in range(filas): # [0-4]
    ladrilloY = ( fila * 24 ) + 100
    for columna in range(columnas):
      ladrilloX = (columna * 31 ) + 245
      rectangulo_ladrillo = { 1: { "vida": 5 , "rectangulo": Rect(ladrilloX, ladrilloY, ancho, alto), "tipo": "metal"}  }
      ladrillos.append(rectangulo_ladrillo)
  return ladrillos



def borrar_ladrillo(ladrillos_list, indice):
  rebote = ''
  if indice >= 0:
      ladrilloTocado = ladrillos_list[indice]
      medio_ladrillo_x = pelota_x + 4
      medio_ladrillo_y = pelota_y + 4
      if medio_ladrillo_x > ladrilloTocado.x + ladrilloTocado.width or medio_ladrillo_x < ladrilloTocado.x:
        # velocidad_x *= -1
        rebote = 'rebote_x'
      else:
        #velocidad_y *= -1
        rebote = 'rebote_y'
      del (ladrillos_list[indice])
  return rebote

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
pelota = pygame.image.load('ball.png')
pelotaRect = pelota.get_rect()
pelotaEmpiezaEnY = 200
pelotaVelocidad = 5
pelotaEnMovimiento = False
pelota_x, pelota_y = (24, pelotaEmpiezaEnY)
velocidad_x, velocidad_y = (pelotaVelocidad, pelotaVelocidad)
pelotaRect.topleft = (pelota_x, pelota_y)

# Crear ladrillo
ladrillo = ladrillo()
ladrillos = []
ladrillos = crear_ladrillos(10, 15)


while True:
    # pintamos todo de negro
    superficieVentana.fill(black)

    # dibujar ladrillo
    # dibujar paleta y pelota
    superficieVentana.blit(paleta, paletaRect) # paleta
    superficieVentana.blit(pelota, pelotaRect) # pelota

    for item_ladrillo_rect in ladrillos:
      superficieVentana.blit(ladrillo, item_ladrillo_rect)

    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            print(event.pos)
            if (mousex < 800 - 55):
                paletaRect.topleft = (mousex, jugadorY)
            else:
                paletaRect.topleft = (800 - 55, jugadorY)
        elif event.type == MOUSEBUTTONUP and not pelotaEnMovimiento:
          pelotaEnMovimiento = True


    indiceLadrilloTocado = pelotaRect.collidelist(ladrillos) # devuelve un indice
    rebote = borrar_ladrillo(ladrillos, indiceLadrilloTocado)
    if rebote == 'rebote_x':
      velocidad_x *= -1
    elif rebote == 'rebote_y':
      velocidad_y *= -1


    # Logica principal del juego
    # Mover la pelota.
    # usamos la formula Distancia = Velocidad x Tiempo
    if pelotaEnMovimiento:
      pelota_x += velocidad_x
      pelota_y += velocidad_y
      pelotaRect.topleft = (pelota_x, pelota_y)

    # Deteccion de coliciones

    # La pelota toca un borde de la pantalla
    # La pelota se sale de la pantalla
    # print(pelota_y)

    # hace rebotar cuando toca el fondo
    if (pelota_y >= 600 - 8):
      pelotaEnMovimiento = False
      pelota_x, pelota_y = (24, pelotaEmpiezaEnY)
      pelotaVelocidad = 8
      velocidad_x, velocidad_y = (pelotaVelocidad, pelotaVelocidad)
      pelotaRect.topleft = (pelota_x, pelota_y)
      ladrillos = crear_ladrillos(pelotaVelocidad + 5, 15)


    # hacer rebotar al tocar la derecha de la pantalla
    if (pelota_x >=800 - 8):
      pelota_x = 800 - 8
      velocidad_x *= -1

    # hacer rebotar al tocar el techo
    if (pelota_y <= 0):
        pelota_y = 0
        velocidad_y *= -1

    # hacer rebotar al toar la izquierda de la pantalla
    if (pelota_x <= 0):
        pelota_x = 0
        velocidad_x *= -1

    # PEGARLE CON LA PALETA
    """
    The colliderect takes a single parameter that represents the rectangle
we want to the check collision against. The colliderect method returns a
Boolean ‘True’ or ‘False’ depending on whether the rectangles intersect
each other.
    """
    if pelotaRect.colliderect(paletaRect):
        pelota_y = jugadorY - 8
        velocidad_y *= -1

    pygame.display.update()
    cuadros_por_segundo.tick(30)


# Basado en los ejemplos de Sloan Kelly