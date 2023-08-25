import random

ganados = 0
perdidos = 0

while (opcion := int(input("""Menú:
1)Jugar 
2)Salir
Elige tu opción: """))) != 2:
    moneda = random.randint(1,2)
    
    while (eleccion := int(input("Elige 1)Águila 2)Sol: "))) not in [1,2]:
        print("Error. Debes elegir 1 o 2.")
    
    print(f"La moneda cayó en: {['Aguila', 'Sól'][moneda-1]}")
    if moneda == eleccion:
        print("Atinaste.")
        ganados += 1
    else:
        print("Fallaste.")
        perdidos += 1
jugados = ganados + perdidos
print(f"""Jugaste {jugados} veces.
Atinaste {ganados} veces.
Perdiste {perdidos} veces.""")