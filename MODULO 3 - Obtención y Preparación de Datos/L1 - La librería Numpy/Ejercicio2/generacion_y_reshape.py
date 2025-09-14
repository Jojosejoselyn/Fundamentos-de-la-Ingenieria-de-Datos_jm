import numpy as np

np.random.seed(42)  # para que los aleatorios sean reproducibles

# 1) arange(1, 17) -> reshape a 4x4
x = np.arange(1, 17)
X = x.reshape(4, 4)
print("Matriz X (4x4, desde 1 a 16):\n", X)

# 2) linspace de 10 puntos equidistantes entre 0 y 100
v = np.linspace(0, 100, 10)
print("\nVector v (10 valores 0..100):\n", v)

# 3) matriz aleatoria 3x3 con enteros 1..20
A = np.random.randint(1, 21, size=(3, 3))
print("\nMatriz A aleatoria (enteros 1..20):\n", A)

# 4) aplicar sqrt y log 

X_sqrt = np.sqrt(X)
X_log  = np.log(X.astype(float))    
A_sqrt = np.sqrt(A)
A_log  = np.log(A.astype(float))

print("\n√X:\n", X_sqrt)
print("\nlog(X):\n", X_log)
print("\n√A:\n", A_sqrt)
print("\nlog(A):\n", A_log)

# 5) Nota rápida sobre enteros vs flotantes
print("\nDtypes:")
print("X:", X.dtype, "| √X:", X_sqrt.dtype, "| log(X):", X_log.dtype)
print("A:", A.dtype, "| √A:", A_sqrt.dtype, "| log(A):", A_log.dtype)
