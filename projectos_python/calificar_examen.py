import pandas as pd

# 1. Cargar los archivos
df_estudiantes = pd.read_csv("./archivos/respuestas_estudiantes.csv")
df_correctas = pd.read_excel("./archivos/respuestas_correctas.xlsx")

# 2. Obtener las preguntas usando métodos permitidos
preguntas = df_correctas['Pregunta'].values  # Usando .values

# 3. Crear diccionario de respuestas correctas
clave_respuestas = {}
for i in range(df_correctas.shape[0]):
    clave_respuestas[df_correctas['Pregunta'].iloc[i]] = df_correctas['Respuesta'].iloc[i]

# 4. Calcular puntuación para cada estudiante
df_estudiantes['Puntuación'] = 0
for p in preguntas:
    respuesta_correcta = clave_respuestas[p]
    df_estudiantes['Puntuación'] = df_estudiantes['Puntuación'].add(
        (df_estudiantes[p] == respuesta_correcta).astype(int))

# 5. Mostrar detalle completo de respuestas
print("\n=== DETALLE COMPLETO DE RESPUESTAS ===")
df_detalle = df_estudiantes.copy()

for p in preguntas:
    df_detalle[p] = df_detalle[p].where(
        df_detalle[p] == clave_respuestas[p], 
        df_detalle[p] + '✗'  # Marca error con símbolo
    )

df_detalle = df_detalle.sort_values('Puntuación', ascending=False)
print("Leyenda: Respuesta✗ = Incorrecta")
print(df_detalle.to_string(index=False))

# 6. Mostrar resultados resumidos
print("\n=== RESULTADOS DE LOS ESTUDIANTES ===")
print(df_estudiantes[['Nombre', 'Puntuación']].sort_values('Puntuación', ascending=False).to_string(index=False))
""" 7. Calcular errores por pregunta
print("\n=== ERRORES POR PREGUNTA ===")
for p in preguntas:
    errores = (df_detalle[p].str.contains('✗')).sum()
    print(f"{p}: {errores} errores")
    """


# 8. Mostrar estadísticas generales
print("\n=== ESTADÍSTICAS ===")
print("Total estudiantes:", df_estudiantes.shape[0])
print("Puntuación máxima:", df_estudiantes['Puntuación'].max())
print("Puntuación mínima:", df_estudiantes['Puntuación'].min())
print("Puntuación promedio:", round(df_estudiantes['Puntuación'].mean(), 2))

# 9. Guardar resultados
df_estudiantes.to_csv("resultados_examen.csv", index=False)
print("\nResultados guardados en 'resultados_examen.csv'")