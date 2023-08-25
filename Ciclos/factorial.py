
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# n!

n = int(input("Ingresa el valor de n: "))
m = n
factorial = 1
while n > 1:
    # factorial = factorial * n
    factorial *= n
    # n = n - 1
    n -= 1

print(f"El factorial de {m} es: {factorial}")