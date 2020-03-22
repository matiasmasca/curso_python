# calculadora elemental
# El usuario ingresa un numero, la operación y otro numero.
numero_1 = float(input("Ingrese un numero: "))
operador = input("Ingrese el operador (+, - , /, *): ")
numero_2 = float(input("Ingrese otro numero: "))

print("El resultado es:")

if operador == "+":
  print(numero_1 + numero_2)
elif operador == "-":
   print(numero_1 - numero_2)
elif operador == "/":
   print(numero_1 / numero_2)
elif operador == "*":
   print(numero_1 * numero_2)
else:
  print("Operación invalida, ingrese: +, - , /, *")

