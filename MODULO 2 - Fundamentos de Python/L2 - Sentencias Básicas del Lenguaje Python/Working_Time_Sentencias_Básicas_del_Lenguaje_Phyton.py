# Working_Time_Sentencias_Básicas_del_Lenguaje_Python.py
# Este programa lo desarrollé para aplicar condicionales y entrada de datos en Python.
# El objetivo es clasificar a una persona por su edad y mostrar información según lo que elija.

# Paso 1: Pedimos nombre y edad al usuario
nombre = input("¿Cuál es tu nombre? ")

try:
    edad = int(input("¿Qué edad tienes? "))
except ValueError:
    print("La edad ingresada no es válida. Intenta de nuevo con un número entero.")
    exit()

# Paso 2: Clasificamos según edad
if edad < 18:
    categoria = "menor de edad"
elif edad < 60:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

# Paso 3: Mostramos mensaje personalizado
print(f"\n¡Hola, {nombre}! Según tu edad, eres {categoria}.")

# Paso 4: Preguntamos si quiere ver el resumen general
ver_resumen = input("\n¿Quieres ver el resumen de las categorías? (responde 'si' o 'no'): ").strip().lower()

if ver_resumen == "si":
    print("\n CATEGORÍAS DE EDAD")
    print("- Menor de edad: menos de 18 años")
    print("- Adulto: entre 18 y 59 años")
    print("- Adulto mayor: 60 años o más")
else:
    print("\n Gracias por usar el programa.")

# PLUS: Guardamos conteo acumulado por categoría sin usar bucles
try:
    with open("conteo.txt", "r") as archivo:
        lineas = archivo.readlines()
        menores = int(lineas[0])
        adultos = int(lineas[1])
        mayores = int(lineas[2])
except FileNotFoundError:
    menores = adultos = mayores = 0

# Sumamos al grupo correspondiente
if categoria == "menor de edad":
    menores += 1
elif categoria == "adulto":
    adultos += 1
else:
    mayores += 1

# Guardamos la información actualizada
with open("conteo.txt", "w") as archivo:
    archivo.write(f"{menores}\n{adultos}\n{mayores}")

# Mostramos resumen actualizado
print("\n📊 Conteo acumulado hasta ahora:")
print(f"- Menores de edad: {menores}")
print(f"- Adultos: {adultos}")
print(f"- Adultos mayores: {mayores}")
