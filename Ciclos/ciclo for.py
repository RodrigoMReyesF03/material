# range(final)
# Secuencia numérica que inicia en 0, avanza de 1 en 1
# y termina antes de final
for i in range(5):
    print(f"El valor de i es: {i}")
    
print("-"*20)

# range(inicio, final)
# Secuencia numérica que inicia en inicio, avanza de 1 en 1
# y llega a antes de final
for i in range(3,8):
    print(f"El valor de i es: {i}")

print("-"*20)

# range(inicio, final, paso)
# Secuencia numérica que inicia en inicio, avanza de
# paso en paso y llega a antes de final
for i in range(3,15,2):
    print(f"El valor de i es: {i}")
    
print("-"*20)

for i in range(10,5,-1):
    print(f"El valor de i es: {i}")
    
print("-"*20)

texto = "Hola mundo"

for i in texto:
    print(f"El valor de i es: {i}")

print("-"*20)

texto = "Hola mundo"
print(texto[5])
print(len(texto))

for i in range(len(texto)):
    print(f"i: {i} - texto[{i}]: {texto[i]}")

print("-"*20)

for k,v in enumerate(texto):
    print(f"k: {k} - v: {v}")
    
print("-"*20)

lista = [1,2,True,["hola","adiós"],5.2]

for i in lista:
    print(f"El valor de i es: {i}")
    
print("-"*20)

lista = [1,2,True,["hola","adiós"],5.2]
    
for i in range(len(lista)):
    print(f"i: {i} - lista[{i}]: {lista[i]}")