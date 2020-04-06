import pygame, sys, time
from pygame.locals import *

# configurar pygame
pygame.init()

# configurar la ventana
superficieVentana = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('¡Hola mundo!')

# configurar los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# configurar fuentes
fuenteBásica = pygame.font.SysFont(None, 48)

# configurar el texto
texto = fuenteBásica.render('¡Hola mundo!', True, BLANCO, AZUL)
textRect = texto.get_rect()
textRect.centerx = superficieVentana.get_rect().centerx
textRect.centery = superficieVentana.get_rect().centery



# pintar un fondo blanco sobre la ventana
superficieVentana.fill(BLANCO)

# dibujar un rectangulo de 340 pix de ancho por 50 de alto.
pygame.draw.rect(superficieVentana, VERDE, (10, 10, 340, 50))

"""
La función pygame.draw.rect() dibuja un rectángulo. El tercer parámetro es una tupla de cuatro
enteros para los bordes izquierdo y superior, ancho y altura del rectángulo. En lugar de una tupla
de cuatro enteros para el tercer parámetro, también puedes pasarle un objeto Rect.
"""

# dibujar el rectángulo de fondo para el texto sobre la superficie
pygame.draw.rect(superficieVentana, ROJO, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

"""
el rectángulo que dibujas esté 20 píxeles alrededor del rectángulo de texto. Es por esto que los bordes inquierdo y superior del rectángulo
corresponden a los bordes izquierdo y superior de textRect menos 20. (Recuerda, restas porque las coordenadas disminuyen
cuando te mueves hacia arriba y hacia la izquierda.) Y el ancho y la altura corresponden al ancho
y a la altura de textRect más 40 (para compensar por el desplazamiento adicional de 20 píxeles de
los bordes izquierdo y superior).
"""

# dibujar el texto sobre la superficie
superficieVentana.blit(texto, textRect)

"""
El método blit() dibujará los contenidos de un objeto Surface sobre otro objeto Surface.
El segundo parámetro de blit() especifica dónde en la superficie de superficieVentana se dibuja
el texto. En este caso se pasa el objeto Rect que devuelve la llamada a text.get_rect()
"""



# dibujar la ventana sobre la pantalla
pygame.display.update()

# ejecutar el bucle del juego
contador = 0

while True:
  contador += 10
  if contador >= 100:
    contador = 0
  superficieVentana.fill(BLANCO)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.draw.rect(superficieVentana, ROJO, (textRect.left - contador, textRect.top - contador, textRect.width + contador, textRect.height + contador))

  superficieVentana.blit(texto, textRect)
  pygame.display.update()
  time.sleep(0.10)
