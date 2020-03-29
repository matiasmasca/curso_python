
# Pueden ser claves pueden ser numericas, y los valores de diferentes tipos
mesesConNumeros = {
  1: ("January", "Enero", "Janeiro"), # un tupla
  2: ["February", "Febrero", "Fevereiro"], #una lista
  3: "March",
  4: "April",
  5: "May",
  6: "June",
  7: "July",
  8: "August",
  9: "September",
  10: "October",
  11: "November",
  12: "December",
}

print(mesesConNumeros[1])
print(mesesConNumeros[1][1])
print(mesesConNumeros[2][2])


# Tamaño del diccionario.
# podemos usar len() para obtener el tamaño
cantidad_meses = len(mesesConNumeros)
print(cantidad_meses)

# Podemos recorrer un diccionario con un for
for item in mesesConNumeros:
    print(item)



