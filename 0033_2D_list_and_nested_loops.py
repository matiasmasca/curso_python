
# 2D list : lista de dos dimenciones
# cada elemento de la primera lista es una lista.
# [] square bracket.

grilla_de_numeros = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  ["\#", 0, "*"]
]

# primero ponemos el indice de la fila y luego el indice del elemento, de la columna.
print(grilla_de_numeros[0][0]) # para mostrar el numero 1
print(grilla_de_numeros[2][1]) # para mostrar el numero 8


# Bucles anidados For each.
# vamos a recorrer la grilla, primero por fila y luego por columna.

# v1

for fila in grilla_de_numeros:
  print(fila)


# v2
# para cada fila
#  y luego para cada columna de la fila
"""
for fila in grilla_de_numeros:
  for columna in fila:
    print("item: " + str(columna))
"""

# Imprmir solo los elementos del medio.
# alternativa 1

for i in range(len(grilla_de_numeros)):
  for j in range(len(grilla_de_numeros[i])):
    if j == 1:
      print(" item del medio: " + str(grilla_de_numeros[i][j]))

# alternativa 2
for fila in grilla_de_numeros:
  item0, item1, item2 = fila
  for item_columna in fila:
    if item_columna == item1:
      print("item: " + str(item_columna))




