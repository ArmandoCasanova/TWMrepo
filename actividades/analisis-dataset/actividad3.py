import os
import sys
from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

raiz = Path(__file__).resolve().parents[2]
sys.path.append(str(raiz))

from entrenar_arbol import NUMERICAS, CATEGORICAS, OBJETIVO
from usar_modelo import es_posible

ruta = "envios_medios.csv" if os.path.exists("envios_medios.csv") else ("../envios_medios.csv" if os.path.exists("../envios_medios.csv") else "../../envios_medios.csv")
ruta_modelo = "modelo_medios.joblib" if os.path.exists("modelo_medios.joblib") else ("../modelo_medios.joblib" if os.path.exists("../modelo_medios.joblib") else "../../modelo_medios.joblib")

datos = pd.read_csv(ruta)
x = datos[NUMERICAS + CATEGORICAS]
y = datos[OBJETIVO]

x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=42
)

modelo = joblib.load(ruta_modelo)
prediccion = modelo.predict(x_prueba)

tabla = x_prueba.copy()
tabla["real"] = y_prueba
tabla["predicho"] = prediccion

errores = tabla[tabla["real"] != tabla["predicho"]]
print(f"Total de errores: {len(errores)}")

print("\n--- CONFUSIONES MAS FRECUENTES ---")
print(errores.groupby(["real", "predicho"]).size().sort_values(ascending=False))

moto_dron = errores[(errores["real"] == "moto") & (errores["predicho"] == "dron")]
es_noche = (moto_dron["hora_salida"] < 6) | (moto_dron["hora_salida"] >= 21)
corregidos = ~moto_dron.apply(lambda r: es_posible("dron", r), axis=1)

print(f"\nMoto a dron total: {len(moto_dron)}")
print(f"Moto a dron de noche: {es_noche.sum()}")
print(f"Moto a dron descartados por reglas de negocio: {corregidos.sum()}")

moto_bici = errores[(errores["real"] == "moto") & (errores["predicho"] == "bicicleta")]
print(f"\nMoto a bicicleta total: {len(moto_bici)}")
print(f"Distancia maxima moto a bicicleta: {moto_bici['distancia_km'].max()} km")
