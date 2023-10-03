
# modo a -> Agrega contenido al final del archivo.
with open("ejemplo append.txt", "a", encoding="utf8") as archivo:
    
    archivo.write("Hola")
    
print("Fin...")