import csv

carreras = []
ingenieros_electricos = 0
ingenieros_sistemas = 0
carreras_objetivo = ["Ingeniería de Sistemas", "Ingeniería Eléctrica"]

with open(
    "encuesta_ingenieria_10000_respuestas.csv", mode="r", encoding="utf-8"
) as estudiantes:
    encuestas = csv.reader(estudiantes)
    next(encuestas)
    for lineas in encuestas:
        carreras.append(lineas[1])
        if lineas[1] == carreras_objetivo[0]:
            ingenieros_sistemas += 1

        if lineas[1] == carreras_objetivo[1]:
            ingenieros_electricos += 1


print(
    f"ingenieros electricos:{ingenieros_electricos} ingenieros de sistemas:{ingenieros_sistemas}"
)
