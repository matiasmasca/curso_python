
# Funciones definidas en módulos
"""
Python también proporciona funciones trigonométricas, logaritmos, etc., pero no están directa-
mente disponibles cuando iniciamos una sesión. Antes de utilizarlas hemos de indicar a Python
que vamos a hacerlo. Para ello, importamos cada función de un módulo.

Podemos importar una parte o todas las que hayan en el modulo.

from math import sin # solo importa la funsion sin
from math import * # importa todo
"""

"""
sin(x): Seno de x, que debe estar expresado en radianes.
cos(x): Coseno de x, que debe estar expresado en radianes.
tan(x): Tangente de x, que debe estar expresado en radianes.
exp(x): El número e elevado a x.
ceil (x): Redondeo hacia arriba de x (en inglés, ((ceiling)) significa techo).
floor (x): Redondeo hacia abajo de x (en inglés, ((floor)) significa suelo).
log(x): Logaritmo natural (en base e) de x.
log10(x): Logaritmo decimal (en base 10) de x.
sqrt(x): Raı́z cuadrada de x (del inglés ((square root))).
"""

# Importar otras funciones.
from math import *

print(floor(3.9)) #devuelve el numero más chico más cercano, quita los decimales
print(ceil(3.1)) # "siil" devuelve el numero mayor más cercano,
print(sqrt(36)) # raiz cuadrada

print(pi)
print(e)




# Para evitar problemas con los nombres de las variables, las funciones, etc.
# Hay otra forma de importar. Pero hay que anteponer math.nombre_funcion para poder usar. Es decir nombre_del_modulo.nombre_funcion
import math
math.sin(0)


import random
numero = random.randint(1, 20)
print(numero)
