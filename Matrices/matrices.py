
matriz = [[1,2,3],
          [4,5,6]]

print(matriz)

print(matriz[1])

print(matriz[1][0])

matriz[1][0] += 1

print(matriz)

# Recorrido por fila
for fila in range(len(matriz)):
    for col in range(len(matriz[0])):
        print(f"matriz[{fila}][{col}] = {matriz[fila][col]}")
        
print("-"*30)

# Recorrido por columna
for col in range(len(matriz[0])):
    for fila in range(len(matriz)):
        print(f"matriz[{fila}][{col}] = {matriz[fila][col]}")
