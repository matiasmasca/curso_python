# primero
"""
 print("Una vez hubo un persona llamada Jorge, ")
 print("el tenia 70 años. ")
 print("A él realmente le gustaba el nombre Jorge, ")
 print("pero a el no le gustaba tener 70 años.")
"""
# segundo
# separar nombres con _, snake_case
# nombre_personaje = "John" # Tom
# edad_personaje = "35" #22

# print("Una vez hubo un persona llamada " + nombre_personaje + ", ")
# print("el tenia " + edad_personaje + " años. ")
# print("A él realmente le gustaba el nombre " + nombre_personaje + ", ")
# print("pero a el no le gustaba tener " + edad_personaje + " años.")

# Tercero. tipo de datos.
# La edad es realmente un numero y no una cadena de caracteres.

nombre_personaje = "Fulanito"
edad_personaje = 35
es_humano = True

print("Una vez hubo un persona llamada " + nombre_personaje + ", ")
print("el tenia " + str(edad_personaje) + " años. ")
print("A él realmente le gustaba el nombre " + nombre_personaje + ", ")
print("pero a el no le gustaba tener " + str(edad_personaje) + " años.")

"""
Los nombres de variables son sensibles a mayúsculas. Sensible a mayúsculas significa que el
mismo nombre de variable con diferente capitalización se considera una variable diferente. De
modo que nombre_personaje , Nombre_personaje , NOMBRE_PERSONAJE, y nombre_PERSONAJE son cuatro variables diferentes.
Cada una de ellas contiene su propio valor independiente. Es una mala idea tener variables con diferente
capitalización en tu programa. En lugar de ello, usa nombres descriptivos para tus variables.
"""
