from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Read JSONL File") \
    .getOrCreate()

# File path to your JSONL file
file_path = "../../data/raw/Gift_Cards.jsonl"

# Read the JSONL file
df = spark.read.json(file_path, multiLine=False)

# Show the first few rows of the DataFrame
df.show(truncate=False)

# Print the schema to verify the structure
df.printSchema()


# df.show()

# Filtrar los verificados
verified_df = df.filter(df.verified_purchase == True)
verified_df.show()

# Seleccionar algunas columnas
selected_df = df.select("rating", "title", "text", "helpful_vote")
selected_df.show()
