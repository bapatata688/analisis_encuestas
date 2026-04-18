import csv

# crear la lista donde se guardaran los encuestados
encuestados = []
# abrir la encuesta
with open(
    "../encuesta_ingenieria_10000_respuestas.csv", mode="r", encoding="utf-8"
) as encuestas:
    # crear la variable que leera la encuesta
    resultados = csv.reader(encuestas)
    # salto de la primera linea del csv
    next(resultados)
    # bucle que itera sobre las filas del csv, y sin son la primera fila, la agregan alista
    for fila in resultados:
        if fila and fila[0]:
            encuestados.append(fila)

# imprimir el total de encuestados
print(f"Total de encuestados: {len(encuestados) }")
