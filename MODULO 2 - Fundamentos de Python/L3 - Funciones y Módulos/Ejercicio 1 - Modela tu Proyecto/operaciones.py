def sumar(a, b):
    """
    Suma dos números.

    Parámetros:
    a (float): Primer número.
    b (float): Segundo número.

    Retorna:
    float: Resultado de la suma.
    """
    return a + b

def restar(a, b):
    """
    Resta dos números.

    Parámetros:
    a (float): Minuendo.
    b (float): Sustraendo.

    Retorna:
    float: Resultado de la resta.
    """
    return a - b

def multiplicar(a, b):
    """
    Multiplica dos números.

    Parámetros:
    a (float): Primer número.
    b (float): Segundo número.

    Retorna:
    float: Resultado de la multiplicación.
    """
    return a * b

def dividir(a, b):
    """
    Divide dos números.

    Parámetros:
    a (float): Dividendo.
    b (float): Divisor.

    Retorna:
    float: Resultado de la división o mensaje de error si b es 0.
    """
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b
