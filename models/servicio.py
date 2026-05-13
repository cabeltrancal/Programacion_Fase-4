# Modificado por: Julian Cardenas
from abc import ABC, abstractmethod

class Servicio(ABC):
    """
    Clase abstracta base para todos los servicios del sistema.
    Define el contrato que deben seguir las clases hijas.
    """

    def __init__(self, **kwargs):
        """
        Constructor base que permite recibir atributos adicionales 
        en las clases que heredan de esta.
        """
        super().__init__()

    @abstractmethod
    def calcular_costo(self) -> float:
        """Método obligatorio para calcular el costo total del servicio."""
        pass

    @abstractmethod
    def descripcion(self) -> str:
        """Método obligatorio para retornar el resumen del servicio."""
        pass
