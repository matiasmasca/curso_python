
# abrir el archivo
# posision relativa, absoluta, o si esta en la misma carpeta que el codigo
# modos de apertura:
# - r para read, leer.
# - w para write, escribir
# - a para append, agregar al final del archivo algo.
# - r+ para read and write, para leer y escribir.

archivo_empleados = open("0041_reading_files_employees.txt", "r")
# acordate siempre de cerrar el archivo. archivo_empleados.close()

# veamos que hay adentro.
# archivo_empleados.readable() va a devolvernos TRUE si puede leer el archivo.
# print(archivo_empleados.readable())

# archivo_empleados.read() devuelve todo el archivo.
# print(archivo_empleados.read())

# archivo_empleados.readline(), lee linea por linea, empezando por la primera.
# print(archivo_empleados.readline())
# print(archivo_empleados.readline())

# readlines: lee las lineas y las guarda en una lista
# print(archivo_empleados.readlines())
# print(archivo_empleados.readlines()[3]) # con el indice puedo ver un valor puntual

# Recorrer el archivo con un for each...
for empleado in archivo_empleados.readlines():
  print(empleado)

archivo_empleados.close() # acordate siempre de cerrar el archivo.
