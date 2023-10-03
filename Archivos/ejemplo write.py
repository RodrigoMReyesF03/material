
# modo w -> Genera un archivo en blanco
with open("ejemplo write.txt", "w", encoding="utf8") as archivo:
    
    # Escribe directamente sobre el archivo
    # archivo.write("Hola\n")
    # archivo.write("mundo")
    
    lista = ["Hola", "mundo", "KABOOM"]
    # archivo.writelines(lista)
    archivo.writelines("\n".join(lista))
    
print("Fin....")