import numpy as np

# Para que siempre tengamos los mismos resultados
np.random.seed(42)

print("=== WORKING TIME - DESAFÍO NUMPY ===")
print()

# Sección 1: Creación y manipulación de arrays
print("1. CREACIÓN Y MANIPULACIÓN DE ARRAYS")
print("-" * 40)

# Generar array de 20 números aleatorios entre 1 y 100
arr = np.random.randint(1, 101, 20)
print("Array original de 20 números:")
print(arr)

# Calcular estadísticas básicas
print("\nEstadísticas básicas:")
print("Suma:", np.sum(arr))
print("Promedio:", np.mean(arr))
print("Máximo:", np.max(arr))
print("Mínimo:", np.min(arr))

# Ordenar en forma ascendente y descendente
print("\nOrdenamiento:")
print("Ascendente:", np.sort(arr))
print("Descendente:", np.sort(arr)[::-1])

# Extraer valores pares
pares = arr[arr % 2 == 0]
print("\nValores pares del array:")
print(pares)

# Reemplazar impares por -1
arr_modificado = arr.copy()
arr_modificado[arr_modificado % 2 != 0] = -1
print("\nArray con impares reemplazados por -1:")
print(arr_modificado)

print("\n" + "="*50)

# Sección 2: Operaciones con matrices
print("2. OPERACIONES CON MATRICES")
print("-" * 40)

# Crear dos matrices 4x4 aleatorias
matriz1 = np.random.randint(1, 51, size=(4, 4))
matriz2 = np.random.randint(1, 51, size=(4, 4))

print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)

# Operaciones básicas entre matrices
print("\nSuma de matrices:")
print(matriz1 + matriz2)

print("\nResta de matrices:")
print(matriz1 - matriz2)

print("\nMultiplicación matricial:")
print(np.dot(matriz1, matriz2))
# También se puede usar: matriz1 @ matriz2

# Matriz transpuesta
print("\nMatriz transpuesta de la primera matriz:")
print(matriz1.T)

# Determinante de la segunda matriz
determinante = np.linalg.det(matriz2)
print("\nDeterminante de la segunda matriz:")
print(determinante)

# Calcular inversa si es posible
print("\nInversa de la segunda matriz:")
if abs(determinante) > 1e-10:  # Verificar que no sea cero
    inversa = np.linalg.inv(matriz2)
    print(inversa)
else:
    print("La matriz no es invertible (determinante muy cercano a cero)")

print("\n" + "="*50)

# Sección 3: Aplicación de funciones matemáticas
print("3. APLICACIÓN DE FUNCIONES MATEMÁTICAS")
print("-" * 40)

# Generar array de 100 valores entre 0 y 10
valores = np.linspace(0, 10, 100)
print("Array de 100 valores entre 0 y 10 generado")

# Calcular seno y coseno
seno_valores = np.sin(valores)
coseno_valores = np.cos(valores)

print("\nPrimeros 10 valores originales:")
print(valores[:10])
print("\nSeno de los primeros 10 valores:")
print(seno_valores[:10])
print("\nCoseno de los primeros 10 valores:")
print(coseno_valores[:10])

# Función exponencial
exp_valores = np.exp(valores)
print("\nExponencial de los primeros 5 valores:")
print(exp_valores[:5])

# Raíz cuadrada de elementos mayores a 5
mayores_5 = valores[valores > 5]
raiz_mayores_5 = np.sqrt(mayores_5)
print("\nCantidad de valores mayores a 5:", len(mayores_5))
print("Raíz cuadrada de los primeros 10 valores mayores a 5:")
print(raiz_mayores_5[:10])

print("\n=== DESAFÍO COMPLETADO ===")