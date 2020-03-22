# Parametros
# Parametros: información adicional que se le pasa a la funcion


# en este caso le pasamos name al llamarla o invocarla.
def saludar_usuario(name):
  print("Hola " + name + "!" )

saludar_usuario("Miguel")
saludar_usuario("Pedro")

# más de un parametro
def saludar_usuario(name, age):
  print("Hola " + name + "!, tu tienes " + str(age))

saludar_usuario("Miguel", 15)
saludar_usuario("Pedro", 32)









