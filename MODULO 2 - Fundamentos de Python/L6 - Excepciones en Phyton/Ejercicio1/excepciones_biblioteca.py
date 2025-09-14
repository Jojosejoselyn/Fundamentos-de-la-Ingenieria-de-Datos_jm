# excepciones_biblioteca.py
# Ejercicio 1 - Préstamo simple en una biblioteca
# Clase 6 Módulo 2: Excepciones en Python

# Excepción personalizada
class LibroNoDisponibleError(Exception):
    def __init__(self, titulo):
        super().__init__(f"El libro '{titulo}' no está disponible en este momento.")

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, stock):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        # Diccionario: clave = título, valor = objeto Libro
        self.catalogo = {}

    def agregar_libro(self, libro):
        self.catalogo[libro.titulo] = libro

    def prestar_libro(self, titulo):
        # Verificar si el libro está en el catálogo
        if titulo not in self.catalogo:
            raise LibroNoDisponibleError(titulo)

        libro = self.catalogo[titulo]

        # Verificar stock
        if libro.stock <= 0:
            raise LibroNoDisponibleError(titulo)

        # Reducir stock en 1
        libro.stock -= 1
        print(f"Libro prestado: {libro.titulo} - Autor: {libro.autor}")
        print(f"Stock restante: {libro.stock}")

# Bloque principal de prueba
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Agregar algunos libros
    biblioteca.agregar_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez", 2))
    biblioteca.agregar_libro(Libro("El Quijote", "Miguel de Cervantes", 1))

    try:
        biblioteca.prestar_libro("Cien Años de Soledad")  # funciona
        biblioteca.prestar_libro("Cien Años de Soledad")  # funciona
        biblioteca.prestar_libro("Cien Años de Soledad")  # lanza excepción
    except LibroNoDisponibleError as e:
        print(f"Error: {e}")

    try:
        biblioteca.prestar_libro("Libro inventado")  # no existe, excepción
    except LibroNoDisponibleError as e:
        print(f"Error: {e}")
