# hola_edad.py - Saludo con verificación de edad

# Pide el nombre
nombre = input("¿Cuál es tu nombre? ")

# Pide la edad y la convierte a entero
edad = int(input("¿Qué edad tienes? "))

# Muestra el saludo
print(f"¡Hola, {nombre}! Bienvenido al mundo de Python.")

# Verifica si es mayor o menor de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
