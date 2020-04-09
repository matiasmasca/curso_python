#!/usr/bin/python
import pygame, os, sys
from pygame.locals import *

# Codigo Spagetti!
# a ver si lo podemos reducir con funciones...
def ladrillo():
    ladrillo = pygame.image.load('brick.png')
    return ladrillo

def crear_ladrillos(filas = 7, columnas = 10):
    # Devuelva una lista de rectangulos de ladrillos, con su hubicación.
    ladrillo = pygame.image.load('brick.png')
    ladrillos = []

    for y in range(filas):
        ladrilloY = (y * 24) + 100
        for x in range(columnas):
            ladrilloX = (x * 31) + 245
            ancho = ladrillo.get_width()
            alto = ladrillo.get_height()
            rectangulo_ladrillo = Rect(ladrilloX, ladrilloY, ancho, alto)
            ladrillos.append(rectangulo_ladrillo)
    return ladrillos

def borrar_ladrillo(ladrillos_list, indice):
    rebote = ''
    if indice >= 0:
        ladrilloTocado = ladrillos_list[indice]
        medio_ladrillo_x = pelota_x + 4 # sumamos el tamaño del ladrillo
        medio_ladrillo_y = pelota_y + 4
        if medio_ladrillo_x > ladrilloTocado.x + ladrilloTocado.width or medio_ladrillo_x < ladrilloTocado.x:
            # velocidad_x *= -1
            rebote = 'rebote_x'
        else:
            # velocidad_y *= -1
            rebote = 'rebote_y'
        del (ladrillos_list[indice]) # borramos el ladrillo tocado de la lista
    return rebote



pygame.init()
cuadros_por_segundo = pygame.time.Clock()
superficieVentana = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Ladrilleros')

NEGRO = pygame.Color(0, 0, 0)

# Crear paleta jugador
paleta = pygame.image.load('bat.png') # tiene 55 pixeles de ancho
paletaRect = paleta.get_rect() # define un rectangulo que sirve para los calculos.
jugadorY = 540 # como el jugador solo se mueve de izquierda a derecha, fijamos su posición en la Y (altura)
mousex, mousey = (0, jugadorY)
paletaRect.topleft = (355, jugadorY) # hubico la paleta



# Crear pelota
pelota = pygame.image.load('ball.png')
pelotaRect = pelota.get_rect()
pelotaEmpiezaEnY = 5
pelotaVelocidad = 5
pelotaEnMovimiento = False
pelota_x, pelota_y = (0, pelotaEmpiezaEnY)
velocidad_x, velocidad_y = (pelotaVelocidad, pelotaVelocidad)
pelotaRect.topleft = (pelota_x, pelota_y)


# Crear ladrillos
# Tarea: Recorrer la lista de ladrillos y cambiar para que salga 1 verde, 1 rojo y uno de madera.
ladrillos = crear_ladrillos(13)


while True:
    # pintamos todo de negro
    superficieVentana.fill(NEGRO)

    # dibujar ladrillos
    for item in ladrillos:
        superficieVentana.blit(ladrillo(), item)

    # dibujar ladrillo
    # dibujar paleta y pelota
    superficieVentana.blit(paleta, paletaRect) # paleta
    superficieVentana.blit(pelota, pelotaRect) # pelota
    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            #print(event.pos)
            if (mousex < 800 - 55):
                paletaRect.topleft = (mousex, jugadorY)
            else:
                paletaRect.topleft = (800 - 55, jugadorY)
        elif event.type == MOUSEBUTTONUP and not pelotaEnMovimiento:
            # agregamos este evento para saber que toco y solto el botón del mouse
            print(event)
            pelotaEnMovimiento = True

    # Logica principal del juego

    # Mover la pelota.
    # agregamos esta decisión
    if pelotaEnMovimiento:
        pelota_x += velocidad_x
        pelota_y += velocidad_y
        pelotaRect.topleft = (pelota_x, pelota_y)

    # Deteccion de coliciones

    # La pelota toca un borde de la pantalla
    # La pelota se sale de la pantalla
    # print(pelota_y)

    # hace rebotar cuando toca el fondo
    # pierde y frena la pelota
    # Tarea: modificar para qeu salga desde el medio del jugador

    if (pelota_y >= 600 - 8):
        pelotaEnMovimiento = False
        pelota_x, pelota_y = (24, pelotaEmpiezaEnY)
        pelotaVelocidad = 3
        velocidad_x, velocidad_y = (pelotaVelocidad, pelotaVelocidad)
        pelotaRect.topleft = (pelota_x, pelota_y)
        ladrillos = crear_ladrillos(13) # Tarea-2: a la tercer vida pierda, reiniciar el tablero.

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
    if pelotaRect.colliderect(paletaRect):
        pelota_y = jugadorY - 8
        velocidad_y *= -1

    # Destruir un ladrillo al golpear
    indiceLadrilloTocado = pelotaRect.collidelist(ladrillos)
    rebote = borrar_ladrillo(ladrillos, indiceLadrilloTocado)
    if rebote == 'rebote_x':
        velocidad_x *= -1
    elif rebote == 'rebote_y':
        velocidad_y *= -1

    pygame.display.update()
    cuadros_por_segundo.tick(30)


# Basado en los ejemplos de Sloan Kelly
