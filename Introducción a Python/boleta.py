udf1 = float(input("Proporciona la calificación de tu udf1: "))
udf2 = float(input("Proporciona la calificación de tu udf2: "))
udf3 = float(input("Proporciona la calificación de tu udf3: "))
udf4 = float(input("Proporciona la calificación de tu udf4: "))
udf5 = float(input("Proporciona la calificación de tu udf5: "))
udf6 = float(input("Proporciona la calificación de tu udf6: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6) / 6

# print se encarga de juntar el contenido y usa sep para separarlos y end para terminar la línea
print("El promedio de este semestre fue:", promedio, "Estudia más.")
# print("El promedio de este semestre fue:", promedio, "Estudia más.", sep="---+---", end="qwerty")
# print("hola")

# Creamos el string concatenando otros strings y lo mandamos a print
print("El promedio de este semestre fue: " + str(promedio) + " Estudia más.")

# La función de format para crear un string
print("El promedio de este semestre fue: {0} Estudia más.".format(promedio))

# valor = 43748852.5888284
# print("El valor es: {0:,.2f}".format(valor))

# f-strings -> Forma moderna de dar formato a strings
print(f"El promedio de este semestre fue: {promedio} Estudia más.")

# valor = 43748852.5888284
# print(f"El valor es: {valor:,.2f}")