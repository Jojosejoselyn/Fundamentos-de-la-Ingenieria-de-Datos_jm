# Práctica con Python - Verificación de edad

# Solicitar nombre y edad al usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# Usar estructura condicional para verificar si es mayor o menor de edad
if edad >= 18:
    condicion = "mayor de edad"
else:
    condicion = "menor de edad"

# Imprimir mensaje de saludo con nombre y condición
print(f"Hola {nombre}, eres {condicion}")