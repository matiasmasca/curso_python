
# nos sirven para organizar mucha información
# generalmente guardamos valores relacionados
# se pueden guardar valores de diferentes tipos

# crear una lista
lista_de_amigos = ["Mateo", "Romeo", "Jonas"] #square brackets

print(lista_de_amigos)

# Indice: cada elemento tiene uno, empieza en 0
print(lista_de_amigos[0])
print(lista_de_amigos[1])
print(lista_de_amigos[2])

# acceder de forma inversa
print(lista_de_amigos[-1])
print(lista_de_amigos[-2])
print(lista_de_amigos[-3])

# rango de valores
# también se lo conoce como "Corte de Lista" crea un nuevo valor de lista con un subconjunto de elementos de otra lista.
lista_de_amigos = ["Mateo", "Romeo", "Jonas", "Ricardo", "Santiago"]
print(lista_de_amigos[1:]) # de la posicion 1 en adelante
print(lista_de_amigos[1:3]) # de la posicion 1 en adelante, hasta la 2, excluye la 3

# cambiando valoles
lista_de_amigos[1] = "Julieta"
print(lista_de_amigos)


# Concatenar listas.
lista_de_amigos = ["Mateo", "Romeo", "Jonas"]
nuevos_amigos = ["Sofia", "Romina", "Julieta"]

todos_mis_amigos = lista_de_amigos + nuevos_amigos + ['José', 'Alberto']

print(todos_mis_amigos)



# Split.
# El método split() devuelve una lista en la que cada palabra en la cadena es un elemento aparte. La separación ocurre en cualquier lugar donde haya un espacio en la cadena.
palabras = 'hormiga babuino tejon murcielago oso castor camello gato'.split()
