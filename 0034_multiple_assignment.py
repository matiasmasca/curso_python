
# Asignación Múltiple
# Puedes especificar múltiples variables, separadas por comas, al lado izquierdo de la declaración de asignación. Y python asigrnara los valores a las variables automaticamente.
a, b, c = ['esto va a ir en a', 'esto en b', 'esto en c']
# es equivalente a
a = ['esto va a ir en a', 'esto en b', 'esto en c'][0] # de la lista, asigna el que este en la posion 0 a la variable a
b = ['esto va a ir en a', 'esto en b', 'esto en c'][1]
c = ['esto va a ir en a', 'esto en b', 'esto en c'][2]

item_a, cantidad_a, item_b, cantidad_b, item_c, catidad_c = ['Amacas', 8, 'Calecita', 2, 'Arboles', 10]


# Interpolación de Cadenas
# Para evitar estar concatenando cadenas, y el esfuerzo extra que eso podría traer. Existe una forma de crear las cadenas de forma dinamica.
# Llamada "interpolación de cadenas", lo cual te permite utilizar comodines como %s para luego en su lugar replazar por el valor de una variable.
# Estos comodines %s se llaman especificadores de conversión.
# Python remplazará los comodines por los valores en las variables al final de la sentencia.

"""
Manuelita vivía en Pehuajó
Pero un día se marchó.
Nadie supo bien por qué
A París ella se fue
Un poquito caminando
Y otro poquitito a pie.
"""

nombre = 'Muelita'
evento = 'Pehuajó'
donde = 'París'
primero = 'caminando'
segundo = 'pie'

print('%s vivía en %s Pero un día se marmarchócho Nadie supo bien por qué a %s ella se fue Un poquito %s Y otro poquitito a %s ' % (nombre, evento, donde, primero, segundo))
# Muelita vivía en Pehuajó Pero un día se marmarchócho Nadie supo bien por qué a París ella se fue Un poquito caminando Y otro poquitito a pie

# agregando saltos de linea con \n
print('%s vivía en %s \n Pero un día se marmarchócho \n Nadie supo bien por qué \n a %s ella se fue \n Un poquito %s \n Y otro poquitito a %s ' % (nombre, evento, donde, primero, segundo))

# Salida esperada:
"""
Manuelita vivía en Pehuajó
Pero un día se marchó.
Nadie supo bien por qué
A París ella se fue
Un poquito caminando
Y otro poquitito a pie.
"""

"""
La interpolación de cadenas puede hacer tu código mucho más fácil de escribir. El primer
nombre de variable corresponde al primer %s, la segunda variable va con el segundo %s
y así sucesivamente. debes tener tantos %s (especificadores de conversión) como variables.

Otro beneficio de usar interpolación de cadenas en lugar de concatenación es que la interpolación funciona con cualquier tipo de datos, no sólo cadenas.
Todos los valores se convierten automáticamente al tipo de datos cadena.
"""
