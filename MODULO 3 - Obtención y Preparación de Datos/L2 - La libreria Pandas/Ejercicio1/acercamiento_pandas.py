# PASO PREVIO: Instalar pandas
# Ejecuta en tu terminal: pip install pandas

import pandas as pd

# 1. Importar la librería pandas como pd
print("1. Pandas importado correctamente")

# 2. Leer el archivo data.csv con pd.read_csv('data.csv') y asignarlo a df
df = pd.read_csv('data.csv')
print("2. Archivo cargado en variable df")

# 3. Usar df.head() para ver los primeros registros
print("\n3. Primeros 5 registros:")
print(df.head())

# 4. Usar df.info() para revisar estructura y tipos de datos
print("\n4. Información general del DataFrame:")
print(df.info())

# 5. Usar df.describe() para ver estadísticas básicas
print("\n5. Estadísticas descriptivas:")
print(df.describe())

# 6. Aplicar df.isnull().sum() para detectar valores nulos
print("\n6. Valores nulos por columna:")
print(df.isnull().sum())

# 7. Usar df.mean(), df.median() y df.std() solo para columnas numéricas
print("\n7. Medidas estadísticas adicionales:")
columnas_numericas = df.select_dtypes(include=['number'])
print("Media por columna:")
print(columnas_numericas.mean())
print("\nMediana por columna:")
print(columnas_numericas.median())
print("\nDesviación estándar por columna:")
print(columnas_numericas.std())

print("\n8. Interpretación breve:")
print("- El dataset tiene", len(df), "registros")
print("- Contiene", len(df.columns), "columnas")
print("- Se pueden identificar patrones en las estadísticas básicas")
print("- Los valores nulos requieren atención si existen")