import os
os.environ["MODIN_ENGINE"] = "ray"
import ray
ray.init()

import modin.pandas as pd


# Ruta al archivo JSON
file_path = "../../data/raw/Gift_Cards.jsonl"

# Cargar el archivo JSON línea por línea
df = pd.read_json(file_path, lines=True)

print(df.head())


# Exportar a csv
# df.to_csv("gift_cards.csv", index = False)