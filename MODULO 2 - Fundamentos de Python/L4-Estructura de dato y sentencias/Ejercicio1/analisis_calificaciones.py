# Lista de calificaciones de ejemplo 
calificaciones = [55, 72, 89, 45, 60, 100, 68, 35, 91, 74]

# Acumulador para la suma total de notas
suma_total = 0

# Contador de estudiantes aprobados
aprobados = 0

# Lista para guardar solo las calificaciones aprobadas
notas_aprobadas = []

# Recorremos cada nota en la lista
for nota in calificaciones:
    # Sumar al total
    suma_total += nota

    # Verificamos si es una nota aprobada
    if nota >= 60:
        aprobados += 1
        notas_aprobadas.append(nota)

# Calcular el promedio general
promedio = suma_total / len(calificaciones)

# Mostrar resultados
print("Promedio general:", promedio)
print("Cantidad de estudiantes aprobados:", aprobados)
print("Notas aprobadas:", notas_aprobadas)
