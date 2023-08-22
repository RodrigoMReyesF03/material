
numero = int(input("Ingrese el valor a revisar: "))
for i in range(2,numero):
    if numero % i == 0:
        print("No es un número primo.")
        break
else: # Se ejecuta si el ciclo no se rompió
    print("Es número primo.")