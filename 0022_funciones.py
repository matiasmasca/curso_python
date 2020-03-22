# Return:
# podemos definir que devuelve la funcion.

# luego de ejecutar devuelve ese valor de la funcion
# por defecto devuelve: none
# es decir, sino se define return, ejecutará y devolverá none.

def cubo_de_numero(numero):
  return numero * numero * numero
  # si pongo algo luedo del return, ya no se ejecutara

print(cubo_de_numero(3))


# Otra forma de utilizar una funcion
# guardar el resultado de la funcion en una variable
def cubo_de_numero(numero):
  return numero * numero * numero

resultado = cubo_de_numero(4)
print(resultado)


# Uso de Expresiones en Llamadas a Funciones
# Como los argumentos son siempre valores individuales. Python evaluará primero esta expresión y luego pasará este valor como argumento.

resultado = cubo_de_numero(2 + 2)
print(resultado)
