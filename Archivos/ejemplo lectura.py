
archivo = open("ejemplo lectura.txt", "r", encoding="utf8")

# Carga el contenido del archivo como un string
# No se recomienda usar con archivos grandes
# contenido = archivo.read()
# print(contenido)

# Lee la línea actual hasta el salto de línea
# y recorre el apuntador.
# linea = archivo.readline()
# print(linea)
# linea = archivo.readline()
# print(linea)

# Carga todo el contenido del archivo en una lista
# donde cada elemento está delimitado por el 
# salto de línea. No se recomienda con archivos
# grandes.
# lista = archivo.readlines()
# print(lista)

# Recorre el archivo línea por línea
for linea in archivo:
    if "ejemplo" in linea:
        print("Lo encontré")

archivo.close()