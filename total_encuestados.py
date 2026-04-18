import csv

encuestados = []
with open(
    "encuesta_ingenieria_10000_respuestas.csv", mode="r", encoding="utf-8"
) as encuestas:
    resultados = csv.reader(encuestas)
    next(resultados)
    for fila in resultados:
        if fila and fila[0]:
            encuestados.append(fila)

print(f"Total de encuestados: {len(encuestados) }")
