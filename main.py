import pygame, random, sys
from pygame.locals import *

ANCHO_VENTANA = 800
ALTO_VENTANA = 600

COLOR_NEGRO = (255, 255, 255)
COLOR_BLANCO = (0, 0, 0)

CUADROS_POR_SEGUNDO = 40

TAMAÑO_MINIMO_ASTEROIDE = 6
TAMAÑO_MAXIMO_ASTEROIDE = 40
VELOCIDAD_MINIMA_ASTEROIDE = 1
VELOCIDAD_MAXIMA_ASTEROIDE = 18
TASA_NUEVO_ASTERODIE = 6
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
                if evento.key == K_RETURN:  # Sale del juego al presionar ESCAPE
                    cerrar_juego()
                return

def jugadorGolpeaAsteroide(rectangulo, lista):
    for item in lista:
        if rectangulo.colliderect(item['rect']):
            return True
    return False

def dibujarTexto(texto, fuente, superficie, x, y):
    objetoTexto = fuente.render(texto, 1, COLOR_NEGRO)
    rectanguloTexto = objetoTexto.get_rect()
    rectanguloTexto.topleft = (x, y)
    superficie.blit(objetoTexto, rectanguloTexto)



# establece un pygame, la ventana y el cursor del ratón
pygame.init()
relojPrincipal = pygame.time.Clock()

superficieVentana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) # , pygame.FULLSCREEN
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

while True:
    # establece el comienzo del juego
    asteroides = []
    puntaje = 0
    rectanguloJugador.topleft = (ANCHO_VENTANA / 2, ALTO_VENTANA - 50)
    moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
    trucoReversa = trucoLento = False
    contadorAgregarAsteroide = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # el ciclo del juego se mantiene mientras se este jugando
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

            if evento.type == MOUSEMOTION: # (x,y)
                # Si se mueve el ratón, este se mueve al lugar donde esté el cursor.
                rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx, evento.pos[1] - rectanguloJugador.centery)
                # rectangulo.move(x,y)
        # Añade asteroides en la parte superior de la pantalla
        if not trucoReversa and not trucoLento:
            contadorAgregarAsteroide += 1

        if contadorAgregarAsteroide >= TASA_NUEVO_ASTERODIE:
            contadorAgregarAsteroide = 0
            tamañoAsteroide = random.randint(TAMAÑO_MINIMO_ASTEROIDE, TAMAÑO_MAXIMO_ASTEROIDE) # 10, 11,12,123-- 40
            # RECT (x,y, ancho, alto)
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
        """
         asteroide = {'rect': rect(10, 20, 5,5),
                           'velocidad':18,
                              'superficie': imagen del asteroide chiquito,
                              }
        """
        for asteroide in asteroides:
            if not trucoReversa and not trucoLento:
                asteroide['rect'].move_ip(0, asteroide['velocidad'])
            elif trucoReversa:
                asteroide['rect'].move_ip(0, -5)
            elif trucoLento:
                asteroide['rect'].move_ip(0, 1)

        # Elimina los asteroides que han caido por debajo.
        for asteroide in asteroides[:]:
            if asteroide['rect'].top > ALTO_VENTANA: #600...
                asteroides.remove(asteroide)

        # Dibuja el mundo del juego en la ventana.
        superficieVentana.fill(COLOR_BLANCO)
        superficieVentana.blit(fondo_img, fondoRect)

        # Dibuja el puntaje y el puntaje máximo
        puntaje += 1 # incrementa el puntaje
        dibujarTexto('Puntaje: %s' % (puntaje), fuente, superficieVentana, 10, 0)
        dibujarTexto('Puntaje Máximo: %s' % (puntajeMax), fuente, superficieVentana, ANCHO_VENTANA/2, 0)

        # Dibuja el rectángulo del jugador
        superficieVentana.blit(imagenEstiradaJugador, rectanguloJugador)

        # Dibuja cada asteroide
        for asteroide in asteroides:
            superficieVentana.blit(asteroide['superficie'], asteroide['rect'])

        pygame.display.update()

        # Verifica si algún asteroide impactó en el jugador.
        if jugadorGolpeaAsteroide(rectanguloJugador, asteroides):
            if puntaje > puntajeMax:
                puntajeMax = puntaje # Establece nuevo puntaje máximo
            rectanguloExplosion.centerx = rectanguloJugador.centerx #- 40
            rectanguloExplosion.centery = rectanguloJugador.centery #- 10
            sonidoExplosion.play()
            superficieVentana.blit(imagenJugadorExplosion, rectanguloExplosion)

            break # sale del bucle while


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
