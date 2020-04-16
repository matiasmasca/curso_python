import pygame, sys, time, random
from pygame.locals import *


def get_pic_comida():
    bacteria = ["bacteria1", "bacteria2", "bacteria3", "bacteria4", "bacteria5"]
    imagen_file = pygame.image.load('images/' + random.choice(bacteria) + '.png')
    imagenComida = pygame.transform.scale(imagen_file, (40, 25))
    return imagenComida

def get_rect_comida():
    return pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20)

# configurar pygame
pygame.init()
reloj_fps = pygame.time.Clock()

# configurar la ventana
ANCHOVENTANA = 400
ALTOVENTANA = 400
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0, 32)
pygame.display.set_caption('Battle Bacteria')

# configurar los colores
NEGRO = (0, 0, 0)

# configurar la estructura de bloque de datos
#  RECT (x, y, tamaño_x, tamaño_y)
jugador = pygame.Rect(300, 100, 40, 40)
imagenJugador = pygame.image.load('images/jugador.png')
imagenEstiradaJugador = pygame.transform.scale(imagenJugador, (40, 40))

fondo_org = pygame.image.load('images/blood2.jpg').convert_alpha()
fondo_img = pygame.transform.scale(fondo_org, (ANCHOVENTANA, ALTOVENTANA))
fondoRect = fondo_img.get_rect()

comidas = [ ]
for i in range(20):
    item = { "rect": get_rect_comida(), "img": get_pic_comida() }
    comidas.append(item.copy())

contadorComida = 0
NUEVACOMIDA = 40

# configurar variables del teclado
moverseIzquierda = False
moverseDerecha = False
moverseArriba = False
moverseAbajo = False

VELOCIDADMOVIMIENTO = 8

# configurar música
sonidoComer = pygame.mixer.Sound('sounds/comer.wav')
pygame.mixer.music.load('sounds/battle-theme-for-achieve-.mid')
pygame.mixer.music.play(-1, 0.0)
musicaSonando = True

# ejecutar el bucle del juego
while True:
    # comprobar si se ha disparado el evento QUIT (salir)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN: #precionar una tecla
            # cambiar las variables del teclado
            if evento.key == K_LEFT or evento.key == ord('a'):
                moverseDerecha = False
                moverseIzquierda = True
            if evento.key == K_RIGHT or evento.key == ord('d'):
                moverseIzquierda = False
                moverseDerecha = True
            if evento.key == K_UP or evento.key == ord('w'):
                moverseAbajo = False
                moverseArriba = True
            if evento.key == K_DOWN or evento.key == ord('s'):
                moverseArriba = False
                moverseAbajo = True
        if evento.type == KEYUP:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if evento.key == K_LEFT or evento.key == ord('a'):
                moverseIzquierda = False
            if evento.key == K_RIGHT or evento.key == ord('d'):
                moverseDerecha = False
            if evento.key == K_UP or evento.key == ord('w'):
                moverseArriba = False
            if evento.key == K_DOWN or evento.key == ord('s'):
                moverseAbajo = False
            if evento.key == ord('x'):
                jugador.top = random.randint(0, ALTOVENTANA - jugador.height)
                jugador.left = random.randint(0, ANCHOVENTANA - jugador.width)
            if evento.key == ord('m'):
                if musicaSonando:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicaSonando = not musicaSonando # pasa a lo contrario, lo que estaba en musicaSonando

        if evento.type == MOUSEBUTTONUP:
            item = { "rect": pygame.Rect(evento.pos[0] , evento.pos[1] , 20, 20), "img": get_pic_comida() }
            comidas.append(item.copy())

    contadorComida += 1

    if contadorComida >= NUEVACOMIDA:
        # agregar nueva comida
        contadorComida = 0
        # comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20))
        item = { "rect": pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20), "img": get_pic_comida() }
        comidas.append(item.copy())

    # pintar el fondo negro sobre la superficie
    superficieVentana.fill(NEGRO)
    superficieVentana.blit(fondo_img, fondoRect)

    # mover el jugador
    if moverseAbajo and jugador.bottom < ALTOVENTANA:
        jugador.top += VELOCIDADMOVIMIENTO # 8
    if moverseArriba and jugador.top > 0:
        jugador.top -= VELOCIDADMOVIMIENTO
    if moverseIzquierda and jugador.left > 0:
        jugador.left -= VELOCIDADMOVIMIENTO
    if moverseDerecha and jugador.right < ANCHOVENTANA:
        jugador.right += VELOCIDADMOVIMIENTO

    # dibujar el bloque sobre la superficie
    superficieVentana.blit(imagenEstiradaJugador, jugador)

    # comprobar si el jugador ha intersectado alguno de los cuadrados de comida
    for comida in comidas[:]:
        # print(comida['rect'])
        if jugador.colliderect(comida['rect']):
            comidas.remove(comida)
            jugador = pygame.Rect(jugador.left, jugador.top, jugador.width + 2, jugador.height + 2)
            imagenEstiradaJugador = pygame.transform.scale(imagenJugador, (jugador.width, jugador.height))
            if musicaSonando:
                sonidoComer.play()

    # dibujar la comida
    for comida in comidas:
        # superficieVentana.blit(get_pic_comida(), comida)
         superficieVentana.blit(comida['img'], comida['rect'])

    # dibujar la ventana sobre la pantalla
    pygame.display.update()
    reloj_fps.tick(40)



# Adaptación de los ejemplos de Al Sweigart

