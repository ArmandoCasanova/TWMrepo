import os
import pandas as pd

ruta = "envios_medios.csv" if os.path.exists("envios_medios.csv") else ("../envios_medios.csv" if os.path.exists("../envios_medios.csv") else "../../envios_medios.csv")
datos = pd.read_csv(ruta)

print("--- CLIMA VS MEDIO ---")
print(pd.crosstab(datos["clima"], datos["medio_recomendado"], normalize="index") * 100)

print("\n--- ZONA VS MEDIO ---")
print(pd.crosstab(datos["zona_destino"], datos["medio_recomendado"], normalize="index") * 100)

print("\n--- LIMITES FISICOS (MIN, MEDIAN, MAX) ---")
print(datos.groupby("medio_recomendado")[["distancia_km", "peso_kg", "volumen_l"]].agg(["min", "median", "max"]))

camionetas_cortas = datos[(datos["medio_recomendado"] == "camioneta") & (datos["distancia_km"] < 2)]
print(f"\nCamionetas en < 2km: {len(camionetas_cortas)}")
