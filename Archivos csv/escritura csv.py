import csv

def leer_csv(nombre_archivo : str) -> list:
    alumnos = []
    with open(nombre_archivo, "r", encoding="utf8") as archivo:
        lector = csv.reader(archivo)
        for linea in lector:
            if linea[2] != "calificación":
                linea[2] = float(linea[2])
                alumnos.append(linea)
    return alumnos

def cambiar_calificacion(alumnos : list, alumno : str, calificacion : float) -> None:
    for i in alumnos:
        if i[0] == alumno:
            i[2] = calificacion
            
def guardar_archivo(alumnos : list, nombre_archivo : str) -> None:
    with open(nombre_archivo, "w", newline="", encoding="utf8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows([["nombre","matrícula","calificación"]] + alumnos)
        
if __name__ == "__main__":
    alumnos = leer_csv("alumnos.csv")
    print(alumnos)
    cambiar_calificacion(alumnos, "Juanito", 80)
    print(alumnos)
    guardar_archivo(alumnos, "prueba.csv")