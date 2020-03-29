
# vemos como convinando bloques For each con If tenemos una herramienta poderosa.

# Version 2:
# se pierde la capitalización (cuando arranca la palabra con mayuscula) de la frase, por eso mejorarmos la funcion.

def traducir(frase):
  traduccion = ""
  # iterar sobre cada letra de la frase y aplicar las reglas del juego
  for letra in frase:
    if letra.lower() in "aeiou": #se fija si la letra esta en ese String.
      if letra.isupper():
        traduccion = traduccion + "G"
      else:
        traduccion = traduccion + "g"
    else:
     traduccion = traduccion + letra
  return traduccion


# tetear la funcion

print("Mi frase: \"Habia un Gato con Botas en una caja que era una ganga\"")
print(traducir("Habia un gato con botas en una caja que era una ganga"))
print("Ahora te toca a vos:")
print(traducir(input("Ingresa tu frase secreta:")))


# version: 2.2... hacer que las letras no vocales tambien se capitalisen.



