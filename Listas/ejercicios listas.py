
def k_elementos(lista : list, numero : int) -> list:
    return lista[::numero]

def n_menores(lista : list, numero : int) -> list:
    return sorted(lista)[:numero]

def eliminar_ocurrencias(lista : list, elemento : int) -> list:
    # lista = lista.copy()
    # # for i in range(lista.count(elemento)):
    # while elemento in lista:
    #     lista.remove(elemento)
    # return lista
    
    res = []
    for i in lista:
        if i != elemento:
            res.append(i)
    return res

def eliminar_duplicados(lista : list):
    res = []
    for i in lista:
        if i not in res:
            res.append(i)
    return res

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9]
    numero = 3
    resultado = k_elementos(lista, numero)
    print(f"Resultado: {resultado}")
    
    lista = [1,6,8,3,1,2]
    numero = 3
    resultado = n_menores(lista, numero)
    print(f"Resultado: {resultado}")
    
    lista = [1,6,8,3,1,2]
    numero = 1
    resultado = eliminar_ocurrencias(lista, numero)
    print(f"Resultado: {resultado}")
    
    lista = [1,5,7,3,7,9,2,1,1,2,5,7,9]
    resultado = eliminar_duplicados(lista)
    print(f"Resultado: {resultado}")
