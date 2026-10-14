import os
import pandas as pd

ruta = "envios_medios.csv" if os.path.exists("envios_medios.csv") else ("../envios_medios.csv" if os.path.exists("../envios_medios.csv") else "../../envios_medios.csv")
datos = pd.read_csv(ruta)

tabla_hora = pd.crosstab(datos["hora_salida"], datos["medio_recomendado"])
print("--- HORA VS MEDIO RECOMENDADO ---")
print(tabla_hora)

noche = (datos["hora_salida"] < 6) | (datos["hora_salida"] >= 21)
print(f"\nEnvios de noche: {noche.sum()} ({noche.mean():.2%})")
print(f"Envios de dia: {(~noche).sum()} ({(~noche).mean():.2%})")

print("\n--- CAMBIO BICICLETAS Y MOTOS EN LA NOCHE ---")
print(tabla_hora.loc[[19, 20, 21, 22], ["bicicleta", "moto"]])
