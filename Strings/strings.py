
texto = ""

texto = "Hola mundo"

texto = 'Hola "mundo"'

texto = "Hola" * 5 #HolaHolaHolaHolaHola

texto = """Hola
mundo"""

texto = "Hola" +  "mundo"

texto = f"Hola {5}"

texto = "Hola mundo, ¿cómo estás?"
print(texto)
print(f"texto[5] = {texto[5]}")
print(f"texto[-19] = {texto[-19]}")
# Slicing
print(texto[5:10]) # [inicio:final]
print(texto[6:20:3]) # [inicio:final:paso]
print(texto[:10]) # [:final]
print(texto[10:]) # [inicio:]
print(texto[:])
print(texto[-10:2:-1])
print(texto[::-1])

# Secuencias de escape

print("Hola\nmundo") # salto de línea
print("Hola\tmundo") # tabulador
print("Hola\"mundo\"") # comilla doble
print("Hola\'mundo\'") # comilla sencilla 
print("Hola\\mundo") # diagonal invertida

# Funciones de strings
texto = "Hola mundo, ¿cómo estás?"
print(texto.upper()) # Mayúsculas
print(texto.lower()) # Minúsculas
print(texto.title()) # Formato de título

print(texto.replace("o", "0"))
print(texto.replace("mundo", "planeta"))
print(texto.replace("Hola", ""))

print(texto.replace("o", "0").replace("a","9"))

texto = " \n   hola   mundo   \t"

print(texto.lstrip()) # Quita espacios a la izquierda
print(texto.rstrip()) # Quita espacios a la derecha
print(texto.strip()) # Quita espacios a la izquierda y derecha

texto = "Hola mundo, ¿cómo estás?"

print(list(texto))
print(texto.split())
print(texto.split("o"))
print(texto.split("mundo"))

lista = ["Hola", "mundo", "otra", "cosa"]
print(", ".join(lista))

texto = "Hola mundO, ¿cómo estás?"

print(texto.count("o")) 

print(texto.index("mundO"))
print(texto.find("mundO"))

# print(texto.index("adiós"))
print(texto.find("adiós"))

texto = "Árbol"

print(texto.isalpha()) # alfabeto
print(texto.isdigit()) # números
print(texto.isalnum()) # alfanuméricos alfabeto + números

print(texto.startswith("Hola"))
print(texto.endswith("mundo"))

print(ord("a"))
print(chr(97))

