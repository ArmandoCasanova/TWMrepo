import os
import sys
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

raiz = Path(__file__).resolve().parents[2]
sys.path.append(str(raiz))

from entrenar_arbol import NUMERICAS, CATEGORICAS, OBJETIVO
from usar_modelo import es_posible

ruta = "envios_medios.csv" if os.path.exists("envios_medios.csv") else ("../envios_medios.csv" if os.path.exists("../envios_medios.csv") else "../../envios_medios.csv")
datos = pd.read_csv(ruta)

x = datos[NUMERICAS + CATEGORICAS]
y = datos[OBJETIVO]

x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=42
)

def evaluar(x_tr, y_tr, class_weight=None, nombre=""):
    prep = ColumnTransformer([
        ("numericas", "passthrough", NUMERICAS),
        ("categoricas", OneHotEncoder(handle_unknown="ignore"), CATEGORICAS),
    ])
    arbol = DecisionTreeClassifier(max_depth=8, min_samples_leaf=5, random_state=42, class_weight=class_weight)
    mod = Pipeline([("preparacion", prep), ("arbol", arbol)])
    mod.fit(x_tr, y_tr)
    pred = mod.predict(x_prueba)
    acc = accuracy_score(y_prueba, pred)
    rep = classification_report(y_prueba, pred, output_dict=True, zero_division=0)
    prec_dron = rep["dron"]["precision"]
    rec_dron = rep["dron"]["recall"]
    n_dron_pred = int((pred == "dron").sum())
    
    df_eval = x_prueba.copy()
    df_eval["pred"] = pred
    imposibles = int((~df_eval.apply(lambda r: es_posible(r["pred"], r), axis=1)).sum())
    print(f"{nombre:<25} | {len(x_tr):>6} | {acc:.2f} | {prec_dron:.2f} | {rec_dron:.2f} | {n_dron_pred:>4} | {imposibles:>2}")

print("Estrategia                | Envios | Acc  | Prec | Rec  | Pred | Imposibles")
evaluar(x_entreno, y_entreno, None, "Sin balancear")
evaluar(x_entreno, y_entreno, "balanced", "Con balanceo (pesos)")

drones = y_entreno[y_entreno == "dron"].index
x_over = pd.concat([x_entreno, x_entreno.loc[drones], x_entreno.loc[drones], x_entreno.loc[drones]])
y_over = pd.concat([y_entreno, y_entreno.loc[drones], y_entreno.loc[drones], y_entreno.loc[drones]])
evaluar(x_over, y_over, None, "Oversampling (repetir)")
