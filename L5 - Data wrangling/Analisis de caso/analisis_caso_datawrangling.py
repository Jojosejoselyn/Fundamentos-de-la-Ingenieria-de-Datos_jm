# ---------------------------------------
# Análisis de Caso - Data Wrangling con Pandas
# Dataset: Credit Card Default (Taiwán)
# ---------------------------------------

import pandas as pd

# 1. Cargar dataset
df = pd.read_csv("datos.csv")

print("Dimensiones:", df.shape)
print("Primeras filas:\n", df.head(), "\n")

# 2. Exploración inicial
print("Información general:")
print(df.info())
print("\nEstadísticas descriptivas:\n", df.describe())

# 3. Identificación de valores inusuales
print("\nValores únicos en EDUCATION:", df["EDUCATION"].unique())
print("Valores únicos en MARRIAGE:", df["MARRIAGE"].unique())

# 4. Limpieza y transformación
# Corregir categorías inválidas en EDUCATION y MARRIAGE
df["EDUCATION"] = df["EDUCATION"].replace([0, 5, 6], 4)  # 4 = otros
df["MARRIAGE"] = df["MARRIAGE"].replace(0, 3)  # 3 = otros

# Eliminar duplicados (por seguridad)
df.drop_duplicates(inplace=True)

# Crear variable de género numérica más clara
df["genero"] = df["SEX"].map({1: "Hombre", 2: "Mujer"})

# 5. Optimización y estructuración
# Resumen de límite de crédito por género
resumen = df.groupby("genero")["LIMIT_BAL"].agg(["mean", "max", "min"])
print("\nResumen de límite de crédito por género:\n", resumen)

# Filtrar clientes mayores de 60 años
subset = df[df["AGE"] > 60]
print("\nClientes mayores de 60 años:\n", subset.head())

# Renombrar columnas para claridad
df.rename(columns={"default.payment.next.month": "default"}, inplace=True)

# 6. Exportación
df.to_csv("datos_limpios.csv", index=False)
df.to_excel("datos_limpios.xlsx", index=False)

print("\n Data Wrangling finalizado. Archivos exportados: datos_limpios.csv y datos_limpios.xlsx")
