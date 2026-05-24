import pandas as pd
import matplotlib.pyplot as plt
# Cargar CSV desde la carpeta datos
datos = pd.read_csv("../datos/datosresistencia.csv")
# Renombrar columnas para que sean más fáciles de usar
datos = datos.rename(columns={
    "time": "fecha",
    "temperature_2m_max (°C)": "temp_max",
    "temperature_2m_min (°C)": "temp_min",
    "precipitation_sum (mm)": "precipitacion"
})
# Convertir la columna de fecha
datos["fecha"] = pd.to_datetime(datos["fecha"])
# Calcular temperatura promedio diaria
datos["temp_promedio"] = (datos["temp_max"] + datos["temp_min"]) / 2
# Indicadores
temp_max_anual = datos["temp_max"].max()
temp_min_anual = datos["temp_min"].min()
promedio_temp_anual = datos["temp_promedio"].mean()
promedio_precipitacion = datos["precipitacion"].mean()
# Mostrar resultados
print("Temperatura máxima del año:", temp_max_anual)
print("Temperatura mínima del año:", temp_min_anual)
print("Temperatura promedio del año:", promedio_temp_anual)
print("Precipitación promedio diaria:", promedio_precipitacion)
# Gráfico
plt.figure(figsize=(12,5))
plt.plot(datos["fecha"], datos["temp_max"], label="Temp Máxima")
plt.plot(datos["fecha"], datos["temp_min"], label="Temp Mínima")
plt.title("Temperaturas diarias - Resistencia 2023")
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
# Guardar gráfico
plt.savefig("../resultados/grafico_temperaturas.png")
# Guardar CSV procesado
datos.to_csv("../resultados/analisis_climatico.csv", index=False)