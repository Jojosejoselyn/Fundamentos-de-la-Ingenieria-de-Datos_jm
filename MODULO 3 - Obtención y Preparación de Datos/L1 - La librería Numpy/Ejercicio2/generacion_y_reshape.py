import numpy as np

# 1. Crea un arreglo x con np.arange(1, 17) y redimensionalo en una matriz de 4x4
x = np.arange(1, 17)
print("Arreglo x original:")
print(x)

matriz_4x4 = x.reshape(4, 4)
print("\nMatriz 4x4:")
print(matriz_4x4)

# 2. Genera un arreglo de 10 elementos equidistantes entre 0 y 100 usando np.linspace()
elementos_equidistantes = np.linspace(0, 100, 10)
print("\nArreglo de 10 elementos equidistantes entre 0 y 100:")
print(elementos_equidistantes)

# 3. Crea una matriz aleatoria de 3x3 con enteros entre 1 y 20 usando np.random.randint()
matriz_aleatoria = np.random.randint(1, 20, (3, 3))
print("\nMatriz aleatoria 3x3 (enteros entre 1 y 20):")
print(matriz_aleatoria)

# 4. Aplica np.sqrt() y np.log() sobre las matrices creadas (cuando sea posible)
print("\nAplicando np.sqrt() a la matriz 4x4:")
sqrt_matriz = np.sqrt(matriz_4x4)
print(sqrt_matriz)

print("\nAplicando np.log() a la matriz 4x4:")
log_matriz = np.log(matriz_4x4)
print(log_matriz)

print("\nAplicando np.sqrt() a la matriz aleatoria:")
sqrt_aleatoria = np.sqrt(matriz_aleatoria)
print(sqrt_aleatoria)

print("\nAplicando np.log() a la matriz aleatoria:")
log_aleatoria = np.log(matriz_aleatoria)
print(log_aleatoria)

# 5. ¿Qué diferencias notas en la forma de aplicar funciones sobre arreglos enteros vs flotantes?
print("\n5. Diferencias entre arreglos enteros vs flotantes:")
print("Arreglo entero original:", matriz_aleatoria.dtype)
print("Resultado sqrt (flotante):", sqrt_aleatoria.dtype)
print("Resultado log (flotante):", log_aleatoria.dtype)

# Comparación adicional
arreglo_entero = np.array([1, 4, 9, 16])
arreglo_flotante = np.array([1.0, 4.0, 9.0, 16.0])

print("\nEjemplo con enteros:", arreglo_entero.dtype)
print("Sqrt de enteros:", np.sqrt(arreglo_entero), "- tipo:", np.sqrt(arreglo_entero).dtype)

print("\nEjemplo con flotantes:", arreglo_flotante.dtype)
print("Sqrt de flotantes:", np.sqrt(arreglo_flotante), "- tipo:", np.sqrt(arreglo_flotante).dtype)