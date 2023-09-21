
def k_elementos(lista : list, numero : int) -> list:
    return lista[::numero]

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9]
    numero = 3
    resultado = k_elementos(lista, numero)
    print(f"Resultado: {resultado}")