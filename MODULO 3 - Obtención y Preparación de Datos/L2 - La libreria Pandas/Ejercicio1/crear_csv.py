import pandas as pd

# Crear datos más simples
datos = {
    'edad': [25, 30, 22, 28, 35, 26],
    'salario': [45000, 52000, 38000, 48000, 60000, 44000],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Madrid', 'Barcelona']
}

df = pd.DataFrame(datos)
# Guardar en la carpeta Ejercicio1
df.to_csv('./Ejercicio1/data.csv', index=False)

print("Archivo data.csv creado exitosamente en la carpeta Ejercicio1")
print("Contenido:")
print(df)





