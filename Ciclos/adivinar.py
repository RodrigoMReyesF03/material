import random

numero = random.randint(1, 100)

num = 0
intentos = 0

while num != numero:
    num = int(input("Introduce tu número: "))
    if num > 100 or num < 1:
        print("El número debe estar entre 1 y 100.")
    elif num > numero:
        print(f"El número es menor a: {num}")
    elif num < numero:
        print(f"El número es mayor a: {num}")
    intentos += 1

print(f"Has adivinado el número.")
print(f"Te tomó {intentos} intentos.")
    
        