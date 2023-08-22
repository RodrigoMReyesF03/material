edad = int(input("Escribe tu edad: "))

if edad < 3:
    print("Aún no tienes edad para estudiar.")
else:
    if edad <= 5:
        print("Kinder")
    else:
        if edad <= 11:
            print("Primaria")
        else:
            if edad <= 14:
                print("Secundaria")
            else:
                if edad <= 17:
                    print("Preparatoria")
                else:
                    if edad <= 22:
                        print("Profesional")
                    else:
                        print("Posgrado")
                        
if edad < 3:
    print("Aún no tienes edad para estudiar.")
elif edad <= 5:
    print("Kinder")
elif edad <= 11:
    print("Primaria")
elif edad <= 14:
    print("Secundaria")
elif edad <= 17:
    print("Preparatoria")
elif edad <= 22:
    print("Profesional")
else:
    print("Posgrado")