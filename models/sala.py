# Modificado por: Julian Cardenas
from models.servicio import Servicio

class ServicioSala(Servicio):
    """Representa un servicio de reserva de salas por horas."""

    def __init__(self, horas: int, precio_por_hora: float, **kwargs):
        # Asegura la inicialización de la clase base
        super().__init__(**kwargs)
        
        if horas <= 0 or precio_por_hora < 0:
            raise ValueError("Las horas deben ser mayores a cero y el precio no puede ser negativo.")
            
        self.horas = horas
        self.precio_por_hora = precio_por_hora

    def calcular_costo(self) -> float:
        """Calcula el costo total de la reserva de sala."""
        return float(self.horas * self.precio_por_hora)

    def descripcion(self) -> str:
        """Retorna una descripción del tiempo reservado."""
        return f"Reserva de sala: {self.horas} horas."
