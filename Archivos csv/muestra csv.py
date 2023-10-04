import csv

with open("alumnos.csv", "r", encoding="utf8") as archivo:
    lector = csv.DictReader(archivo)
    promedio = 0
    for fila, linea in enumerate(lector):
        promedio += float(linea["calificación"])
    promedio /= fila + 1
    print(promedio)

# with open("alumnos.csv", "r", encoding="utf8") as archivo:
#     lector = csv.reader(archivo)
#     promedio = 0
#     for fila, linea in enumerate(lector):
#         if fila != 0:
#             promedio += float(linea[2])
#     promedio /= fila
#     print(promedio)

# with open("alumnos.csv", "r", encoding="utf8") as archivo:
    # promedio = 0
    # fila = 0
    # for linea in archivo:
    #     lista = linea.strip().split(",")
    #     if fila != 0:
    #         promedio += float(lista[2])
    #     fila += 1
    # promedio /= fila - 1 
    # print(promedio)