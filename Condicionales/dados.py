import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma_dados = dado1 + dado2

eleccion = input("""Debes elegir entre alguna de las opciones:
a) Debajo de 7
b) Igual a 7
c) Arriba de 7
Elige tu opción: """).lower().strip()

print(f"El dado 1 cayó en: {dado1}")
print(f"El dado 2 cayó en: {dado2}")
print(f"La suma de los dados es: {suma_dados}")

if eleccion == "a" and suma_dados < 7:
    print("¡Has adivinado!")
elif eleccion == "b" and suma_dados == 7:
    print("¡Has adivinado!")
elif eleccion == "c" and suma_dados > 7:
    print("¡Has adivinado!")
else:
    print("¡Has perdido!")
