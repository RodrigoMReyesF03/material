import random

def generar_llave() -> str:
    abc = "abcdefghijklmnñopqrstuvwxyz"
    llave = ""
    while len(llave) != len(abc):
        letra = abc[random.randint(0, len(abc) - 1)]
        if letra not in llave:
            llave += letra
    return llave

def cifrar(texto : str, llave : str) -> str:
    texto = texto.lower()
    abc = "abcdefghijklmnñopqrstuvwxyz"
    cifrado = ""
    for letra in texto:
        if letra in abc:
            cifrado += llave[abc.find(letra)]
        else:
            cifrado += letra
    return cifrado

def descifrar(texto : str, llave : str) -> str:
    texto = texto.lower()
    abc = "abcdefghijklmnñopqrstuvwxyz"
    cifrado = ""
    for letra in texto:
        if letra in llave:
            cifrado += abc[llave.find(letra)]
        else:
            cifrado += letra
    return cifrado

def cifrar_archivo(origen : str, destino : str, llave : str) -> None:
    with open(origen, "r", encoding="utf8") as entrada:
        with open(destino, "w", encoding="utf8") as salida:
            for linea in entrada:
                salida.write(cifrar(linea, llave))
                
def descifrar_archivo(origen : str, destino : str, llave : str) -> None:
    with open(origen, "r", encoding="utf8") as entrada:
        with open(destino, "w", encoding="utf8") as salida:
            for linea in entrada:
                salida.write(descifrar(linea, llave))

if __name__ == "__main__":
    llave = generar_llave()
    print(f"Llave generada: {llave}")
    
    texto = "Hola mundo"
    cifrado = cifrar(texto, llave)
    print(f"Texto cifrado: {cifrado}")
    
    descifrado = descifrar(cifrado, llave)
    print(f"Texto descifrado: {descifrado}")
    
    cifrar_archivo("ejemplo para cifrar.txt", "ejemplo cifrado.txt", llave)
    print("Archivo cifrado...")
    
    descifrar_archivo("ejemplo cifrado.txt", "ejemplo descifrado.txt", llave)
    print("Archivo descifrado...")