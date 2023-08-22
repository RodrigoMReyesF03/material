
x = 1000

match (x):
    case 1000:
        print("El valor es 1000")
    case "hola":
        print("Es un string con hola")
    case _:
        print("Todo lo demás...")