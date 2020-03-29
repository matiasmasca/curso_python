# Juego basico de adivinanza
# el participante debe encontrar la palabra secreta
# ingresa respuestas hasta que acierta la palabra o sale.

# usaremos variables, bugles, condiciones if

# version 2
# agregamos una cantidad maxima de intentos

palabra_secreta = "gamer"
suposicion = ""
contador_de_intentos = 0
limite_de_itentos = 3
llego_al_limite = False

while suposicion != palabra_secreta and not(llego_al_limite):
 if contador_de_intentos < limite_de_itentos:
  contador_de_intentos += 1
  suposicion = input("Ingresar palabra secreta: ")
 else:
  llego_al_limite = True

if llego_al_limite:
  print("Perdiste! te quedaste sin intentos, \n segui participando...")
else:
  print("Ganaste, sos re hacker!")

