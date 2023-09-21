
lista = []

lista = ["Hola", 124, True]

lista = [1,2] + [3,4] #[1,2,3,4]
print(lista)

lista = [1,2] * 3
print(lista)
lista[3] = 5
print(lista)

lista = [1,2,4,6,2,4,6]
print(lista[::2])

lista = [1,2,3,4]
# append(elemento)
lista.append(5)
print(lista)

# insert(índice, elemento)
lista.insert(3,"Hola")
print(lista)

lista.insert(90,"Adiós")
print(lista)

lista.insert(-90,"Otra más")
print(lista)

lista = [1,2,5,2,1,3,1,4]

# pop(índice) -> valor por default de índice es -1
elemento = lista.pop()
print(f"Elemento: {elemento}")
print(f"Lista: {lista}")

elemento = lista.pop(4)
print(f"Elemento: {elemento}")
print(f"Lista: {lista}")

# remove(elemento) elimina la primera ocurrencia del elemento
lista.remove(2)
print(lista)

if "hola" in lista:
    lista.remove("hola")
    print(lista)

lista = ["hola", 1, 5.2, True, "hola", False]

print(lista.index("hola"))

print(lista.count("hola"))

lista = [1,6,4,6,4,2,5,2,1]
lista.reverse()
print(lista)

lista.sort() # ordena de manera ascendente
print(lista)

lista.sort(reverse=True) # ordena de manera descendente
print(lista)

print(sorted(lista, reverse=True)) # crea una nueva lista ordenada

lista = ["maría", "rodolfo", "arturo", "josé"]
lista.sort()
print(lista)

lista = ["maría", "Rodolfo", "arturo", "José"]
lista.sort()
print(lista)

# internamente usa < 
# lista = [1,2,"hola"] 
# lista.sort()
# print(lista)

a = 10
b = a
a = 15
print(f"a: {a} - b: {b}")

a = [1,2]
b = a
a.append(3)
print(f"a: {a} - b: {b}")

a = [1,2]
b = a.copy()
a.append(3)
print(f"a: {a} - b: {b}")

# parámetros por valor -> int, float, strings
# parámetros por referencia -> list
def funcion(lista : list):
    lista.append("a")
    
def funcion2(lista : list):
    lista = lista.copy()
    lista.append("a")

a = [1,2]
funcion(a)
print(a)
funcion2(a)
print(a)