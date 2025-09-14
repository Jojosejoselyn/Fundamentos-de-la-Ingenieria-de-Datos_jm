from __future__ import annotations
from typing import Literal

EstadoAuto = Literal["detenido", "circulando", "estacionado", "danado"]

class Auto:
    """
    Modelo simple de un Auto con:
    - Atributos (propiedades)
    - Métodos (comportamientos)
    - Estado (cambia según lo que haga el auto)
    """

    # Estados permitidos
    ESTADOS_VALIDOS = {"detenido", "circulando", "estacionado", "danado"}

    def __init__(
        self,
        color: str,
        peso: float,                # en kg
        tamano: str,                # ejemplo: "mediano", "compacto", "SUV"
        alto: float,                # en metros
        largo: float,               # en metros
        cantidad_ruedas: int,
        cantidad_puertas: int,
        tipo: str                   # ejemplo: "sedán", "hatchback", "pickup"
    ) -> None:
        # Propiedades visibles
        self.color = color
        self.peso = peso
        self.tamano = tamano
        self.alto = alto
        self.largo = largo
        self.cantidad_ruedas = cantidad_ruedas
        self.cantidad_puertas = cantidad_puertas
        self.tipo = tipo

        # Atributos internos
        self._estado: EstadoAuto = "detenido"
        self._velocidad: int = 0  # km/h

    # Getters/Setters
    @property
    def estado(self) -> EstadoAuto:
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado: EstadoAuto) -> None:
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido: {nuevo_estado}")
        self._estado = nuevo_estado

    @property
    def velocidad(self) -> int:
        return self._velocidad

    # Métodos
    def arrancar(self) -> None:
        if self.estado == "danado":
            print("No se puede arrancar: el auto está dañado.")
            return
        if self.estado == "circulando":
            print("El auto ya estaba en marcha.")
            return
        self.estado = "circulando"
        if self.velocidad == 0:
            self._velocidad = 10  # arranca con una velocidad base
        print(f"Arrancando... Estado: {self.estado}, velocidad: {self.velocidad} km/h")

    def frenar(self, fuerza: int = 10) -> None:
        if self.estado not in ("circulando", "detenido"):
            print("No tiene sentido frenar si el auto no está en movimiento.")
            return
        self._velocidad = max(0, self.velocidad - abs(fuerza))
        if self.velocidad == 0:
            self.estado = "detenido"
        print(f"Frenando... Estado: {self.estado}, velocidad: {self.velocidad} km/h")

    def acelerar(self, incremento: int = 10) -> None:
        if self.estado == "danado":
            print("No se puede acelerar: el auto está dañado.")
            return
        if self.estado in ("detenido", "estacionado"):
            self.arrancar()
        self._velocidad = max(0, self.velocidad + abs(incremento))
        self.estado = "circulando"
        print(f"Acelerando... Estado: {self.estado}, velocidad: {self.velocidad} km/h")

    def girar(self, direccion: Literal["izquierda", "derecha"]) -> None:
        if self.estado != "circulando":
            print("El auto debe estar circulando para girar.")
            return
        print(f"Girando a la {direccion} a {self.velocidad} km/h.")

    def estacionar(self) -> None:
        self._velocidad = 0
        self.estado = "estacionado"
        print("El auto ha sido estacionado.")

    def danar(self, motivo: str = "desconocido") -> None:
        self.estado = "danado"
        self._velocidad = 0
        print(f"El auto se dañó (motivo: {motivo}). Quedó inmovilizado.")

    def reparar(self) -> None:
        if self.estado != "danado":
            print("El auto no estaba dañado.")
            return
        self.estado = "detenido"
        print("El auto fue reparado. Estado: detenido.")

    # Representación
    def __str__(self) -> str:
        return (f"Auto({self.tipo}, color {self.color}, {self.cantidad_puertas} puertas, "
                f"{self.cantidad_ruedas} ruedas) | Estado: {self.estado}, "
                f"Velocidad: {self.velocidad} km/h")


# Mini demo
if __name__ == "__main__":
    mi_auto = Auto(
        color="negro",
        peso=1500.0,
        tamano="mediano",
        alto=1.45,
        largo=4.8,
        cantidad_ruedas=4,
        cantidad_puertas=4,
        tipo="sedán"
    )

    print(mi_auto)              
    mi_auto.arrancar()
    mi_auto.acelerar(20)
    mi_auto.girar("izquierda")
    mi_auto.frenar(15)
    mi_auto.estacionar()
    mi_auto.danar("neumático pinchado")
    mi_auto.arrancar()          
    mi_auto.reparar()
    print(mi_auto)              
