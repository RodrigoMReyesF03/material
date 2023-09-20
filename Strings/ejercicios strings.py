
def quita_vocales(texto : str) -> str:
    vocales = "aeiouáéíóú"
    for i in vocales:
        texto = texto.replace(i, "").replace(i.upper(), "")
    return texto

if __name__ == "__main__":
    texto = "Hola Árbol Algo"
    resultado = quita_vocales(texto)
    print(f"El resultado es: {resultado}")