def obtener_palabra(nombre_archivo : str) -> str:
    with open(nombre_archivo, 'r', encoding='utf8')as archivo:
            palabra = archivo.readline().strip()
            return palabra
    
if __name__ == "__main__":
    resultado = obtener_palabra("Ahorcado/palabras.txt")
    print(resultado)

    