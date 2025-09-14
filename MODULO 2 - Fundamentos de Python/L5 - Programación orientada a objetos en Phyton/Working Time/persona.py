# Working Time - Programación Orientada a Objetos (POO)
# Clase: Persona
# Autor@: Jose (estilo propio, simple y legible)

import re

class Persona:
    """
    Clase que modela a una persona con:
    - nombre
    - edad
    - correo_electronico
    """

    def __init__(self, nombre: str, edad: int, correo_electronico: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.correo_electronico = correo_electronico

    def mostrar_datos(self) -> None:
        """Muestra los datos de la persona en un formato amigable."""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Email: {self.correo_electronico}")

    def validar_correo(self) -> bool:
        """Verifica si el correo electrónico es válido usando expresiones regulares."""
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, self.correo_electronico) is not None

    def actualizar_datos(self, nombre: str = None, edad: int = None, correo_electronico: str = None) -> None:
        """Permite actualizar uno o más atributos de la persona."""
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
        if correo_electronico:
            self.correo_electronico = correo_electronico

    def es_mayor_de_edad(self) -> bool:
        """Retorna True si la persona tiene 18 años o más, False en caso contrario."""
        return self.edad >= 18

    def comparar_edad(self, otra_persona) -> str:
        """Compara la edad entre dos personas y devuelve quién es mayor."""
        if self.edad > otra_persona.edad:
            return f"{self.nombre} es mayor que {otra_persona.nombre}."
        elif self.edad < otra_persona.edad:
            return f"{otra_persona.nombre} es mayor que {self.nombre}."
        else:
            return f"{self.nombre} y {otra_persona.nombre} tienen la misma edad."

    def __str__(self) -> str:
        return f"Persona({self.nombre}, {self.edad} años, {self.correo_electronico})"


# ----------------------- Mini demo -----------------------
if __name__ == "__main__":
    p1 = Persona("Carlos", 28, "carlos@mail.com")
    p2 = Persona("María", 17, "maria@dominio")

    p1.mostrar_datos()
    print("Correo válido:", p1.validar_correo())
    print("Es mayor de edad:", p1.es_mayor_de_edad())

    p2.mostrar_datos()
    print("Correo válido:", p2.validar_correo())
    print("Es mayor de edad:", p2.es_mayor_de_edad())

    # Actualizar datos de María
    p2.actualizar_datos(edad=19, correo_electronico="maria@gmail.com")
    p2.mostrar_datos()

    # Comparar edades
    print(p1.comparar_edad(p2))
