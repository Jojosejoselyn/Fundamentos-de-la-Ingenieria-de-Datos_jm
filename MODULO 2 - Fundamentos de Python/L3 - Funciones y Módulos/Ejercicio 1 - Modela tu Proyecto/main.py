import operaciones

def main():
    print("Calculadora con módulo externo\n")
    
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    print(f"Suma: {operaciones.sumar(a, b)}")
    print(f"Resta: {operaciones.restar(a, b)}")
    print(f"Multiplicación: {operaciones.multiplicar(a, b)}")
    print(f"División: {operaciones.dividir(a, b)}")

if __name__ == "__main__":
    main()

