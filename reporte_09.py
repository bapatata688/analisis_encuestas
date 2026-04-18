def procesar_datos_encuesta():
    encuestas = []
    try:
        with open("encuesta_ingenieria_10000_respuestas.csv", 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            for linea in lineas[1:]:
                datos = linea.strip().split(',')
                if len(datos) == 26:
                    generales = [datos[1], int(datos[2]), datos[3], int(datos[5])]
                    academicas = [int(x) for x in datos[6:15] + datos[16:20]]
                    tecnologicas = [int(datos[15])] # q10_calidad_internet
                    economicas = [datos[4]]
                    percepcion = [int(x) for x in datos[20:26]]
                    encuestado = [int(datos[0]), generales, academicas, tecnologicas, economicas, percepcion]
                    encuestas.append(encuestado)
    except FileNotFoundError:
        print("Error: No se encontró 'encuesta_ingenieria_10000_respuestas.csv' en la carpeta.")
    return encuestas

def generar_reporte_09():
    datos = procesar_datos_encuesta()
    if not datos: return
    
    conteos_internet = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
    
    for encuestado in datos:
        nivel_internet = encuestado[3][0]
        for i in range(len(conteos_internet)):
            if conteos_internet[i][0] == nivel_internet:
                conteos_internet[i][1] += 1
                break
                
    print("--- Reporte 9: Acceso y calidad de internet en casa (q10) ---")
    print("Nivel (1=Bajo/Nulo, 5=Excelente) | Cantidad de Estudiantes")
    print("-" * 55)
    for item in conteos_internet:
        print(f" Nivel {item[0]} {' ' * 28} | {item[1]}")

if __name__ == "__main__":
    generar_reporte_09()