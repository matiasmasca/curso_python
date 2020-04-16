import pygame, sys, time, random
from pygame.locals import *


def get_pic_comida():
    bacteria = ["bacteria1", "bacteria2", "bacteria3", "bacteria4", "bacteria5"]
    imagen_original = pygame.image.load('images/' + random.choice(bacteria) + '.png')
    imagenComida = pygame.transform.scale(imagen_original, (40, 25))
    return imagenComida


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
jugador = pygame.Rect(300, 100, 40, 40)

# almacenará un objeto rect que registra el tamaño y la posición del jugador. La variable no contiene la imagen del jugador, sólo su tamaño y posición. Al
# principio del programa, la esquina superior izquierda del jugador se ubica en (300, 100) y el
# jugador tiene una altura y un ancho de 40 píxeles para empezar.



imagenOriginalJugador = pygame.image.load('images/jugador.png') # El valor de retorno es un objeto Surface que tiene el gráfico del archivo dibujado sobre su superficie. Guardamos este objeto Surface dentro de imagenOriginalJugador .
imagenEstiradaJugador = pygame.transform.scale(imagenOriginalJugador, (40, 40))

"""
La función Transform en el módulo pygame.transform.
La función pygame.transform.scale() puede reducir o agrandar un sprite. El primer argumento es un objeto pygame.Surface con la imaten dibujada sobre él.
El segundo argumento es una tupla con los nuevos ancho y altura de la imagen en el primer argumento.
La función scale() devuelve un objeto pygame.Surface con la imagen dibujada en un nuevo tamaño.

Almacenaremos la imagen original en la variable imagen_original, y la imagen estirada se guardará en la variable imagenComida .
Llamamos nuevamente a pygame.image.load() para crear un objeto Surface con la imagen de una bacteria dibujada sobre él.
"""




fondo_org = pygame.image.load('images/blood2.jpg').convert_alpha()
fondo_img = pygame.transform.scale(fondo_org, (400, 400))
fondoRect = fondo_img.get_rect()

comidas = []
for i in range(20):
    item = { "rect": pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20), "img": get_pic_comida() }
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
sonidoRecoleccion = pygame.mixer.Sound('sounds/comer.wav')
pygame.mixer.music.load('sounds/battle-theme-for-achieve-.mid')
pygame.mixer.music.play(-1, 0.0)
musicaSonando = True

"""
los archivos de sonido.
Hay dos módulos para sonido en Pygame.
El módulo pygame.mixer puede reproducir efectos de sonido breves durante el juego.
El módulo pygame.mixer.music puede reproducir música de fondo.
Llamamos a la función constructor pygame.mixer.Sound() para crear un objeto
pygame.mixer.Sound (llamado objeto Sound por brevedad). Este objeto tiene un método play()
que reproducirá el efecto de sonido al ser llamado.

El primer parametro indica cuantas veces repetir el sonido, con -1 hacemos que se repita siempre. Si le pasamos 3, repite 4 veces.
El segudo parametro indica en que punto del archivo se empieza a reproducir, 0.0 es desde el principio.


"""

# ejecutar el bucle del juego
while True:
    # comprobar si se ha disparado el evento QUIT (salir)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN:
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
                # Voy a tener suerte: cambia aleatoreamente el jugador en la pantalla
                jugador.top = random.randint(0, ALTOVENTANA - jugador.height)
                jugador.left = random.randint(0, ANCHOVENTANA - jugador.width)
            if evento.key == ord('m'):
                # activa o desactiva la musica de fondo
                if musicaSonando:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicaSonando = not musicaSonando

        if evento.type == MOUSEBUTTONUP:
            # comidas.append(pygame.Rect(evento.pos[0] - 10, evento.pos[1] - 10, 20, 20))
            item = { "rect": pygame.Rect(evento.pos[0] - 10, evento.pos[1] - 10, 20, 20), "img": get_pic_comida() }
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
        jugador.top += VELOCIDADMOVIMIENTO
    if moverseArriba and jugador.top > 0:
        jugador.top -= VELOCIDADMOVIMIENTO
    if moverseIzquierda and jugador.left > 0:
        jugador.left -= VELOCIDADMOVIMIENTO
    if moverseDerecha and jugador.right < ANCHOVENTANA:
        jugador.right += VELOCIDADMOVIMIENTO


    # dibujar el bloque sobre la superficie
    superficieVentana.blit(imagenEstiradaJugador, jugador)
    """
    Blit dibuja el sprite del jugador sobre el objeto Surface de la ventana (el cual se almacena en superficieVentana.
    El segundo parámetro del método blit() es un objeto Rect que especifica dónde en el objeto
    Surface se dibujará el sprite. El objeto Rect almacenado en jugador es el que registra la posición
    del jugador en la ventana.
    """


    # comprobar si el jugador ha intersectado alguno de los cuadrados de comida
    # En lugar de iterar sobre la lista de comidas con el bucle for, iteramos sobre una copia de la misma. Esta copia se crea usando una parte sin argumentos [:]
    for comida in comidas[:]:
        # print(comida['rect'])
        if jugador.colliderect(comida['rect']):
            comidas.remove(comida)
            jugador = pygame.Rect(jugador.left, jugador.top, jugador.width + 2, jugador.height + 2) # aumenta el tamaño del jugador, aumentando su rectangulo
            imagenEstiradaJugador = pygame.transform.scale(imagenOriginalJugador, (jugador.width, jugador.height)) # le pasamos la imagen original
            if musicaSonando:
                sonidoRecoleccion.play()

    # dibujar la comida
    for comida in comidas:
        # superficieVentana.blit(get_pic_comida(), comida)
         superficieVentana.blit(comida['img'], comida['rect'])

    """
    Llamamos al método blit() y le pasamos el objeto Surface almacenado en imagenComida . (Este es el objeto Surface con la imagen de las cerezas).
    La variable comida (la cual contiene una vez a cada uno de los objetos Rect en la lista comidas
    por cada iteración del bucle) indica al método blit() dónde dibujar imagenComida .
    """

    # dibujar la ventana sobre la pantalla
    pygame.display.update()
    reloj_fps.tick(40)


# Adaptación de los ejemplos de Al Sweigart

