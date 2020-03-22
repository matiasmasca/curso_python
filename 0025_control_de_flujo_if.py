
# Else if
# AND ambos tienen que ser verdadero
es_humano = False
es_mago = True

if es_humano and es_mago:
  print("Usted es un humano y es mago")
elif es_humano and not(es_mago):
  print("Usted es un humano y no es mago")
else:
  print("Usted no es un humano o no es mago")

if es_humano and es_mago:
  print("Usted es un humano y es mago")
elif es_humano and not(es_mago):
  print("Usted es un humano y no es mago")
elif not(es_humano) and es_mago:
  print("Usted no es humano pero es mago")
else:
  print("Usted no es un humano ni es mago, aqui no puedes entrar!")


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




