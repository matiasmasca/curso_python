import pygame, random, sys
from pygame.locals import *

CUADROS_POR_SEGUNDO = 40 # Un “cuadro” es el proceso de dibujar los gráficos en la pantalla durante una iteración del bucle del juego.

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
COLOR_NEGRO = (255, 255, 255)
COLOR_BLANCO = (0, 0, 0)

TAMAÑO_MINIMO_ASTEROIDE = 5
TAMAÑO_MAXIMO_ASTEROIDE = 45
VELOCIDAD_MINIMA_ASTEROIDE = 3
VELOCIDAD_MAXIMA_ASTEROIDE = 13
TASA_NUEVO_ASTERODIE = 9
TASA_MOVIMIENTO_JUGADOR = 5

def cerrar_juego():
    pygame.quit()
    sys.exit()

def esperarTeclaJugador():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                cerrar_juego()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:  # Sale del juego al presionar ESCAPE
                    cerrar_juego()
                return

def jugadorGolpeaAsteroide(rectanguloJugador, asteroides):
    for v in asteroides:
        if rectanguloJugador.colliderect(v['rect']):
            return True
    return False

def dibujarTexto(texto, fuente, superficie, x, y):
    objetoTexto = fuente.render(texto, 1, COLOR_NEGRO) # crea un objeto Surface sobre el cual se dibuja el texto con una fuente específica. render(text, antialias, color, background=None)
    rectanguloTexto = objetoTexto.get_rect() # toma la información de ancho y alto de objetoTexto
    rectanguloTexto.topleft = (x, y) # lo ubica en las coordenadas x e y.
    superficie.blit(objetoTexto, rectanguloTexto) # dibuja el objeto Surface del texto renderizado sobre el objeto Surface superficie que recibió como argumento

# establece un pygame, la ventana y el cursor del ratón
pygame.init()
relojPrincipal = pygame.time.Clock()
superficieVentana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) # modo ventana
# superficieVentana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.FULLSCREEN) # modo pantalla completa
pygame.display.set_caption('Chaque\' el cascote')
pygame.mouse.set_visible(False)

# establece las fuentes
fuente = pygame.font.SysFont(None, 48)

# establece los sonidos
sonidoJuegoTerminado = pygame.mixer.Sound('sounds/game_over.ogg')
sonidoExplosion = pygame.mixer.Sound('sounds/Explosion2.wav')
pygame.mixer.music.load('sounds/StarWars - Battle Song[1].mid')

# establece las imagenes
imagenJugador = pygame.image.load('images/nave1.png')
imagenEstiradaJugador = pygame.transform.scale(imagenJugador, (45, 72))
rectanguloJugador = pygame.Rect(0, 0,45,45) # un poco más corto para que no tome el fuego

# fondo de pantalla
fondo_org = pygame.image.load('images/NASA_UCLA_WilliamK_Hartmann.jpg')
fondo_img = pygame.transform.scale(fondo_org, (ANCHO_VENTANA, ALTO_VENTANA))
fondoRect = fondo_img.get_rect()

# para fin del juego
imagenExplosion = pygame.image.load('images/choque_explosion.png')
imagenJugadorExplosion = pygame.transform.scale(imagenExplosion, (220, 222))
rectanguloExplosion = pygame.Rect(0, 0,220,222 )

imagenasteroide = pygame.image.load('images/meteoro3.png')

# Muestra la pantalla inicial
dibujarTexto('La Lluvia Estelar', fuente, superficieVentana, (ANCHO_VENTANA / 4)+40, (ALTO_VENTANA / 4))
dibujarTexto('Presione una tecla para comenzar.', fuente, superficieVentana, (ANCHO_VENTANA / 3) - 180, (ALTO_VENTANA / 3) + 50)
pygame.display.update()
esperarTeclaJugador()

puntajeMax = 0



while True: # este no es tecnicamente el bucle del juego
    # establece el comienzo del juego
    asteroides = []
    puntaje = 0
    rectanguloJugador.topleft = (ANCHO_VENTANA / 2, ALTO_VENTANA - 50) # jugador en el medio de la pantalla.
    moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
    trucoReversa = trucoLento = False
    contadorAgregarAsteroide = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # el bucle del juego se mantiene mientras se este jugando
     # El bucle del juego gestiona los eventos y dibuja la ventana mientras el juego está ejecutándos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                cerrar_juego()

            if evento.type == KEYDOWN:
                if evento.key == ord('z'):
                    trucoReversa = True
                if evento.key == ord('x'):
                    trucoLento = True
                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverDerecha = False
                    moverIzquierda = True
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverIzquierda = False
                    moverDerecha = True
                if evento.key == K_UP or evento.key == ord('w'):
                    moverAbajo = False
                    moverArriba = True
                if evento.key == K_DOWN or evento.key == ord('s'):
                    moverArriba = False
                    moverAbajo = True

            if evento.type == KEYUP:
                if evento.key == ord('z'):
                    trucoReversa = False
                    # puntaje = 0
                if evento.key == ord('x'):
                    trucoLento = False
                    # puntaje = 0
                if evento.key == K_ESCAPE:
                        cerrar_juego()
                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverIzquierda = False
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverDerecha = False
                if evento.key == K_UP or evento.key == ord('w'):
                    moverArriba = False
                if evento.key == K_DOWN or evento.key == ord('s'):
                    moverAbajo = False

            if evento.type == MOUSEMOTION:
                # Si se mueve el ratón, este se mueve al lugar donde esté el cursor.
                rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx, evento.pos[1] - rectanguloJugador.centery)

        """
        El Método move_ip()
        El método move_ip() para objetos Rect modificará horizontal o verticalmente la posición del objeto Rect en un número de píxeles.

        El "ip" al final del método move_ip() es la abreviatura de "in place" (que en español significa "en el lugar"). Esto quiere decir que el método modifica
        al propio objeto Rect, y no devuelve un nuevo objeto Rect con los cambios. También existe un método move() que no modifica al objeto Rect sino que crea y devuelve un nuevo objeto Rect en la nueva ubicación.

        """
        # Añade asteroides en la parte superior de la pantalla
        if not trucoReversa and not trucoLento:
            contadorAgregarAsteroide += 1
        if contadorAgregarAsteroide >= TASA_NUEVO_ASTERODIE:
            contadorAgregarAsteroide = 0
            tamañoAsteroide = random.randint(TAMAÑO_MINIMO_ASTEROIDE, TAMAÑO_MAXIMO_ASTEROIDE)
            nuevoAsteroide = {'rect': pygame.Rect(random.randint(0, ANCHO_VENTANA-tamañoAsteroide), 0 - tamañoAsteroide, tamañoAsteroide, tamañoAsteroide),
                              'velocidad': random.randint(VELOCIDAD_MINIMA_ASTEROIDE, VELOCIDAD_MAXIMA_ASTEROIDE),
                              'superficie':pygame.transform.scale(imagenasteroide, (tamañoAsteroide, tamañoAsteroide)),
                              }
            asteroides.append(nuevoAsteroide)

        # Mueve el jugador.
        if moverIzquierda and rectanguloJugador.left > 0:
            rectanguloJugador.move_ip(-1 * TASA_MOVIMIENTO_JUGADOR, 0)
        if moverDerecha and rectanguloJugador.right < ANCHO_VENTANA:
            rectanguloJugador.move_ip(TASA_MOVIMIENTO_JUGADOR, 0)
        if moverArriba and rectanguloJugador.top > 0:
            rectanguloJugador.move_ip(0, -1 * TASA_MOVIMIENTO_JUGADOR)
        if moverAbajo and rectanguloJugador.bottom < ALTO_VENTANA:
            rectanguloJugador.move_ip(0, TASA_MOVIMIENTO_JUGADOR)

        # Mueve el cursor del ratón hacia el jugador.
        pygame.mouse.set_pos(rectanguloJugador.centerx, rectanguloJugador.centery)

        # Mueve los asteroides hacia abajo.
        for item in asteroides:
            if not trucoReversa and not trucoLento:
                item['rect'].move_ip(0, item['velocidad'])
            elif trucoReversa:
                item['rect'].move_ip(0, -5)
            elif trucoLento:
                item['rect'].move_ip(0, 1)

        # Elimina los asteroides que han caido por debajo.
        # [:] develve una copia de la lista con todos sus ítems (del primero al último).
        # No puedes agregar o quitar ítems de una lista mientras estás iterando sobre ella. Python puede
        # perder la cuenta de cuál debería ser el próximo valor de la variable comida si el tamaño de la lista
        # asteroides está cambiando

        for item in asteroides[:]:
            if item['rect'].top > ALTO_VENTANA:
                asteroides.remove(item)

        # Dibuja el mundo del juego en la ventana.
        superficieVentana.fill(COLOR_BLANCO)
        superficieVentana.blit(fondo_img, fondoRect)

        # Dibuja el puntaje y el puntaje máximo
        dibujarTexto('Puntaje: %s' % (puntaje), fuente, superficieVentana, 10, 0)
        dibujarTexto('Puntaje Máximo: %s' % (puntajeMax), fuente, superficieVentana, ANCHO_VENTANA/2, 0)

        # Dibuja el rectángulo del jugador
        superficieVentana.blit(imagenEstiradaJugador, rectanguloJugador)

        # Dibuja cada asteroide
        for v in asteroides:
            superficieVentana.blit(v['superficie'], v['rect'])

        pygame.display.update()

        # Verifica si algún asteroide impactó en el jugador.

        if jugadorGolpeaAsteroide(rectanguloJugador, asteroides):
            if puntaje > puntajeMax:
                puntajeMax = puntaje # Establece nuevo puntaje máximo
            rectanguloExplosion.centerx = rectanguloJugador.centerx - 40
            rectanguloExplosion.centery = rectanguloJugador.centery - 10
            sonidoExplosion.play()
            superficieVentana.blit(imagenJugadorExplosion, rectanguloExplosion)
            break # sale del bucle while

        puntaje += 1 # incrementa el puntaje
        # añadir dificultad

        relojPrincipal.tick(CUADROS_POR_SEGUNDO)

    # Detiene el juego y muestra "Juego Terminado"
    pygame.mixer.music.stop()
    sonidoJuegoTerminado.play()

    dibujarTexto('Juego Terminado', fuente, superficieVentana, (ANCHO_VENTANA / 3)-40, (ALTO_VENTANA / 3))
    dibujarTexto('Presione una tecla jugar de nuevo.', fuente, superficieVentana, (ANCHO_VENTANA / 3) - 150, (ALTO_VENTANA / 3) + 50)
    pygame.display.update()

    esperarTeclaJugador()

    sonidoJuegoTerminado.stop()



# Adaptación de los ejemplos de Al Sweigart
