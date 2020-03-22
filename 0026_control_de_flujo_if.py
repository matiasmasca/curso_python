
# Comparaciones: Operadores de comparación.
# operador de comparacion: >, <, >=, <=, ==, !=

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

resultado = max_num(3,1,9)
print("El mayor es " + str(resultado))



"""
Bloques
Varias líneas de código pueden ser agrupadas en un bloque. Un bloque consiste en líneas de
código que comparten la indentación (o cantidad de espacios desde el borde izquierdo). Puedes ver dónde comienza y termina un
bloque mirando el número de espacios antes de de cada una de las líneas.
"""
