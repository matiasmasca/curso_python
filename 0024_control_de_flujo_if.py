# sentencia IF
# el programa responde a los datos que tiene, a los valores que se le pasa.
# en el dia a dia, resolvemos este tipo de declaraciones
# donde hay condiciones



# Ahora si, en python

es_humano = False

if es_humano:
  print("Usted es un ser humano")
else:
  print("Usted no es un ser humano")

"""
Condicion
Una condición es una expresión que combina dos valores con un operador de comparación (tal
como < o > ) y se evalúa a un valor Booleano. Una condición es sólo otro nombre para una
expresión que se evalúa a True o False
"""

# Más de una condicion
# OR: uno u otro o ambos
es_humano = True
es_mago = True

if es_humano or es_mago:
  print("Usted es un humano o es mago o ambos")
else:
  print("Usted no es un humano ni mago")

# AND ambos tienen que ser verdadero
es_humano = True
es_mago = False

if es_humano and es_mago:
  print("Usted es un humano y es mago")
else:
  print("Usted no es un humano o no es mago")

# Else if
