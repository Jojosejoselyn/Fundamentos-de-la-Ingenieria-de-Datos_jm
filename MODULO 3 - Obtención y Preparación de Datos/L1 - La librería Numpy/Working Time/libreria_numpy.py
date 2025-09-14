import numpy as np

np.random.seed(42)



# Sección 1: Arrays


def operaciones_array():
    arr = np.random.randint(1, 101, 20)
    print("Array original:\n", arr)

    print("\nSuma:", np.sum(arr))
    print("Promedio:", np.mean(arr))
    print("Máximo:", np.max(arr))
    print("Mínimo:", np.min(arr))

    print("\nOrden ascendente:\n", np.sort(arr))
    print("Orden descendente:\n", np.sort(arr)[::-1])

    pares = arr[arr % 2 == 0]
    print("\nValores pares:\n", pares)

    arr_mod = arr.copy()
    arr_mod[arr_mod % 2 != 0] = -1
    print("\nArray con impares reemplazados por -1:\n", arr_mod)



# Sección 2: Matrices


def operaciones_matrices():
    A = np.random.randint(1, 51, size=(4, 4))
    B = np.random.randint(1, 51, size=(4, 4))

    print("\nMatriz A:\n", A)
    print("\nMatriz B:\n", B)

    print("\nA + B:\n", A + B)
    print("\nA - B:\n", A - B)
    print("\nA @ B (producto matricial):\n", A @ B)

    print("\nTranspuesta de A:\n", A.T)

    det_B = np.linalg.det(B)
    print("\nDeterminante de B:", det_B)

    if det_B != 0:
        print("\nInversa de B:\n", np.linalg.inv(B))
    else:
        print("\nLa matriz B no es invertible.")



# Sección 3: Funciones matemáticas


def funciones_numpy():
    x = np.linspace(0, 10, 100)

    print("\nSeno de x:\n", np.sin(x))
    print("\nCoseno de x:\n", np.cos(x))
    print("\nExponencial de x:\n", np.exp(x))

    raiz_mayor_5 = np.sqrt(x[x > 5])
    print("\nRaíz cuadrada de valores > 5:\n", raiz_mayor_5)



# Ejecución principal


if __name__ == "__main__":
    operaciones_array()
    operaciones_matrices()
    funciones_numpy()
