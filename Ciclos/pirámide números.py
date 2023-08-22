
num = int(input("Ingresa el número de niveles: "))

for i in range(1,num+1):
    linea = ""
    for j in range(1, i+1):
        linea = f"{linea}{j}"
    print(linea)