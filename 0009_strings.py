frase = "Curso de Python"
print(frase)

# Es posible realizar operaciones con cadenas. Por ejemplo, podemos "sumar" cadenas añadiendo una a otra. Esta operación no se llama suma, sino concatenación y se representa con el signo +.

# Concatenación
print(frase + " esta muy bueno")
print("muy " + "pero " + "muy " + "bueno!")


# Repetición
# podemos repetir una misma cadena un ciertno numero de veces con el signo *
print("Esto es una prueba. " * 3)

# funciones/métodos para cadenas
# Los métodos son funciones adjuntas a un valor. Por ejemplo, todos los valores de cadena tienen el método lower(), el cuál devuelve una copia de la cadena en minúsculas.

print(frase.lower()) # convertir a minusculas
print(frase.upper()) # convertir a MAYUSCULAS
print(frase.isupper()) # esta todo en mayusculas?
print(frase.upper().isupper()) # podemos convinar funciones
print(len(frase)) # cantidad de caracteres de la cadena
print(frase[0]) # caracter por indice en la cadena
print(frase[0] + frase[6] + frase[9]) # iniciales por indice en la cadena
print(frase.index("C"))
print(frase.replace("Python", "Ruby")) # remplazar una cadena dentro de otra

# Caracteres
# Cuando se comparan cadenas, Python va a usar la tabla ASCII para definir quien esta primero.
# con la funcion ORD nos devuelve el nro. de orden de ese caracter en la tabla
print(ord('a')) # 97

print(chr(64)) # @
print(chr(241)) # ñ

print("abajo" < "arriba")


"""
La tabla ASCII presenta un problema cuando queremos ordenar palabras: las letras mayúscu-
las tienen un valor numérico inferior a las letras minúsculas (por lo que ’Zapata’ precede a
’ajo’) y las letras acentuadas son siempre ((mayores)) que sus equivalentes sin acentuar (’aba-
nico’ es menor que ’ábaco’). Hay formas de solucionar eso, pero ya es otra historia.
"""

# Cadenas Multi-Línea
"""
Hasta ahora todas las cadenas han sido de una sola línea y tenían un carácter de comillas al
principio y al final. Sin embargo, si utiliza comillas triples al comienzo y al final entonces la
cadena puede ir a lo largo de varias líneas
"""

print("""
  una cadena
  de
  varias
  lineas""")

