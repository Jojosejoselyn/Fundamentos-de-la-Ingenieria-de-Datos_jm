def calculadora():
    while True:
        try:
            # Pedimos los números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            # Pedimos la operación
            operador = input("Ingresa la operación (+, -, *, /): ")

            # Según el operador, hacemos la operación
            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero.")
                resultado = num1 / num2
            else:
                raise ValueError("Operador no válido. Usa +, -, * o /.")

            print(f"Resultado: {num1} {operador} {num2} = {resultado}")

        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        finally:
            print("Operación finalizada.\n")

        # Preguntar si el usuario quiere seguir
        repetir = input("¿Quieres realizar otra operación? (s/n): ")
        if repetir.lower() != "s":
            break

# Bloque principal
if __name__ == "__main__":
    calculadora()
