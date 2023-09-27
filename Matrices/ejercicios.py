import random
def crear_matriz_aleatoria(filas : int, columnas : int) -> list:
    # matriz = []
    # for fila in range(filas):
    #     row = []
    #     for col in range(columnas):
    #         row.append(random.randint(0,100))
    #     matriz.append(row)
    # return matriz
    return [[random.randint(0,100) for col in range(columnas)] for fila in range(filas)]

def crear_matriz_ceros(filas : int, columnas : int) -> list:
    return [[0 for col in range(columnas)] for fila in range(filas)]

def imprimir_matriz(matriz : list) -> None:
    for fila in matriz:
        print(fila)

def dimensiones_matriz(matriz : list) -> tuple:
    return len(matriz), len(matriz[0])

def comparacion_matrices(matriz1 : list, matriz2 : list) -> bool:
    return dimensiones_matriz(matriz1) == dimensiones_matriz(matriz2)

def suma_por_filas(matriz : list) -> list:
    res = []
    for col in range(len(matriz[0])):
        suma = 0
        for fila in range(len(matriz)):
            suma += matriz[fila][col]
        res.append(suma)
    return res

def suma_por_columnas(matriz : list) -> list:
    res = []
    for fila in range(len(matriz)):
        suma = 0
        for col in range(len(matriz[0])):
            suma += matriz[fila][col]
        res.append(suma)
    return res

def suma_matrices(matriz1 : list, matriz2 : list) -> list:
    if not comparacion_matrices(matriz1, matriz2):
        return None
    filas, columnas = dimensiones_matriz(matriz1)
    matriz = crear_matriz_ceros(filas, columnas)
    for fila in range(filas):
        for col in range(columnas):
            matriz[fila][col] = matriz1[fila][col] + matriz2[fila][col]
    return matriz

def resta_matrices(matriz1 : list, matriz2 : list) -> list:
    if not comparacion_matrices(matriz1, matriz2):
        return None
    filas, columnas = dimensiones_matriz(matriz1)
    matriz = crear_matriz_ceros(filas, columnas)
    for fila in range(filas):
        for col in range(columnas):
            matriz[fila][col] = matriz1[fila][col] - matriz2[fila][col]
    return matriz

def division_matrices(matriz1 : list, matriz2 : list) -> list:
    if not comparacion_matrices(matriz1, matriz2):
        return None
    filas, columnas = dimensiones_matriz(matriz1)
    matriz = crear_matriz_ceros(filas, columnas)
    for fila in range(filas):
        for col in range(columnas):
            matriz[fila][col] = matriz1[fila][col] / matriz2[fila][col]
    return matriz

def multiplicacion_estandar(matriz1 : list, matriz2 : list) -> list:
    filas1, columnas1 = dimensiones_matriz(matriz1)
    filas2, columnas2 = dimensiones_matriz(matriz2)
    if columnas1 != filas2:
        return None
    matriz = crear_matriz_ceros(filas1, columnas2)
    # Les queda de tarea

if __name__ == "__main__":
    matriz = crear_matriz_aleatoria(3,2)
    print(matriz)
    
    matriz = [[0] * 2] * 3
    print(matriz)
    matriz[0][0] = 1
    print(matriz)
    
    matriz = crear_matriz_ceros(3,2)
    print(matriz)
    matriz[0][0] = 1
    print(matriz)
    
    imprimir_matriz(matriz)
    
    matriz = [[1,2,3],[4,5,6]]
    print(suma_por_filas(matriz))
    print(suma_por_columnas(matriz))
    
    m1 = [[1,2,3],[4,5,6]]
    m2 = [[6,4,2],[6,3,2]]
    matriz = suma_matrices(m1, m2)
    imprimir_matriz(matriz)