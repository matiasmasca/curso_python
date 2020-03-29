
# Translator Rules
# transformar vocales en -> g

def traducir(frase):
  traduccion = ""
  # iterar sobre cada letra de la frase y aplicar las reglas del juego
  for letra in frase:
    if letra in "AEIOUaeiou": #se fija si la letra esta en ese String.
      traduccion = traduccion + "g"
    else:
     traduccion = traduccion + letra
  return traduccion


# tetear la funcion

print("Mi frase: \"Habia un Gato con Botas en una caja que era una ganga\"")
print(traducir("Habia un gato con botas en una caja que era una ganga"))
print("Ahora te toca a vos:")
print(traducir(input("Ingresa tu frase secreta:")))




