import csv  # Importación global para exportar a CSV

# Diccionario principal para guardar los productos
inventario = {}

# Función para agregar productos al inventario
def agregar_producto(nombre, cantidad, precio, categoria):
    inventario[nombre] = {
        'cantidad': cantidad,
        'precio': precio,
        'categoria': categoria
    }

# Función para eliminar productos
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# Función para actualizar cantidad y/o precio
def actualizar_producto(nombre, cantidad=None, precio=None):
    if nombre in inventario:
        if cantidad is not None:
            inventario[nombre]['cantidad'] = cantidad
        if precio is not None:
            inventario[nombre]['precio'] = precio
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# Función para listar productos por categoría
def listar_por_categoria(categoria):
    print(f"\nProductos en la categoría '{categoria}':")
    for nombre, detalles in inventario.items():
        if detalles['categoria'] == categoria:
            print(f"- {nombre} | Cantidad: {detalles['cantidad']} | Precio: ${detalles['precio']}")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = 0
    for detalles in inventario.values():
        total += detalles['cantidad'] * detalles['precio']
    return total

# Función para exportar el inventario a un archivo CSV
def exportar_inventario_csv(nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Producto', 'Cantidad', 'Precio', 'Categoría'])
        for nombre, detalles in inventario.items():
            writer.writerow([nombre, detalles['cantidad'], detalles['precio'], detalles['categoria']])

# Ejemplo de uso 
agregar_producto("Laptop", 5, 750, "Electrónica")
agregar_producto("Teclado", 20, 25, "Electrónica")
agregar_producto("Manzana", 100, 0.3, "Alimentos")
agregar_producto("Jugo", 30, 1.5, "Alimentos")

actualizar_producto("Laptop", precio=720)
eliminar_producto("Jugo")

listar_por_categoria("Electrónica")

print("\nValor total del inventario:", calcular_valor_total())

exportar_inventario_csv("inventario.csv")