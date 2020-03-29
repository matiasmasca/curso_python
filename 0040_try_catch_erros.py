
# v3
# se pueden dar diferentes tipos de errores.

try:
  # value = 10 / 0
  numero = int(input("Ingrese un numero:"))
  print(numero)
except ZeroDivisionError:
  print("Hey! no se puede dividir por 0")
except ValueError:
  print("Ingreso invalido")

#  IndexError("This is an index error")
# para probar un error podes hacer:
raise IndexError("This is an index error")


# lista completa en https://docs.python.org/3/library/exceptions.html
