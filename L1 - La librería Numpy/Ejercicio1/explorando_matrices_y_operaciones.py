# Ejercicio 1: Explorando matrices y operaciones básicas

import numpy as np

# 1. Importa la librería NumPy como np
print("Matriz A original:")

# 2. Crea una matriz A de 3x3 con números enteros del 1 al 9
A = np.array([[1, 2, 3],
              [4, 5, 6], 
              [7, 8, 9]])
print(A)

# 3. Realizar las siguientes operaciones:

# Suma 10 a cada elemento de la matriz
suma_resultado = A + 10
print("\nSuma 10 a cada elemento:")
print(suma_resultado)

# Multiplica la matriz por 2
mult_resultado = A * 2
print("\nMultiplica por 2:")
print(mult_resultado)

# Extrae los elementos mayores a 5 utilizando selección condicional
mayores_5 = A[A > 5]
print("\nElementos mayores a 5:")
print(mayores_5)

# 4. Asigna la matriz a una nueva variable B = A y modifica un valor de B
B = A
print("\nMatriz A antes de modificar B:")
print(A)

B[0, 0] = 100
print("\nDespués de B[0, 0] = 100:")
print("A:", A)
print("B:", B)

# Ahora con copia
A = np.array([[1, 2, 3],
              [4, 5, 6], 
              [7, 8, 9]])

C = A.copy()
C[0, 0] = 200
print("\nCon A.copy():")
print("A:", A)
print("C:", C)