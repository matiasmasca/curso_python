import herramientas_utiles

# sin la extension,
# ojo con el nombre, con numeros al principio no funciona.
# un modulo es un archivo de python qu epodemos invocar o importar en nuestro codigo. para tener acceso a esas
# funciones.
# evitemos el copy and paste...

print(herramientas_utiles.roll_dice(10))

# Modulos en python.
# https://docs.python.org/3/py-modindex.html
# depende de la version
# estos son modulos que vienen en python y que los podemos importar cuando quieras.
# en el listado lo que no tengan una URL de donde estan ubicados son los que se usan directamente, los otros hay que ubircar donde estan en tu maquina.

# podemos guardar los modulos en una carpeta llamada "lib".

# build-in modules.
# los que vienen con python por defecto
# external modules.
# otros modulos que podemos usar, generalmente en una carpeta /lib

 PIP
# es una herramienta para administrar paquetes, o librerias. Y poder instalarlos en nuestra maquina facilmente.
# viene pre-instalado desde Python 3.
 Para saber si lo tengo: $ pip --version
# Para saber que paquetes tengo: $ pip list
 Para instalar algo: $ pip install ModuleName
# Si quiero instalar algo llamado python-docx
 $ pip install python-docx
# en el programa import docx y luego usarlo ... docx.MetodoDeDocx
 con $ pip uninstall, lo desinstalamos.

