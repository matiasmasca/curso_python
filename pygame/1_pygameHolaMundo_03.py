import pygame, sys
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

# pintar un fondo blanco sobre la ventana
superficieVentana.fill(BLANCO)

# configurar fuentes
# fuenteBasica = pygame.font.SysFont(None, 48)
fuenteBasica = pygame.font.SysFont('Dyuthi', 48)

"""
Pygame puede dibujar texto en cualquier fuente de tu computadora.

Se crea un objeto pygame.font.Font (llamado objeto Font para abreviar) llamando a la función pygame.font.SysFont().
El primer parámetro es el nombre de la fuente, pero le pasaremos el valor None para usar la fuente del sistema por defecto.
El segundo parámetro es el tamaño de la fuente (que se mide en unidades llamadas puntos).

"""

# configurar el texto
texto = fuenteBasica.render('¡Hola mundo!', True, NEGRO, 0)

"""
El objeto Font que has guardado en la variable fuenteBasica tiene un método llamado render().
Este método devolverá un objeto Surface con el texto dibujado sobre él. El primer parámetro de render() es la cadena de texto a dibujar.
El segundo parámetro es un Booleano para indicar si quieres utilizar antialiasing. El antialiasing difumina ligeramente tu texto para
que se vea más suave.
"""

textRect = texto.get_rect()
textRect.centerx = superficieVentana.get_rect().centerx
textRect.centery = superficieVentana.get_rect().centery + 100

"""
El tipo de datos pygame.Rect (llamado Rect para abreviar) representa áreas rectangulares con un cierto tamaño y posición asociados.
Para crear un nuevo objeto llama a la función pygame.Rect(). Los parámetros son enteros para las coordenadas XY de la esquina superior
izquierda, seguidos por el ancho y el alto, todos en píxeles.
El nombre de la función con los parámetros se ve así: pygame.Rect(izquierda, arriba, ancho, alto)
El tipo de datos Rect tiene muchos atributos que describen el rectángulo que representa.

Si modificas alguno de estos atributos, el resto de ellos se modificará automáticamente.
Por ejemplo, si creas un objeto Rect que tiene 20 píxeles de ancho y 20 de alto, cuya esquina superior izquierda está en las coordenadas
(30, 40), entonces la coordenada X del lado derecho si fijará automáticamente en 50 (porque 20 + 30 = 50).

El módulo que importas es pygame, y dentro del módulo pygame están los módulos font y surface.
En Pygame han decidido que los módulos empezaran con minúscula y los tipos de datos con mayúscula. Esto hace más fácil distinguir los tipos de datos de los módulos.

"""

# dibujar el texto sobre la superficie
superficieVentana.blit(texto, textRect)

# dibujar la ventana sobre la pantalla
pygame.display.update()

# ejecutar el bucle del juego
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
