# Sistema de Análisis de Encuesta de Ingeniería

Análisis exploratorio de datos sobre 10,000 estudiantes de ingeniería, organizado en 20 reportes individuales y un reporte general consolidado.

---

## Estructura del repositorio

```
sistema_encuestas/
├── encuesta_ingenieria_10000_respuestas.csv   # Dataset principal
├── diccionario_variables_encuesta.csv         # Descripción de cada columna
├── preguntas_encuesta.csv                     # Preguntas originales del instrumento
├── reporte_general.ipynb                      # Consolidado de los 5 primeros reportes
├── reporte_1.ipynb
├── reporte_2.ipynb
├── reporte_3.ipynb
├── reporte_4.ipynb
└── reporte_5.ipynb
```

---

## Reportes

| #   | Descripción                                                        | Estado     |
| --- | ------------------------------------------------------------------ | ---------- |
| 1   | Total de encuestados                                               | Completado |
| 2   | Cantidad de estudiantes por carrera                                | Completado |
| 3   | Cantidad de estudiantes por semestre                               | Completado |
| 4   | Cantidad de estudiantes por jornada                                | Completado |
| 5   | Porcentaje de estudiantes que trabajan y que no trabajan           | Completado |
| 6   | Promedio general del promedio académico reportado                  | Pendiente  |
| 7   | Promedio académico por carrera                                     | Pendiente  |
| 8   | Promedio académico por semestre                                    | Pendiente  |
| 9   | Cantidad de estudiantes con acceso a internet en casa              | Pendiente  |
| 10  | Cantidad de estudiantes con computadora propia                     | Pendiente  |
| 11  | Cantidad de estudiantes según horas de estudio semanal             | Pendiente  |
| 12  | Nivel de satisfacción general con la carrera                       | Pendiente  |
| 13  | Nivel de estrés académico general                                  | Pendiente  |
| 14  | Curso percibido como más difícil                                   | Pendiente  |
| 15  | Carrera con mayor nivel promedio de estrés                         | Pendiente  |
| 16  | Relación entre trabajar y promedio académico                       | Pendiente  |
| 17  | Relación entre acceso a internet y promedio académico              | Pendiente  |
| 18  | Relación entre horas de estudio y rendimiento académico            | Pendiente  |
| 19  | Porcentaje de estudiantes interesados en cursos virtuales          | Pendiente  |
| 20  | Perfil predominante del encuestado según respuestas más frecuentes | Pendiente  |

---

## Requisitos

- Python 3.10 o superior
- Jupyter Notebook o JupyterLab
- Librería estándar `csv` (incluida en Python)

Para los reportes interactivos:

```bash
pip install pandas ipywidgets
```

---

## Uso

1. Clonar el repositorio y ubicarse en la carpeta del proyecto.
2. Asegurarse de que el archivo `encuesta_ingenieria_10000_respuestas.csv` esté en la raíz.
3. Abrir cualquier notebook con Jupyter y ejecutar las celdas en orden.

```bash
jupyter notebook reporte_general.ipynb
```

---

## Dataset

El archivo `encuesta_ingenieria_10000_respuestas.csv` contiene 10,000 registros de estudiantes de las carreras de Ingeniería Eléctrica, Ingeniería de Sistemas e Ingeniería Electrónica. La descripción completa de cada columna se encuentra en `diccionario_variables_encuesta.csv`.
