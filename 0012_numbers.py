
# Funciones prededinidas
# Python también proporciona funciones que podemos utilizar en las expresiones. Estas funciones se dice que están predefinidas.
# Veamos algunos ejemplos de funciones en numeros.

# Conversion.
# convierten de un tipo a otro.

# float: conversión a flotante. Si recibe un número entero como argumento, devuelve el mismo número convertido en un flotante equivalente.
# La función float también acepta argumentos de tipo cadena. Cuando se le pasa una cadena,float la convierte en el número flotante que ésta representa y sino hay numero se produce un error.

b = float(3.5)
c = float(3.0)

# El número sobre el que se aplica la función se denomina argumento. Observa que el argumento de la función debe ir encerrado entre paréntesis:

# int: conversión a entero. Si recibe un número flotante como argumento, devuelve el entero que se obtiene eliminando la parte fraccionaria.
a = int(3.5)


# str : conversión a cadena. Recibe un número y devuelve una representación de éste como cadena.
print(str(my_num))
print(str(my_num) + " es mi numero favorito")


# para saber el tipo podemos usar la funcion type
type(b)

# valor absoluto
my_num = -5
print(abs(my_num))

# Power: Potencia, base y potencia
print(pow(3,2))

# Max
# devuelve el mayor de los dos
print(max(3,6))

print(min(3,6))

# Redondeo.
# round : redondeo. Puede usarse con uno o dos argumentos. Si se usa con un sólo argumento, redondea el número al flotante más próximo cuya parte decimal sea nula.
print(round(3.3))
print(round(3.3837))

Si round recibe dos argumentos,
éstos deben ir separados por una coma y el segundo indica el número de decimales que
deseamos conservar tras el redondeo.
print(round(3.14159265359, 2))


# Importar otras funciones.
# hay funciones que existen en archivos diferentes llamados "modulos" y que podemos usar importandolas a nuestro codigo con "import"

from math import *

print(floor(3.9)) #devuelve el numero más chico más cercano, quita los decimales
print(ceil(3.1)) # "siil" devuelve el numero mayor más cercano,
print(sqrt(36)) # raiz cuadrada



