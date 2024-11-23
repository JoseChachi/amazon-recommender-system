import dask.dataframe as dd


# Ruta al archivo JSON
file_path = "../../data/raw/Gift_Cards.jsonl"

# Cargar el archivo JSON línea por línea
df = dd.read_json(file_path, lines=True)

# Mostrar los primeros registros como tabla
print(df.head())


# Exportar a csv
# df.to_csv("gift_cards.csv", index = False)