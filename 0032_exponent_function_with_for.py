# Funcion exponencial.
# la idea es usar bucles For, para calcular la potencia.
# pero dentro de una funcion para ordenar el codigo.


# de forma nativa en python, la potencia se puede calcular como
print("potencia nativa:")
print(2**2) # dos a la dos, dos al cuadrado
print(3**2) # 3 al cuadrado
print("\n")



def elevar_a_potencia(base_num, potencia_num):
  resultado = 1
  for index in range(potencia_num): #tantas veces como potencia_num
    resultado = resultado * base_num # lo multiplicamos por si mismo
  return resultado

print("potencia por funcion propia:")
print(elevar_a_potencia(3, 2)) # tiene que imprimir 9
