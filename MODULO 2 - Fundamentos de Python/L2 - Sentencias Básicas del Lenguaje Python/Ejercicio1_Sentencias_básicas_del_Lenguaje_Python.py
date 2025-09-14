# Programa: Verificación de beneficio por edad y país

# Paso 1: Captura de datos
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
pais = input("Ingresa tu país de residencia: ")

# Paso 2: Conversión de tipos y normalización
edad = int(edad)
pais = pais.lower()

# Paso 3: Validación de condiciones
paises_validos = ["argentina", "chile", "colombia"]
puede_acceder = edad >= 18 and pais in paises_validos

# Paso 4: Mensaje personalizado
print(f"\\nHola, {nombre}. Tienes {edad} años y vives en {pais.capitalize()}.")

if puede_acceder:
    print("Puedes acceder al beneficio.")
else:
    print("No puedes acceder al beneficio.")
