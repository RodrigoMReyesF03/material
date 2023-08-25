
total = 0
while (precio := float(input("Ingresa el precio del artículo: "))) >= 0:
    total += precio
    
print(f"El total a pagar es: ${total:,.2f}")