numeros_de_la_suerte = [3, 4, 8, 13, 21, 81]
lista_de_amigos = ["Mateo", "Romeo", "Julieta", "Jonas", "Ricardo", "Santiago"]

print(lista_de_amigos)

# Funciones para listas.
# extend: le suma una lista, a otra lista
# lista_de_amigos.extend(numeros_de_la_suerte)
# print(lista_de_amigos)

# append: agrega un elemento al final de la lista
# lista_de_amigos.append("Jacinto")
# print(lista_de_amigos)

# insert: agrega un elemento en la posicion indicada. Moviendo todo hacia la derecha.
lista_de_amigos.insert(1, "Luciana")
print(lista_de_amigos)

# remove: ingresar el elemnto a eliminar
lista_de_amigos.remove("Luciana")
print(lista_de_amigos)

# pop : quita el último elemento de la lista.
lista_de_amigos.pop()
print(lista_de_amigos)

# del lista[indice] : del elimina un elmento de la lista por su indice. La sentencia del es una sentencia, no una función ni un operador. No tiene paréntesis ni devuelve un valor.
del lista_de_amigos[2]

# index: devuelve el indice de un elemento, devuelve un error sino encuentra nada
print(lista_de_amigos.index("Mateo"))

# count : cuenta cuantas veces aparece un valor en la lista.
lista_de_amigos = ["Mateo", "Romeo", "Julieta", "Jonas", "Ricardo", "Sergio", "Sergio"]
print(lista_de_amigos.count("Mateo"))
print(lista_de_amigos.count("Sergio"))

# sort : ordena de forma ascendente, de menor a mayor.
lista_de_amigos.sort()
print(lista_de_amigos)

numeros_de_la_suerte.sort()
print(numeros_de_la_suerte)

# reverse : ordena en orden inverso
numeros_de_la_suerte.reverse()
print(numeros_de_la_suerte)

# copy : copiar una lista a otra
otros_amigos = lista_de_amigos.copy()
print(otros_amigos)

# operador in.
# El operador in te puede decir si un valor está en una lista o no. Las expresiones que usan el
# operador in devuelven un valor lógico: True si el valor está en la lista y False si no está.
lista_de_amigos = ["Mateo", "Romeo", "Julieta", "Jonas", "Ricardo", "Sergio", "Sergio"]
'Jonas' in lista_de_amigos
'Julian' in lista_de_amigos
