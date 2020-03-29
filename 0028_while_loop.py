# bucles
"""
La sentencia while o "mientras sea" marca el comienzo de un bucle de repetición.
Los bucles pueden ejecutar el mismo código repetidas veces.
Cuando la ejecución llega hasta una sentencia while, evalúa lacondición junto a la palabra reservada while. Si la condición se evalúa a verdadero (True), la ejecución se
mueve dentro del bloque while Si la condición se evalúa a falso (False), la ejecución se mueve hasta debajo del bloque while.
"""

# while condition :

# Paso & Bandera
contador = 0

while contador <= 10:
  print(i)
  i += 1 # ojo sino pones esto... nunca se cumple la condición y será un bucle infinito
print("Termine con el bucle")


# Rompiendo el bucle con "break"
# Una sentencia break indica a la ejecución que salga inmediatamente del bucle while y se mueva a la primera línea a continuación del mismo.

vida = 100

respuesta = input("¿Quiere avanzar por la neblina? (Si / No)")
respuesta = respuesta.lower()
print(respuesta)

if respuesta[0] == "s":
  caminar_neblina = True
  print("No sabia lo que hacia")
else:
  caminar_neblina = False
  print("te arrepientes y vuelves a tu casa")

while caminar_neblina == True:
    if vida < 95:
        print("sobrevive!")
        # caminar_neblina = False
        break
    vida = vida - 1
    print("Quema quema" + str(vida) + str(caminar_neblina))


print("Computadora, informe signos vitales...")
print("Signos vitales: " + str(vida))
