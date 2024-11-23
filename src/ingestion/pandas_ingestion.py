import pandas as pd


# Ruta al archivo JSON
file_path = "../../data/raw/meta_Gift_Cards.jsonl"

# Cargar el archivo JSON línea por línea
df = pd.read_json(file_path, lines=True)

# Mostrar los primeros registros como tabla
print(df.head())

print(df.count())
# Exportar a csv
# df.to_csv("gift_cards.csv", index = False)