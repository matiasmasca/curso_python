
# Que hacemos cuando hay errores en nuestros programas?
# cuando potencialmente tenemos más errores?


numero = int(input("Ingrese un numero:"))
print(numero)

 #fin v1

# v2 atrapemos ese error potencial


try:
  numero = int(input("Ingrese un numero:"))
  print(numero)
except:
  print("Ingreso invalido")

# ese except asi como esta, capata solo lo que este adentro del try y no otro error en el programa



