
n = int(input("Ingresa el valor de n: "))

sumatoria = 0
for k in range(n+1):
    # sumatoria = sumatoria + 2*k + 1
    sumatoria += 2*k + 1
print(f"El resultado de la sumatoria es: {sumatoria}")