
def mi_primera_funcion():
    print("Hola")
    print("Ésta es mi primera función.")

# print(mi_primera_funcion())

# parámetros -> entradas
# valor de retorno -> salida

# sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingrese el valor de x: "))
    y = float(input("Ingrese el valor de y: "))
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")

# suma1()
# print(f"{x}")
# print(f"{y}")
# print(f"{resultado}")

# Con parámetros y sin valor de retorno
def suma2(x : float, y : float):
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")

# suma2(5, 9)
# a = float(input("Introduce x: "))
# b = float(input("Introduce y: "))
# suma2(a, b)
# suma2("hola", "mundo")

# Con parámetros y valor de retorno
def suma3(x : float, y : float) -> tuple:
    resultado = x + y
    return x,y,resultado
    
# res = suma3(6,2)
# print(f"Resultado: {res}")
# a, b, c = suma3(7,5)
# print(f"a: {a}")
# print(f"b: {b}")
# print(f"c: {c}")

def funcion(a : float = 5, b : float = 4, c : float = 3, d : float = 2) -> float:
    return a + b * c / d

res = funcion(1,2,3,4)
print(f"Resultado: {res}")

res = funcion(1,2,3)
print(f"Resultado: {res}")

res = funcion(d = 10)
print(f"Resultado: {res}")

res = funcion()
print(f"Resultado: {res}")

res = funcion(1,d=7)
print(f"Resultado: {res}")

res = funcion(d=7, a=5, c=12, b=5)
print(f"Resultado: {res}")

