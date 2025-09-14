# Diccionario de empleados 
empleados = {
    'emp1': {'nombre': 'Carlos', 'edad': 28},
    'emp2': {'nombre': 'Luis', 'edad': 35},
    'emp3': {'nombre': 'Camila', 'edad': 22},
    'emp4': {'nombre': 'Damari', 'edad': 40},
    'emp5': {'nombre': 'Osvaldo', 'edad': 27}
}

# Lista para guardar empleados menores de 30
menores_30 = []

# Mostrar empleados mayores de 30
print("Empleados mayores de 30 años:")
for emp_id, datos in empleados.items():
    if datos['edad'] > 30:
        print(f"- {datos['nombre']} ({datos['edad']} años)")
    elif datos['edad'] < 30:
        menores_30.append(datos['nombre'])

# Mostrar resultado final
print("\nEmpleados menores de 30 años:", menores_30)
print("Cantidad total de empleados:", len(empleados))
