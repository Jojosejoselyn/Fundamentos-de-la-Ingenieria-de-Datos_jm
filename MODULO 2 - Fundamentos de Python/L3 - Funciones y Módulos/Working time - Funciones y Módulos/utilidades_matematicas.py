import math

def area_circulo(radio):
    """
    Calcula el área de un círculo.

    Parámetros:
    radio (float): Radio del círculo.

    Retorna:
    float: Área calculada.
    """
    return math.pi * radio ** 2

def area_rectangulo(ancho, alto):
    """
    Calcula el área de un rectángulo.

    Parámetros:
    ancho (float): Ancho del rectángulo.
    alto (float): Alto del rectángulo.

    Retorna:
    float: Área calculada.
    """
    return ancho * alto

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Parámetros:
    base (float): Base del triángulo.
    altura (float): Altura del triángulo.

    Retorna:
    float: Área calculada.
    """
    return (base * altura) / 2

def factorial(numero):
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
    numero (int): Número del cual se quiere obtener el factorial.

    Retorna:
    int: Resultado del factorial.
    """
    if numero == 0 or numero == 1:
        return 1
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

def es_primo(numero):
    """
    Determina si un número es primo.

    Parámetros:
    numero (int): Número a evaluar.

    Retorna:
    bool: True si es primo, False si no lo es.
    """
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def area_poligono_regular(n_lados, longitud_lado):
    """
    Calcula el área de un polígono regular.

    Parámetros:
    n_lados (int): Número de lados del polígono (mínimo 3).
    longitud_lado (float): Longitud de cada lado.

    Retorna:
    float: Área del polígono regular.
    """
    if n_lados < 3:
        return "Un polígono debe tener al menos 3 lados."
    return (n_lados * longitud_lado ** 2) / (4 * math.tan(math.pi / n_lados))