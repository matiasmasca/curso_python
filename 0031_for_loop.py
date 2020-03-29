# Bucles For Each - Bucle "Para cada X"
# repite un conjunto de sentencias un determinado numero de veces. Es muy util para "recorer" listas de valores como listas, cadenas, diccionarios, rangos, etc.

# Una sentencia for comienza con la palabra clave for, seguida por una variable, seguido por la palabra clave in, seguido por un valor iterable, y terminando con dos puntos.
# En cada ejecución, a la variable en la sentencia for se le asigna el valor del siguiente elemento de la lista.

#for <item> in <iterable>:
#   pass

# la variable que se usa despues de la palabra for, es la que tendrá el valor actual en la iteración/vuelta

# Recorriendo una Lista de forma simple.
amigos = ["Juan", "Caren", "Brayan"]
for nombre_amigo in amigos:
  print(nombre_amigo)
print("fin lista \n")



for un_item in "En este conjunto de letras":
  print(un_item)


# la función range() devuelve una secuencia de numeros iniciando en 0, hasta el valor máximo introducido.
# range(5) devuelve range(0, 5)
# es equivalente a la lista [0, 1, 2, 3, 4]
# print(list(range(5)))
# rango de 0 a 4, no incluye a 5.
for contador in range(5):
  print('En esta iteración, el CONTADOR vale ' + str(contador))

# de 0 a 9, no incluye a 10.
for indice in range(10):
  print(indice)
print("fin del for \n")

# de 3 a 9, no incluye a 10.
for indice in range(3, 10):
  print(indice)
print("fin del for \n")

# Recorriendo una Lista de forma manual
amigos = ["Juan", "Caren", "Brayan"]
for index in range(len(amigos)):
  print(amigos[index])

# condiciones simples para un elemento dentro del bucle
amigos = ["Juan", "Caren", "Brayan"]
for index in range(len(amigos)):
  if index == 0:
    print("\n")
    print("=== Lista Amigos ===")
#  else:
#    print("")
  print(amigos[index])
print("=== * ===")

