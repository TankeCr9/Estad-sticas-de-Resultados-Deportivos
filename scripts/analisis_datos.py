
import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos con ruta relativa
df = pd.read_csv('datos/resultados_partidos.csv')

# Cálculos estadísticos (goles totales, promedios)
df['goles_totales'] = df['goles_local'] + df['goles_visitante']
promedio_goles = df['goles_totales'].mean()

# Guardar un reporte de texto en /resultados
with open('resultados/reporte.txt', 'w') as f:
    f.write(f"Promedio de goles por partido: {promedio_goles}\n")

# Generar y guardar gráfico comparativo
plt.figure(figsize=(6,4))
plt.bar(['Goles Local', 'Goles Visitante'], [df['goles_local'].sum(), df['goles_visitante'].sum()], color=['blue', 'red'])
plt.title('Total de Goles del Torneo')
plt.savefig('resultados/grafico_rendimiento.png')
print("Análisis ejecutado con éxito.")
