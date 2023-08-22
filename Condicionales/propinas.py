
cuenta = float(input("Ingresa el total de la cuenta: "))
personas = int(input("Ingresa el número de personas: "))

por_persona = cuenta / personas

if por_persona < 150:
    porcentaje = 10
elif por_persona <= 250:
    porcentaje = 13
else:
    porcentaje = 15
propina = por_persona * (1 + porcentaje / 100)
print(f"Te toca pagar ${propina:,.2f} con un {porcentaje}% de propina incluido.")