import math

def quita_vocales(texto : str) -> str:
    vocales = "aeiouáéíóú"
    for i in vocales:
        texto = texto.replace(i, "").replace(i.upper(), "")
    return texto

def palindromo(texto : str) -> bool:
    texto = texto.lower()
    res = ""
    for letra in texto:
        if letra.isalpha():
            res += letra
    return res == res[::-1]

def cambio(texto : str) -> str:
    voc1 = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    voc2 = "eiouaEIOUAéíóúáÉÍÓÚÁ"
    res = ""
    for letra in texto:
        if letra in voc1:
            res += voc2[voc1.index(letra)]
        else:
            res += letra
    return res

def cifrado_cesar(texto : str, recorrido : int) -> str:
    texto = texto.lower()
    abc = "abcdefghijklmnñopqrstuvwxyz"
    res = ""
    for letra in texto:
        if letra.isalpha():
            res += abc[(abc.find(letra) + recorrido) % len(abc)]
        else:
            res += letra
    return res

def descifrado_cesar(texto : str, recorrido : int) -> str:
    return cifrado_cesar(texto, -recorrido)
        
if __name__ == "__main__":
    # texto = "Hola Árbol Algo"
    # resultado = quita_vocales(texto)
    # print(f"El resultado es: {resultado}")
    
    # texto = "No lemon, no melon."
    # resultado = palindromo(texto)
    # print(f"\"{texto}\" es un palíndromo: {resultado}")
    # texto = "Anita lava la tina."
    # resultado = palindromo(texto)
    # print(f"\"{texto}\" es un palíndromo: {resultado}")
    # texto = "Algo aquí."
    # resultado = palindromo(texto)
    # print(f"\"{texto}\" es un palíndromo: {resultado}")
    
    texto = "Hola mundo xyz"
    resultado = cifrado_cesar(texto, 3)
    print(f"Texto cifrado: {resultado}")
    original = descifrado_cesar(resultado, 3)
    print(f"Texto descifrado: {original}")
    
    # print(-3 - 27 * int(-3/27))
    # print(-3 - 27 * math.floor(-3/27))