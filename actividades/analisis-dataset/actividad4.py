import os
import sys
from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

raiz = Path(__file__).resolve().parents[2]
sys.path.append(str(raiz))

from entrenar_arbol import NUMERICAS, CATEGORICAS, OBJETIVO

ruta = "envios_medios.csv" if os.path.exists("envios_medios.csv") else ("../envios_medios.csv" if os.path.exists("../envios_medios.csv") else "../../envios_medios.csv")
ruta_modelo = "modelo_medios.joblib" if os.path.exists("modelo_medios.joblib") else ("../modelo_medios.joblib" if os.path.exists("../modelo_medios.joblib") else "../../modelo_medios.joblib")

datos = pd.read_csv(ruta)
x = datos[NUMERICAS + CATEGORICAS]
y = datos[OBJETIVO]

x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=42
)

modelo = joblib.load(ruta_modelo)
nombres = list(modelo.named_steps["preparacion"].get_feature_names_out())
importancias = modelo.named_steps["arbol"].feature_importances_

df_imp = pd.DataFrame({"caracteristica": nombres, "importancia": importancias}).sort_values("importancia", ascending=False)
print("--- TOP 5 CARACTERISTICAS MAS IMPORTANTES ---")
print(df_imp.head(5))

base_acc = (modelo.predict(x_prueba) == y_prueba).mean()
print(f"\nExactitud original con todas las columnas: {base_acc:.4f}")

for col in ["distancia_km", "volumen_l", "refrigerado", "peso_kg", "zona_destino"]:
    num = [c for c in NUMERICAS if c != col]
    cat = [c for c in CATEGORICAS if c != col]
    prep = ColumnTransformer([
        ("numericas", "passthrough", num),
        ("categoricas", OneHotEncoder(handle_unknown="ignore"), cat),
    ])
    mod = Pipeline([
        ("preparacion", prep),
        ("arbol", DecisionTreeClassifier(max_depth=8, min_samples_leaf=5, random_state=42)),
    ])
    mod.fit(x_entreno[num + cat], y_entreno)
    acc = (mod.predict(x_prueba[num + cat]) == y_prueba).mean()
    print(f"Exactitud sin {col:<15}: {acc:.4f} (cambio: {acc - base_acc:+.4f})")
