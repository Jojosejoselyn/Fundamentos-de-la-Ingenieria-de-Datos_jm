import numpy as np

# 1. Crear una matriz A de 3x3 con números enteros del 1 al 9
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matriz A original:\n", A)

# 2. Sumar 10 a cada elemento de la matriz
A_suma = A + 10
print("\nMatriz A + 10:\n", A_suma)

# 3. Multiplicar la matriz por 2
A_mult = A * 2
print("\nMatriz A * 2:\n", A_mult)

# 4. Seleccionar los elementos mayores a 5
mayores_5 = A[A > 5]
print("\nElementos mayores a 5:\n", mayores_5)

# 5. Referencia vs copia
# Caso 1: referencia
B = A
B[0, 0] = 100   # modificamos un elemento
print("\nDespués de modificar B (referencia):")
print("Matriz A:\n", A)
print("Matriz B:\n", B)

# Caso 2: copia real
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])  # restauramos A
C = A.copy()
C[0, 0] = 200
print("\nDespués de modificar C (copia):")
print("Matriz A:\n", A)
print("Matriz C:\n", C)
