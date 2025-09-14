# Pide nombre y edad al usuario y dice si es mayor o menor de edad

print("Bienvenido/a al verificador de edad.")

def es_mayor(edad):
# Retorna True si la edad es mayor o igual a 18
    return edad >= 18

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Qué edad tienes? "))

# Usa la función para verificar si es mayor o menor
if es_mayor(edad):
    print(f"{nombre}, eres mayor de edad.")
else:
    print(f"{nombre}, eres menor de edad.")
