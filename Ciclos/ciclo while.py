
# for i in range(inicio, final, paso)

i = 1 # inicio -> contador
while i <= 10: # condición de paro o salida
    print(f"El valor de i es: {i}")
    # i = i + 1
    i += 1 # paso

print("-"*20)

texto = "Hola mundo"
i = 0
while i < len(texto):
    print(f"i: {i} - texto[{i}]: {texto[i]}")
    i += 1
    
print("-"*20)

lista = [1, 2, "Hola", ["True", False], 2945j]
i = 0
while i < len(lista):
    print(f"i: {i} - lista[{i}]: {lista[i]}")
    i += 1

print("-"*20)

# Menú ciclado
opcion = 4
while opcion != 0:
    print("""Menú principal:
1) Calcular área
2) Calcular perímetro
3) Calcular apotema
0) Salir""")
    opcion = int(input("Elige la opción que deseas: "))
