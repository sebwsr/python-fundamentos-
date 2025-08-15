import pandas as pd

# 1. Cargar los archivos
df_estudiantes = pd.read_csv("respuestas_estudiantes.csv")
df_correctas = pd.read_excel("respuestas_correctas.xlsx", engine='openpyxl')

# 2. Crear diccionario de respuestas correctas
clave_respuestas = dict(zip(df_correctas['Pregunta'], df_correctas['Respuesta']))

# 3. Identificar las columnas de preguntas (P1, P2,...)
preguntas = [col for col in df_estudiantes.columns if col.startswith('P')]

# 4. Calcular puntuación para cada estudiante
df_estudiantes['Puntuación'] = 0
for p in preguntas:
    df_estudiantes['Puntuación'] += (df_estudiantes[p] == clave_respuestas[p]).astype(int)

# 5. Calcular errores por pregunta
errores_por_pregunta = {}
for p in preguntas:
    errores_por_pregunta[p] = (df_estudiantes[p] != clave_respuestas[p]).sum()

# 6. Mostrar resultados
print("=== RESULTADOS ===")
print(df_estudiantes[['Nombre', 'Puntuación']].to_string(index=False))

print("\n=== ERRORES POR PREGUNTA (DETALLE POR ALUMNO) ===")

# Crear un DataFrame que muestre las respuestas incorrectas
df_errores = df_estudiantes.copy()

# Marcar con 'X' las respuestas incorrectas de cada alumno
for p in preguntas:
    df_errores[p] = df_errores[p].where(df_errores[p] == clave_respuestas[p], 'X')

# Mostrar solo alumnos con al menos un error
alumnos_con_errores = df_errores[df_errores[preguntas].eq('X').any(axis=1)]

if not alumnos_con_errores.empty:
    print("Alumnos con respuestas incorrectas (X = error):")
    print(alumnos_con_errores.to_string(index=False))
else:
    print("¡Todos los alumnos respondieron correctamente todas las preguntas!")
# 7. Guardar resultados en CSV
df_estudiantes.to_csv("resultados_examen.csv", index=False)
print("\nResultados guardados en 'resultados_examen.csv'")