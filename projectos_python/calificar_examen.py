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

print("\n=== DETALLE COMPLETO DE RESPUESTAS ===")

# Crear copia del DataFrame para marcar errores
df_detalle = df_estudiantes.copy()

# Marcar respuestas incorrectas y mantener las correctas
for p in preguntas:
    df_detalle[p] = df_detalle[p].where(
        df_detalle[p] == clave_respuestas[p], 
        df_detalle[p] + '✗'  # Marca error con símbolo
    )

# Ordenar por puntuación (opcional)
df_detalle = df_detalle.sort_values('Puntuación', ascending=False)

# Mostrar tabla completa
print("Leyenda: Respuesta✗ = Incorrecta")
print(df_detalle.to_string(index=False))
# 7. Guardar resultados en CSV
df_estudiantes.to_csv("resultados_examen.csv", index=False)
print("\nResultados guardados en 'resultados_examen.csv'")