
dic = {
    "uno": [1,2],
    2: True,
    (1,2): "Adiós"
}

print(dic)
print(dic["uno"])
print(dic[(1,2)])

print(dic.get("uno"))
print(dic.get("dos")) # None
print(dic.get("dos", "default"))

dic["dos"] = "Un nuevo valor"
print(dic)

for key in dic:
    print(f"Llave: {key} - Valor: {dic[key]}")
    
dic.pop("uno")

print(dic)

alumno = {
    "nombre": {
        "nombre": "Adrían",
        "apellido paterno": "Sosa",
        "apellido materno": "Martínez"
    },
    "dirección": {
        "calle": "Av. Lago de Guadalupe",
        "número": "S/N",
        "colonia": "Jardines de Atizapán",
        "municipio": "Atizapán de Zaragoza"
    }
}

print(alumno["nombre"]["apellido paterno"])